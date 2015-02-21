import numpy as np
import matplotlib.pyplot as plt

# Evaluates the complex function at the nodes of the grid
# re and im are pairs, re=(a,b) and im=(c,d), defining the rectangular region
# N is the number of nodes per unit interval 
def applyFunctionOverGrid(f, re, im,  N): 
   
    # Dimensions of the area
    l=re[1]-re[0]
    h=im[1]-im[0]
    
    # Points of the grid
    x = np.linspace(re[0], re[1], N*l) # N*l = resolution
    y = np.linspace(im[0], im[1], N*h)
    
    # Complex grid
    x , y = np.meshgrid(x,y)
    zdomain = x + 1j*y
    
    # Return the function evaluated over the grid
    return f(zdomain) 

# Clas object to handle simple plotting of complex functions
class ComplexPlot:
    
    # Ranges
    re = [-1,1]
    im = [-1,1]    
    
    # number of points in a unit
    pointDensity = 100
    
    def __init__(self, domain_colouring):
        self.domainColouring = domain_colouring

    # Convenience method for square ranges centered on the origin
    def view(self, w):
        self.re = [-w,w]
        self.im = [-w,w]

    # Function to render the image
    def plot(self, f, title, axisOn=True, domain_colouring=None, view=None):
        
        # Use values stored on the object unless specified        
        if view:
            re = [-view,view]
            im = [-view,view]
        else:
            re = self.re
            im = self.im
        
        # Get the function output        
        w = applyFunctionOverGrid(f, re, im, self.pointDensity)
    
        # Use default or specified colouring
        if (domain_colouring):
            domc = domain_colouring(w)
        else:
            domc = self.domainColouring(w)
        
        # Axis labels
        plt.xlabel("$\Re(z)$")
        plt.ylabel("$\Im(z)$")
        plt.title(title)
    
        # Show the plot (when axis off do not need to specify the extent)
        if(axisOn):
            plt.imshow(domc, origin="lower", extent=[re[0], re[1], im[0], im[1]])
        else:
            plt.imshow(domc, origin="lower")
            plt.axis('off')
        
    def multiplot(self, plots, (r,c) , firstAxisOnly=False):

        # Adjust plot parameters to fir the number of plots
        plt.rcParams['figure.figsize'] = 6*r, 4*c    
    
        plotno = 1 # Counter
        
        for p in plots:
            
            function = p['fcn']
            title    = p['title']
            
            # Whether or not to only display the first axis
            if firstAxisOnly:
                axisOn = (plotno==1)
            else:
                axisOn = True

            if 'col' in p:
                domc = p['col']
            else:
                domc = self.domainColouring
            
            plt.subplot(r,c,plotno)

            # If the view is set then use it             
            if 'view' in p:
                self.plot(function, title, axisOn, view=p['view'], domain_colouring=domc)
            else:
                self.plot(function, title, axisOn, domain_colouring=domc)
            
            plotno += 1

        # Reset the plot parameters for single plots
        plt.rcParams['figure.figsize'] = 5, 5

    def plotMultiColorings(self, title, func, colorings):

        # Reset the plot parameters for single plots
        plt.rcParams['figure.figsize'] = 15, 8

        plots = []
        for c in colorings:
            plots.append({'fcn': func, 'col': c, 'title': ''})

        plots[0]['title'] = title

        self.multiplot(plots, (1,len(plots)), firstAxisOnly=True)
        

    def additiveCollisionPlot(self,f,g):

        fcn = lambda ca,cb : lambda z: ca*f(z) + cb*g(z)
        
        n = 9
        plots = []
        for i in range(n):
            
            cb = i*1./(n-1)
            ca = 1 - cb
            
            plots.append({ 'title' : 'inner('+str((ca,cb))+'(f,g))',  'fcn': fcn(ca,cb) })        
    
        self.multiplot(plots , (3,3), firstAxisOnly=True)    
