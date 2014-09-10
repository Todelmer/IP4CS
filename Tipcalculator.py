# -*- coding: utf-8 -*-
"""
Spyder Editor
Matthew Georges

Tip Calcuator
"""
print "Welcome to the Tip Calculator"

meal = input ("What is the cost of your meal?")
tip = 0.15
tax = 0.0815

meal = meal + meal * tax

total = meal + meal * tip

tipamount = meal * tip

print "A tip of 15% = " + str (tipamount)

print "Your total is: " + str(total)

from datetime import datetime
now = datetime.now()

print now