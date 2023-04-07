#!/usr/bin/env python
# coding: utf-8

# # Setup
# 
# Clone GitHub [repository](https://github.com/ultralytics/yolov5), install [dependencies](https://github.com/ultralytics/yolov5/blob/master/requirements.txt) and check PyTorch and GPU.

# !git clone https://github.com/ultralytics/yolov5  # clone
# %cd yolov5
# %pip install -qr requirements.txt  # install

# In[1]:


import torch
import utils
import time
import os
display = utils.notebook_init()  
print('is torch.cuda available? ',torch.cuda.is_available())# checks
os.environ["GIT_PYTHON_REFRESH"] = "quiet"


# # 1. Detect
# 
# `detect.py` runs YOLOv5 inference on a variety of sources, downloading models automatically from the [latest YOLOv5 release](https://github.com/ultralytics/yolov5/releases), and saving results to `runs/detect`. Example inference sources are:
# 
# ```shell
# python detect.py --source 0  # webcam
#                           img.jpg  # image 
#                           vid.mp4  # video
#                           screen  # screenshot
#                           path/  # directory
#                          'path/*.jpg'  # glob
#                          'https://youtu.be/Zgi9g1ksQHc'  # YouTube
#                          'rtsp://example.com/media.mp4'  # RTSP, RTMP, HTTP stream
# ```
# Here we detect an xray-like video in './video/result1.mp4'<br>The model file used in detection is bestl.pt<br>The video is only one example. Contact me if you want more.

# In[2]:


get_ipython().system('python detect.py --weights bestl.pt --source ./video/result1.mp4')


# # result
# The detection result is in '.runs/detect/exp(n)'
