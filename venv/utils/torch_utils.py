# -*- coding: utf-8 -*-
"""
@Created at 2020/4/22 19:37
@Author: Kurt
@file:torch_utils.py
@Desc:
"""

import torch
import os

# def select_device(gpu_id):
#     # if torch.cuda.is_available() and gpu_id >= 0:
#     if gpu_id >= 0:
#         Config.DEVICE = torch.device('cuda:%d' % (gpu_id))
#     else:
#         Config.DEVICE = torch.device('cpu')