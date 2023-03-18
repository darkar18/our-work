# InterfaceGAN++: Exploring the limits of InterfaceGAN

> Authors: [Apavou Clément](https://github.com/clementapa) & [Belkada Younes](https://github.com/younesbelkada)

![Python 3.8](https://img.shields.io/badge/python-3.8-green.svg?style=plastic)
![pytorch 1.10.2](https://img.shields.io/badge/pytorch-1.10.2-green.svg?style=plastic)
![sklearn 0.21.2](https://img.shields.io/badge/sklearn-0.21.2-green.svg?style=plastic)

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/darkar18/style-interface/blob/master/InterFaceGAN%2B%2B.ipynb)

<p float="left">
  <img src="images/bald2.gif" width="200" />
  <img src="images/blond.gif" width="200" /> 
  <img src="images/makeup.gif" width="200" /> 
  <img src="images/gray_hair.gif" width="200" /> 
</p>

> From left to right - Images generated using styleGAN and the boundaries *Bald*, *Blond*, *Heavy_Makeup*, *Gray_Hair*

This the the repository to a project related to the [*Introduction to Numerical Imaging*](https://delon.wp.imt.fr/enseignement/mva-introduction-a-limagerie-numerique/) (*i.e, Introduction à l'Imagerie Numérique* in French), given by the MVA Masters program at ENS-Paris Saclay. The project and repository is based on the work from [Shen et al.](https://github.com/younesbelkada/interfacegan/blob/master/README_old.md), and fully supports their codebase. You can refer to the [original README](https://github.com/younesbelkada/interfacegan/blob/master/README_old.md)) to reproduce their results.

- [Introduction](#introduction)
- [:fire: Additional features](#-fire--additional-features)
- [:hammer: Training an attribute detection classifier](#-hammer--training-an-attribute-detection-classifier)
  * [:movie_camera: Get the pretrained StyleGAN2](#-movie-camera--get-the-pretrained-stylegan2)
  <!-- * [:movie_camera: Get the pretrained StyleGAN3](#-movie-camera--get-the-pretrained-stylegan3) -->
  * [:art: Run the generation script](#-art--run-the-generation-script)
- [:pencil2: Edit generated images](#-pencil2--edit-generated-images)
  * [Examples](#examples)
    + [StyleGAN2](#stylegan2)

## Introduction

> In this repository, we propose an approach, termed as InterFaceGAN++, for semantic face editing based on the work from Shen et al. Specifically, we leverage the ideas from the previous work, by applying the method for new face attributes, and also for StyleGAN3. We qualitatively explain that moving the latent vector toward the trained boundaries leads in many cases to keeping the semantic information of the generated images (by preserving its local structure) and modify the desired attribute, thus helps to demonstrate the disentangled property of the styleGANs. 

## :fire: Additional features
+ New attributes (Bald, Gray hair, Blond hair, Earings, ...) for: Stylegan2

The list of new features can be found on our [attributes detection classifier repository](https://github.com/clementapa/CelebFaces_Attributes_Classification/blob/main/utils/constant.py)

## :hammer: Training an attribute detection classifier

We use a ViT-base model to train an attribute detection classifier, please refer to our [classification code](https://github.com/clementapa/CelebFaces_Attributes_Classification) if you want to test it for new models. Once you retrieve the trained SVM from this repo, you can directly move them in this repo and use them.

## :star: Generate images using StyleGAN2

We did not changed anything to the structure of the old repository, please refer to the [previous README](https://github.com/younesbelkada/interfacegan/blob/master/README_old.md). For StyleGAN


## :movie_camera: Get the pretrained StyleGAN2

We use the styleGAN2 trained on ffhq for our experiments, if you want to reproduce them, run:
```
wget -P models/pretrain https://api.ngc.nvidia.com/v2/models/nvidia/research/stylegan2/versions/1/files/stylegan2-ffhq-1024x1024.pkl 
```

## :art: Run the generation script

If you want to generate 10 images using styleGAN2 downloaded before, run:
```
python generate_data.py -m stylegan2_ffhq -o output_stylegan1 -n 10
```

## :pencil2: Edit generated images

You can edit the generated images using our trained boundaries! Depending on the generator you want to use, make sure that you have downloaded the right model and put them into ``` models/pretrain ```. 

#### StyleGAN2

Example of generated images using StyleGAN2 and moving the images towards the opposite direction of the attribute **young**:

<p float="center">
  <img src="images/sg2.jpeg" alt="original images generated with StyleGAN2"/>
</p>
<p float="center">
  <img src="images/sg2_not_young.jpeg" alt="non young version of the images generated with StyleGAN2"/>
</p>

## Citation

```bibtex
@inproceedings{shen2020interpreting,
  title     = {Interpreting the Latent Space of GANs for Semantic Face Editing},
  author    = {Shen, Yujun and Gu, Jinjin and Tang, Xiaoou and Zhou, Bolei},
  booktitle = {CVPR},
  year      = {2020}
}
```

```bibtex
@article{shen2020interfacegan,
  title   = {InterFaceGAN: Interpreting the Disentangled Face Representation Learned by GANs},
  author  = {Shen, Yujun and Yang, Ceyuan and Tang, Xiaoou and Zhou, Bolei},
  journal = {TPAMI},
  year    = {2020}
}
```
