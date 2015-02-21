# -*- coding: utf-8 -*-
from matplotlib.colors import hsv_to_rgb
import matplotlib.cm as cm
import numpy as np


#
# Example HSV Colouring

# computes the hue corresponding to the complex number z
def hue(z):
    H = np.angle(z)/(2*np.pi)+1
    return np.mod(H,1)
    
# Array the same size of the saturation value
def fixedSaturation(s):
    return lambda(z): s * np.ones_like(z, float)
    
# Value is set by mapping 
def logValue(z, n, fix_unit=False, whitening=.2):
    
    modulus = np.absolute(z)
    
    # logm = logn(modulus) 
    Logm = np.log(modulus) / np.log(n)
    Logm = np.nan_to_num(Logm) # If infinte takes the max/min possible values
   
    # Set V is now between 1 and 0 occuring over logarithmic intervals
    V = Logm-np.floor(Logm) # Shift to zero
        
    # Lock the interior of the unit circle to a single interval
    if fix_unit:
        V[modulus < 1] = modulus[modulus < 1]
        
    # V**w > V for V in [0,1] and 0<w<1 
    # Can avoid too many dark colors
    return V ** whitening



# Creates a function that maps points in C to RGB colours
# dstack stacks the value across the third dimension (as you would expect for colours)
def HSVdomainColouring(H,S,V):
    return lambda(z): hsv_to_rgb(np.dstack( (H(z),S(z),V(z)) ))


# Creates a colourmap using a matplotlib colourmap to the absolute value
def AbsoluteCmColouring(color_map):
    return lambda z: color_map(1/np.absolute(z))[:, ...,0:-1] 

# Creates a colourmap using a matplotlib colourmap to the absolute value
def LogAbsoluteCmColouring(color_map):
    return lambda n: lambda z: color_map(np.log(1/np.absolute(z))/np.log(n) )[:, ...,0:-1] 

# Some useful domain colourings

log2value = lambda z: logValue(z, 2, whitening=.05, fix_unit=True)
hsv1 = HSVdomainColouring(hue, fixedSaturation(.9), log2value)

hsv2 = HSVdomainColouring(hue,fixedSaturation(.9), lambda z: np.ones(z.shape))

rgb1 = AbsoluteCmColouring(cm.Blues)
rgbLog = LogAbsoluteCmColouring(cm.Blues)


def AbsoluteCmRealColouring(color_map):
    return lambda z : color_map(np.real(z))[:, ...,0:-1] 

rgbReal  = AbsoluteCmRealColouring(cm.coolwarm)
