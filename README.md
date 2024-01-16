# Learning-Rescaling

# Learning-Rescaling
开源的图像缩放算法   
图像缩放是一种常用的双向操作，首先将高分辨率图像降采样以适应各种显示屏幕或便于存储和带宽使用，然后将相应的低分辨率图像上采样以恢复原始分辨率或放大图像中的细节。

## 目录
  - [1. Learning-Rescaling](#1-Learning-Rescaling)

    
###  1. <a name='Image-Rescaling'></a>Image-Rescaling
* DLV-IRN (Arxiv 2023-03)：
  * paper：https://openreview.net/pdf?id=nCwStXFDQu
  * code：https://github.com/zqcrafts/FouriDown
  * 简介：提出了一种新颖的傅里叶域下采样范式，简称为FouriDown，它将现有的下采样技术统一起来。
  * 
* DLV-IRN (Arxiv 2023-03)：
  * paper：https://arxiv.org/pdf/2303.06747.pdf
  * code：None
  * 简介：出了辅助编码模块，以进一步推动图像缩放性能的极限。提出了两种在缩小比例的LR图像中存储编码的潜在变量的选择，这两种选择在现有的图像文件格式中都很容易得到支持。一个保存为alpha通道，另一个保存为图像头中的元数据，相应的模块分别表示为后缀-a和-m。
    
* SAIN (AAAI 2023 Oral)：
  * paper：https://arxiv.org/pdf/2303.02353.pdf
  * code：https://github.com/yang-jin-hai/SAIN
  * 简介：提出了一种自对称可逆网络(SAIN),用于具有压缩感知的图像重采样。为了解决分布偏移问题，我们首先开发了一个端到端的不对称框架，分别为高质量和压缩的LR图像分别设计了两个独立的双射映射。然后，基于这个框架的实证分析，使用各向同性高斯混合模型来建模丢失信息(包括降采样和压缩)的分布，并提出增强型可逆块以在一次前向传播过程中生成高质量/压缩的LR图像。此外，设计了一系列损失函数来规范学到的LR图像并增强其可逆性。
  * 测试结果：输出的LR带有严重的JPEG压缩，输出的压缩重建图质量可以。可尝试根据需求修改

* HyperThumbnail (AAAI 2023 Oral)：
  * paper：https://arxiv.org/pdf/2304.01064.pdf
  * code：https://github.com/AbnerVictor/HyperThumbnail
  * 简介：提出了一种新的框架(超缩略图),用于实时6K率失真感知图像缩放。首先通过带有我们提出的量化预测模块的编码器将HR图像嵌入到JPEG LR缩略图中，该模块最小化嵌入LR JPEG缩略图的文件大小，同时最大化HR重建质量。然后，一个高效的频率感知解码器实时从LR中重建高保真度的HR图像。
  * 测试结果：未运行、

* HCD (ICCV 2023)：
  * paper：https://arxiv.org/pdf/2211.10643.pdf
  * code：None
  * 简介：提出了一种协作的降尺度方案 Hierarchical Collaborative Downscaling（HCD），其重点是获得图像的更好的下采样表示，而不是学习模型，该方案优化了 HR 和 LR 图像域的表示，获得了更优的下采样图片。
  * 测试结果：未运行
  * 复现：HCD方案包括两个过程，包括协作HR生成和协作LR生成。首先迭代地优化对原始HR图像的扰动，以生成协作的HR示例。然后，得到缩小比例的图像，并生成协作LR示例。最后，可以从更好的缩小表示中得到更好的高分辨率图像。

* MULLER (ICCV 2023)：
  * paper：https://arxiv.org/pdf/2304.02859.pdf
  * code：None
  * 简介：我们提出了一种非常轻量级的多层拉普拉斯缩放器，只需要少量可训练参数，被称为MULLER缩放器。MULLER具有带通特性，即它学会提高某些频率子带中的细节，从而有利于下游识别模型。
  * 测试结果：未运行

* IRN (IJCV 2022)：
  * paper：https://arxiv.org/pdf/2210.04188.pdf
  * code：https://github.com/pkuxmq/Invertible-Image-Rescaling
  * 简介：提出了一种新颖的可逆框架来处理这个一般问题，它从一个新的角度建模了双向退化和恢复，即可逆双射变换。可逆性使得框架能够模型预退化时的失真信息损失，从而在后恢复过程中减轻欠定问题。
  * 测试结果：未运行
 
* InvDN (CVPR 2021)：
  * paper：https://arxiv.org/pdf/2104.10546v1.pdf
  * code：https://github.com/Yang-Liu1082/InvDN
  * 简介：提出了一种可逆去噪网络(InvDN)来解决这个挑战。InvDN将含噪声的输入转换为低分辨率的干净图像和一个包含噪声的潜在表示。为了去除噪声并恢复干净图像，InvDN在反转过程中用另一个从先验分布中采样的潜在表示替换含噪声的潜在表示。
  * 测试结果：未运行
    
