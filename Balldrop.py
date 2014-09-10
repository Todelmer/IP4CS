# -*- coding: utf-8 -*-
"""
Created on Thu Sep  4 09:22:58 2014

@author: matthewgeorges

This program calculates the tim it takes for a ball to fall from a given hight.
"""
def balldrop(h):
    h = input( "Enter the hight of the ball in meters")

    a = 9.8
    t = ((2 * h)/a)**.5
    return balldrop

print "The ball hits the ground after " + str(t) + " seconds"
