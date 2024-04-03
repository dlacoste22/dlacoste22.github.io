# -*- coding: utf-8 -*-
"""
Created on Tue Jun 24 15:02:38 2014

@author: viot
"""

import numpy as np
import matplotlib.pylab as plt


def exact(x):
    return 1/np.sqrt(2*np.pi)*np.exp(-x*x/2)
    
npoints=30000   
nbins=100
fig=plt.figure()
eta1 = np.random.random_sample((npoints,1))
eta2 = np.random.random_sample((npoints,1))
histo=np.zeros(nbins)

b=-5+(np.arange(nbins)+0.5)/10.0
x=np.sqrt(-2.0*np.log(eta1))*np.cos(np.pi*eta2)
plt.axes(xlim=(-5, 5), ylim=(0, 0.45),xlabel='x',ylabel='P(x)')
plt.plot(b,exact(b))
 

for i in np.arange(npoints):
       histo[np.int(50+10*x[i])]+=1
       if (i %1000 ==0 and i!=0):
           plt.plot(b,histo/(i/10.0),'o')
           plt.plot(b,exact(b))
           plt.xlabel('x')
	   plt.ylabel('P(x)')
	   plt.xlim(-5,5)
	   plt.ylim(0,0.45)
#           plt.show()
           plt.pause(1)
           plt.clf()
         
plt.show()