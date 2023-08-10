from models.modules.inv_arch import SAINet
from models.modules.subnet_constructor import subnet
from models.modules.quantization import Quantization

from torch.nn.parallel import DataParallel, DistributedDataParallel
from collections import OrderedDict
import torch
import torch.nn as nn
import torch.nn.functional as F
import os, glob
import cv2
import numpy as np
import math
def load_network(load_path, network, strict=True):
    if isinstance(network, nn.DataParallel) or isinstance(network, DistributedDataParallel):
        network = network.module
    load_net = torch.load(load_path)
    load_net_clean = OrderedDict()  # remove unnecessary 'module.'
    for k, v in load_net.items():
        if k.startswith('module.'):
            load_net_clean[k[7:]] = v
        else:
            load_net_clean[k] = v
    network.load_state_dict(load_net_clean, strict=strict)

def test_pipeline():
    down_num = int(math.log(2, 2)) # opt_net['scale']=2
    net = SAINet(channel_in=3, channel_out=3, subnet_constructor=subnet('DBNet', 'xavier'),
                 e_blocks=5, v_blocks=3, down_num=down_num, gmm_components=5)
    # print(net)
    # pretrain_model = '../experiments/pretrained_models/SAINx2_JPEG.pth'
    pretrain_model = '../experiments/pretrained_models/SAINx2_WebP.pth'
    load_network(pretrain_model, net, strict=True)
    net.eval()
    net = net.cuda()
    Quantize = Quantization()

    img_path = r'./Test_Image/000016.png'

    if os.path.isfile(img_path):
        paths = [img_path]
    else:
        paths = sorted(glob.glob(os.path.join(img_path, '*')))

    for idx, path in enumerate(paths):
        imgname, extension = os.path.splitext(os.path.basename(path))
        # print('Testing', idx, imgname)

        img = cv2.imread(path, cv2.IMREAD_UNCHANGED)[:, :, ::-1]
        print('Testing', idx, imgname, img.shape)
        # img = cv2.resize(img, (256, 256), interpolation=cv2.INTER_LANCZOS4)
        img = torch.from_numpy(np.ascontiguousarray(np.transpose(img, (2, 0, 1))) / 255.).float()
        img = img.unsqueeze(0).cuda()
        # _, _, H, W = img.size()
        # padder_size = 32
        # mod_pad_h = (padder_size - H % padder_size) % padder_size
        # mod_pad_w = (padder_size - W % padder_size) % padder_size
        # img = F.pad(img, (0, mod_pad_w, 0, mod_pad_h))
        with torch.no_grad():
            output, LR = net(img)
            LR = Quantize(LR)
        # output = output[:, :, :H*4, :W*4]
        print(output.shape)
        print(LR.shape)

        output_img = LR.data.squeeze().float().cpu().clamp_(0, 1).numpy()
        output_img = np.transpose(output_img[[2, 1, 0], :, :], (1, 2, 0))
        output = (output_img * 255.0).round().astype(np.uint8)
        # output = cv2.resize(
        #     output, (
        #         int(w_input * outscale),
        #         int(h_input * outscale),
        #     ), interpolation=cv2.INTER_LANCZOS4)
        save_path = './'
        save_path = os.path.join(save_path, f'{imgname}.{extension}')
        cv2.imwrite(save_path, output)

if __name__ == '__main__':
    test_pipeline()
