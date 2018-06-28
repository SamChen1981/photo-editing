# -*- coding: utf-8 -*-
"""
@author: Guro, Snorre & Sondre
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy import ndimage          ##Bildebehandling

## Laste inn bildene 
bilde = plt.imread('svomme_strek.png')

## Gå fra tredimensjonalt (rgb) til 1 (gray)
bilde = bilde[...,0:3]
# vBilde = bilde[310:510, 440:840 ]
#Lager en maske, som er True hvor bildet er svart
maskeBolge = (bilde<0.01)
#plt.imshow(maskeBolge)
#plt.figure()

# best resultat ved (5, 5)
maskeBolge= ndimage.binary_dilation(maskeBolge, structure=np.ones((5, 5 , 1))).astype(maskeBolge.dtype)

# Initialize plotting
plt.ion()
greybilde = plt.imshow(bilde)
plt.draw()

res=bilde.copy()

# Solve diffusion equation
alpha = .25                     # dt / dx**2
ant = 0
while True:
    laplace = (res[0:-2, 1:-1] +
               res[2:, 1:-1] +
               res[1:-1, 0:-2] +
               res[1:-1, 2:] -
               4 * res[1:-1, 1:-1]) ## - laplace v (g)
   # kunstigTid = laplace +0 
    res[1:-1, 1:-1] += alpha * laplace
    res[~maskeBolge]=bilde[~maskeBolge] 
    ant+=1
    if(ant%100):				# viser bilde etter vær 100 utregning
        greybilde.set_array(res)
        plt.draw()
        plt.pause(1e-20)