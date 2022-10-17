# YOLACT_Retina
A simple, fully convolutional model for real-time instance segmentation in vitreoretinal procedures. 
Paper published with this work:
```
Nespolo, R. G., Yi, D., Cole, E., Warren, A., Wang, D., & Leiderman, Y. I. (2022). 
Feature Tracking and Segmentation in Real Time via Deep Learning in Vitreoretinal Surgery–A platform for AI-Mediated Surgical Guidance. 
Ophthalmology Retina. DOI: https://doi.org/10.1016/j.oret.2022.10.002
```


This is the code for the original papers:
 - [YOLACT: Real-time Instance Segmentation](https://arxiv.org/abs/1904.02689)
 - [YOLACT++: Better Real-time Instance Segmentation](https://arxiv.org/abs/1912.06218)

# Installation
 - Clone this repository and enter it:
   ```Shell
   git clone https://github.com/rgnespolo/YOLACT_Retina_Public.git
   cd yolact
   ```
 - Set up the environment using one of the following methods:
   - Using [Anaconda](https://www.anaconda.com/distribution/)
     - Run `conda env create -f environment.yml`
   - Manually with pip
     - Set up a Python3 environment (e.g., using virtenv).
     - Install [Pytorch](http://pytorch.org/) 1.0.1 (or higher) and TorchVision.
     - Install some other packages:
       ```Shell
       # Cython needs to be installed before pycocotools
       pip install cython
       pip install opencv-python pillow pycocotools matplotlib 
       ```


# Citation
If you use this code base in your work, please cite the original authors of this archtecture:

```
@article{yolact-plus-tpami2020,
  author  = {Daniel Bolya and Chong Zhou and Fanyi Xiao and Yong Jae Lee},
  journal = {IEEE Transactions on Pattern Analysis and Machine Intelligence}, 
  title   = {YOLACT++: Better Real-time Instance Segmentation}, 
  year    = {2020},
}
```
