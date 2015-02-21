# -*- coding: utf-8 -*-
import numpy as np
from matplotlib import cm
import domain_colourings as dc
from plot_apparatus import ComplexPlot
from functions import identity

# Create a modulus mapping function here we use base 2
log2value = lambda z: dc.logValue(z, 10, whitening=.1)

# Define two colourings
hsv1 = dc.HSVdomainColouring(dc.hue,dc.fixedSaturation(.9), log2value)
rgb1 = dc.AbsoluteCmColouring(cm.Blues)

# Create a plotting object defaults to hsv
cPlot = ComplexPlot(hsv1)




