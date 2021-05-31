# -*- coding: utf-8 -*-
"""
Created on Mon May 10 09:45:14 2021

@author: Schule
"""

import os
import pandas as pd
import pydicom
import h5py
import numpy as np
from scipy import ndimage


def image_to_array(pat_id, info_file):
    file_list = (info_file.loc[info_file['pat_id'] == pat_id, 'path']).tolist()
    ref_file = pydicom.read_file(file_list[0]) 
    image_dims_3d = (int(ref_file.Rows), int(ref_file.Columns), len(file_list))
    origArray = np.zeros(image_dims_3d, dtype=ref_file.pixel_array.dtype)
    for filename in file_list:
        ds = pydicom.read_file(filename)
        origArray[:, :, file_list.index(filename)] = ds.pixel_array
        
    return origArray

def get_files_in_directory(dir):
    file_list = []

    for paths, dirnames, filenames in os.walk(dir, topdown = True):
        for file in filenames:
                file_list.append(os.path.join(paths,file))
    file_list.sort()
    return file_list

def scale_array_3D(array, dims):
    scaling_factor = [dims[0]/array.shape[0], dims[1]/array.shape[1], dims[2]/array.shape[2]]
    scaledArray = ndimage.zoom(array, scaling_factor)

    print("Scaled image size: {}".format(scaledArray.shape))
    return scaledArray








