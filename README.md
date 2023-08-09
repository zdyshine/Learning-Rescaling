# Learning-Rescaling

# Learning-Rescaling
开源的图像缩放算法  

## 目录
  - [1. Learning-Rescaling](#1-Learning-Rescaling)

    
###  1. <a name='Image-enhance'></a>Image-enhance
* SAIN (AAAI 2023 Oral)：
  * paper：https://arxiv.org/pdf/2303.02353.pdf
  * code：https://github.com/yang-jin-hai/SAIN
  * 简介：提出了一种自对称可逆网络(SAIN),用于具有压缩感知的图像重采样。为了解决分布偏移问题，我们首先开发了一个端到端的不对称框架，分别为高质量和压缩的LR图像分别设计了两个独立的双射映射。然后，基于这个框架的实证分析，使用各向同性高斯混合模型来建模丢失信息(包括降采样和压缩)的分布，并提出增强型可逆块以在一次前向传播过程中生成高质量/压缩的LR图像。此外，设计了一系列损失函数来规范学到的LR图像并增强其可逆性。
  * 测试结果：未运行

* SAIN (AAAI 2023 Oral)：
  * paper：https://arxiv.org/pdf/2304.01064.pdf
  * code：https://github.com/AbnerVictor/HyperThumbnail
  * 简介：提出了一种新的框架(超缩略图),用于实时6K率失真感知图像缩放。首先通过带有我们提出的量化预测模块的编码器将HR图像嵌入到JPEG LR缩略图中，该模块最小化嵌入LR JPEG缩略图的文件大小，同时最大化HR重建质量。然后，一个高效的频率感知解码器实时从LR中重建高保真度的HR图像。
  * 测试结果：未运行、

* HCD (ICCV 2023)：
  * paper：https://arxiv.org/pdf/2211.10643.pdf
  * code：None
  * 简介：提出了一种协作的降尺度方案 Hierarchical Collaborative Downscaling（HCD），其重点是获得图像的更好的下采样表示，而不是学习模型，该方案优化了 HR 和 LR 图像域的表示，获得了更优的下采样图片。
  * 测试结果：未运行

* MULLER (ICCV 2023)：
  * paper：https://arxiv.org/pdf/2304.02859.pdf
  * code：None
  * 简介：我们提出了一种非常轻量级的多层拉普拉斯缩放器，只需要少量可训练参数，被称为MULLER缩放器。MULLER具有带通特性，即它学会提高某些频率子带中的细节，从而有利于下游识别模型。
  * 测试结果：未运行

#### 1.2 通用超分
* WaveMixSR：
  * paper：https://arxiv.org/pdf/2307.00430v1.pdf
  * code：https://github.com/pranavphoenix/WaveMixSR
  * 简介：提出了一种新的神经网络——WaveMixSR,用于基于WaveMix架构的图像超分辨率，它使用2D离散小波变换进行空间标记混合。与基于Transformer的模型不同，WaveMixSR不会将图像展开为像素/块序列。相反，它利用卷积的内积偏置以及小波变换的无损标记混合性质来实现更高的性能，同时需要较少的资源和训练数据。
