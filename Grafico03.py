'''
Created on 14 dic 2017

@author: mpasteri
linspace(start, stop, num=50, endpoint=True, retstep=False, dtype=None)[source]
start : scalar
    The starting value of the sequence.
stop : scalar
    The end value of the sequence, unless endpoint is set to False. In that case, the sequence consists of all but the last of num + 1 evenly spaced samples, so that stop is excluded. Note that the step size changes when endpoint is False.
num : int, optional
    Number of samples to generate. Default is 50. Must be non-negative.

Su NumPy 
http://www.physics.nyu.edu/pine/pymanual/html/chap3/chap3_arrays.html


'''

import pylab  as myplt
import numpy


x = numpy.linspace(0,15,100)
a1 = 0.5
y1 = a1*x

a2 =1.0
y2 = a2*x

a3 = 1.5
y3 = a3*x

print('x, y')

for ind in range(0,100):
    print(x[ind],y1[ind])    
    
#myplt.axis([0, 100, 0, 100])
myplt.plot(x,y1)
myplt.plot(x,y2)
myplt.plot(x,y3)
myplt.grid(True)
myplt.show()










