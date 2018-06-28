# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 12:37:13 2017

@author: Guro, Snorre & Sondre
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy import ndimage          ##Bildebehandling
from scipy import misc
#http://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_photo/py_inpainting/py_inpainting.html

## Laste inn bildene 
imTgt = plt.imread('bolge_landpng.png')

## Gå fra tredimensjonalt (rgb) til 1 (gray)
imTgt = np.sum(imTgt[...,0:4], 2) / 4.

##

# Initialize plotting
plt.ion() ## Interactive on 
imOrginal = plt.imshow(imTgt,  plt.cm.gray)
plt.draw()

a = 2
alpha = .25                     # dt / dx**2
ant =0
laplaceV = (imTgt[0:-2, 1:-1] +
               imTgt[2:, 1:-1] +
               imTgt[1:-1, 0:-2] +
               imTgt[1:-1, 2:] -
               4 * imTgt[1:-1, 1:-1]) ## - laplace v (g)
while True:
    laplaceU = (imTgt[0:-2, 1:-1] +
               imTgt[2:, 1:-1] +
               imTgt[1:-1, 0:-2] +
               imTgt[1:-1, 2:] -
               4 * imTgt[1:-1, 1:-1]) ## - laplace u (g)
    
    # kunstigTid = laplace Target - (laplace Source * a) Clone
    laplace= laplaceU - (laplaceV * a)
    imTgt[1:-1, 1:-1] += alpha * laplace
    imTgt[imTgt < 0] = 0
    imTgt[imTgt > 1] = 1
    ant+=1
    if(ant%5):
        imOrginal.set_array(imTgt)
        plt.draw()
        plt.pause(1e-20)                             1 =  paint, 2 = somlos, 3 = kontrast