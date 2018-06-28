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
imSrc = plt.imread('guro_svommerpng.png')
imMask = plt.imread('guro_STORmaske.png')

#Regner på de 3 første dimensjonene (RGB),(ikke alfa kanalen)  
imTgt = imTgt[...,0:3]                
imSrc = imSrc[...,0:3]
imMask = imMask[...,0:3]

#Setter maskebildet til bool
#Lager en maske, som er True hvor bildet er svart
imMask = (~(imMask<0.8))

vTarget = imTgt[740:940, 740:1140]
vSource = imSrc[310:510, 440:840 ]
vMaske = imMask[310:510, 440:840 ]
# v2 = im2[310:510, 440:840 ]
#vMaske = im2[maskeSvommer] funker ikke pga dimensjon
#imSrc[maskeSvommer] = 0 #jør alt rundt maska svart
#v2 = im2[maskeSvommer]


# Initialize plotting
plt.ion() ## Interactive on 
imOrginal = plt.imshow(imTgt)
plt.draw()
# Solve diffusion equation
copyTarget=vTarget.copy()

alpha = .25                     # dt / dx**2
ant =0
while True:
    laplaceU = (vTarget[0:-2, 1:-1] +
               vTarget[2:, 1:-1] +
               vTarget[1:-1, 0:-2] +
               vTarget[1:-1, 2:] -
               4 * vTarget[1:-1, 1:-1]) ## - laplace u (g)

    laplaceV = (vSource[0:-2, 1:-1] +
               vSource[2:, 1:-1] +
               vSource[1:-1, 0:-2] +
               vSource[1:-1, 2:] -
               4 * vSource[1:-1, 1:-1]) ## - laplace v (g)
    
    laplace= laplaceU - laplaceV
    vTarget[1:-1, 1:-1] += alpha * laplace
    vTarget[vMaske] = copyTarget[vMaske]
    vTarget[vTarget < 0] = 0
    vTarget[vTarget > 1] = 1
    ant+=1
    if(ant%100):
        imOrginal.set_array(imTgt)
        plt.draw()
        plt.pause(1e-20)