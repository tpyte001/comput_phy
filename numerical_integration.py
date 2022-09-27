# numerical integration
# use the reinmann sums
# say N is 5
# split into N trapezoids
# area of trapezoid = h/2 (A+B)
# so h would be (b-a) / N
# so sum of (b-a)/N
# Integral = sum of area of ith trapezoid
import numpy as np
import math as m

def integral_sin(a="lowerbound",b="upperbound",n,h):
    area = (h / 2) * ((np.sin(a) + np.sin(b))) + h 