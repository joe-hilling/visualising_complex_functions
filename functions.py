# -*- coding: utf-8 -*-

identity  = lambda(z) : z
add       = lambda(v) : lambda z : z + v
multiply  = lambda(c) : lambda z : c*z
inv       = lambda(z) : 1/z


invfn      = lambda  f  : lambda z : 1/f(z)
dividefn   = lambda h,g: lambda z : h(z) / g(z)
multiplyfn = lambda a,b: lambda z : a(z) * b(z) 
addfn      = lambda a,b: lambda z : a(z) + b(z) 
subtractfn = lambda a,b: lambda z : a(z) - b(z)
