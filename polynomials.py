# -*- coding: utf-8 -*-

"""
    POLYNOMIALS
    The Factor Theorem says that if a polynomial p(x) has root r, then x−r divides p(x).
    
    Fundamental theorem says that degree n polynomials have n roots. This allows
    us to equare the polynomial and root views. I.e, a collection of points and 
    a function defined on all the space. Polynomials functions are equivalent 
    to defining set of points (the roots). However finding the roots from a 
    polynomial requires (in general) iteratively searching them out. But if we
    have roots we can easily get to the function.
"""

class Polynomial:
    
    def __init__(self, roots):
        
        # Creates tuple of singe functions (z-root_i) 
        self.roots = map(lambda root: lambda z: (z-root), roots)        
        
        # Evaluates the roots each separately
        self.evaluateMonoids = lambda z : map(lambda root: (z-root) , roots)
    
        # Evaluate whole function value
        self.function = lambda z : reduce(lambda a,b: a*b , self.evaluateMonoids(z))

