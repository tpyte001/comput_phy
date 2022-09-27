import numpy as np

def fwdDiffSin(x,h=0.01):
    return (np.sin(x+h) - np.sin(x)) / h

def cenDiffSin(x,h=0.01):
    return (np.sin(x+h) - np.sin(x-h)) / (2*h)

x = np.pi/3

print(fwdDiffSin(x))
print(cenDiffSin(x))

error = ((cenDiffSin(x) - fwdDiffSin(x)) / cenDiffSin(x)) * 100
print(error,'Percent') 


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
    
print('Percent Accuracy')
deltah(x)

