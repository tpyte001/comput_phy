import numpy as np


x = np.pi/3

#forward difference of sin(x)
def fwdDiffSin(x,h=0.01):
    return (np.sin(x+h) - np.sin(x)) / h

#Central difference of sin(x)
def cenDiffSin(x,h=0.01):
    return (np.sin(x+h) - np.sin(x-h)) / (2*h)

#test
print(fwdDiffSin(x))
print(cenDiffSin(x))

#Percent error of central difference to forward difference
error = ((cenDiffSin(x) - fwdDiffSin(x)) / cenDiffSin(x)) * 100
print(error,'Percent') 

#Error comparison for different values of h, increasing
def deltah(x):
    errorOne = ((cenDiffSin(x,0.00001) - fwdDiffSin(x,0.00001)) / cenDiffSin(x,0.00001)) * 100
    errorTwo = ((cenDiffSin(x,0.0001) - fwdDiffSin(x,0.0001)) / cenDiffSin(x,0.0001)) * 100
    errorThree = ((cenDiffSin(x,0.001) - fwdDiffSin(x,0.001)) / cenDiffSin(x,0.001)) * 100
    errorFour = ((cenDiffSin(x,0.01) - fwdDiffSin(x,0.01)) / cenDiffSin(x,0.01)) * 100
    errorFive = ((cenDiffSin(x,0.1) - fwdDiffSin(x,0.1)) / cenDiffSin(x,0.1)) * 100
    print(errorOne)
    print(errorTwo)
    print(errorThree)
    print(errorFour)
    print(errorFive)
    #format these for 4 decimal places
    #make into a graph
print('Percent Accuracy')
deltah(x)

#finite difference for second derivative
def second_derivative_sin(x):
    return (sin(x+h)-2*sin(x)+sin(x-h)) / (2*h)
    

