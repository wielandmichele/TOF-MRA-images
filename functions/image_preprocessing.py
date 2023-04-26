# -*- coding: utf-8 -*-
"""
Created on Fri May 14 15:35:10 2021

@author: Schule
"""
import numpy as np

def normalize(img):
    lmin = float(img.min())
    lmax = float(img.max())
    return np.floor((img - lmin)/(lmax - lmin)*255)

def z_normalize(array):
    array_z = (array - array.mean()) / array.std()
    return (array_z)



