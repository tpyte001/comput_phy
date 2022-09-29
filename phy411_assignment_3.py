import numpy as np

def back_diff(x=4,h=0.01):
    return ((x+h)**2 - x**2)/ h
print(back_diff())

def cent_diff(x=4,h=0.01):
    return ((x+h)**2 - (x-h)**2) / (2 * h) 
print(cent_diff())

def second_finite_deriv(x=4,h=0.01):
    return ((x+h)**2 - 2*(x**2) + (x-h)**2) / (h**2)
print(second_finite_deriv())

def trapezoid(a=-1,b=1,N=100):
    #correct result, prints 1.57 = pi/2
    h = (b-a)/N
    sigma = h * (np.sum(np.array([np.sqrt(1-((a+i*h)**2)) for i in range(1,N)])))
    return h * (0.5 * np.sqrt(1.0 - (a**2.0)) + (0.5 * np.sqrt(1.0 - (b**2.0)))) + sigma
print(trapezoid())

def error_values(x=4):
    delta_input_list = [0.01,0.001,0.0001,0.00001]
    for h in range(3):
        return back_diff(4,delta_input_list[h]) - cent_diff(4,delta_input_list[h]) 
    
print(error_values())