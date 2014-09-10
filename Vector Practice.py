# -*- coding: utf-8 -*-
"""
Created on Tue Sep  9 09:08:07 2014

@author: matthewgeorges
"""

#Messing with vectors!

#Import the necessary array package from numpy
from numpy import array
a = [3,-4,2]
b = [2,1,-1.5]

#I labeled the array as a float, in case this program needs to be adapted to handle decimal numbers
a = array(a,float)
b = array(b,float)

print "Your vectors are:"
print a,b

#The magnitude of a vector is defined as the sum of every element squared
ma = a[0]**2 + a[1]**2 + a[2]**2
mb = b[0]**2 + b[1]**2 + b[2]**2

#The answers are inserted in to strings, for clarity
print "the magnitude of vector a = " + str(ma)
print "the magnitude of vector b = " + str(mb)

#Importing the dot product from numpy
from numpy import dot
print "the dot product of vectors a and b = " + str(dot(a,b))