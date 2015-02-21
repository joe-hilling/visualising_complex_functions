# -*- coding: utf-8 -*-
from domain_colourings import hsv1,rgb1,rgbLog,rgbReal
from plot_apparatus import ComplexPlot
import functions as fn

# Create a plotting object defaults to hsv
cPlot = ComplexPlot(hsv1)
cPlot.pointDensity = 50
cPlot.view(3)

# Domain Colourings
triple = [hsv1, rgb1, rgbLog(10)]  
triple = [hsv1, rgb1, rgbReal]  

rgbComp = lambda z: rgbReal(np.imag(z))

quadruple = [hsv1,rgb1,rgbReal, rgbComp]

# Identity
cPlot.plotMultiColorings('Identity: $f(z) = z$', fn.identity, triple)

# Complex number addition
cPlot.plotMultiColorings('Translation/Addition: $f(z) = z-(1+2i)$', fn.add(1+2j), triple)

# Multiplication
cPlot.plotMultiColorings('Scaling (1) $f(z) = 3z$', fn.multiply(3), triple)

# Multiplication
cPlot.plotMultiColorings('Scaling (2) $f(z) = z*.7$', fn.multiply(.7), triple)

# Complex multiplication
cPlot.plotMultiColorings('Rotation $f(z) = iz$', fn.multiply(1j), triple)

# Complex multiplication
cPlot.plotMultiColorings('Multiplication $f(z) = (3-2i)*z$', fn.multiply((3-2j)), triple)

# Square
cPlot.plotMultiColorings('Square $f(z) = z^2$', lambda z: z*z, triple)

# Square
cPlot.plotMultiColorings('Almost square $f(z) = z(z+1.1+1.1i)$', lambda z: z*(z+1.1+1.1j), triple)

cPlot.plotMultiColorings('Almost square $f(z) = z(z+1.1+1.1i)$', lambda z: z*(z+1.1+1.1j), triple)

cPlot.plotMultiColorings('Three roots', lambda z: z*(z+1.1+1.1j)*(z-1.1+2.1j), quadruple)


# Additive inverse
cPlot.view(10)
cPlot.pointDensity = 50
cPlot.plotMultiColorings('1/(z-1) + 1/(z+1)', lambda z : 1/(z-1) + 1/(z+1), triple)

cPlot.plotMultiColorings('1/(z-1) - 1/(z+1)', lambda z : 1/(z-1) - 1/(z+1), triple)
cPlot.plotMultiColorings('-1/(z-1) + 1/(z+1)', lambda z : -1/(z-1) + 1/(z+1), triple)


cPlot.plotMultiColorings('1/z + 1/z', lambda z : 1/z + 1/z, triple)

# Multiplicative inverse
cPlot.plotMultiColorings(1/)


def AdditiveCollisionPlot(f,g):

    fcn = lambda ca,cb : lambda z: ca*f(z) + cb*g(z)
    
    n = 9
    plots = []
    for i in range(n):
        
        cb = i*1./(n-1)
        ca = 1 - cb
        
        print((ca,cb))
        plots.append({ 'title' : '',  'fcn': fcn(ca,cb) })        

    cPlot.multiplot(plots , (3,3), firstAxisOnly=True)    

    
f = lambda z: z*(z+1.1+1.1j)*(z-1.1+2.1j)
g = lambda z: (z-(2.3-.5j))*(z-2.1-1.4j)*(z+2.1-2.1j)    

# Show a collision
cPlot.view(10)
AdditiveCollisionPlot(f,g)

import numpy as np

f = np.cos
g = lambda z: np.exp(z)
cPlot.view(3)
AdditiveCollisionPlot(f,g)


f = np.cos
g = np.cosh
cPlot.view(10)
cPlot.domainColouring = 
AdditiveCollisionPlot(f,g)




def MultiplicativeCollisionPlot(f,g):
    
    # Fractional plowers lead to problems (thing sqrt and branch cutting)
    fcn = lambda ca,cb : lambda z: f(z)**ca * g(z)**cb
    
    n = 9
    plots = []
    for i in range(n):
        
        cb = i*1./(n-1)
        ca = 1 - cb
        
        print((ca,cb))
        plots.append({ 'title' : '',  'fcn': fcn(ca,cb) })        

    cPlot.multiplot(plots , (3,3), firstAxisOnly=True)    
    
cPlot.view(2)
MultiplicativeCollisionPlot(lambda x: x**2,lambda x: x**2 + x)