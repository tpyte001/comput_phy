import numpy as np
'''
def back_diff(x=4,h=0.01):
    return ((x+h)**2 - x**2)/ h
print(back_diff())

def cent_diff(x=4,h=0.01):
    return ((x+h)**2 - (x-h)**2) / (2 * h) 
print(cent_diff())

def second_finite_deriv(x=4,h=0.01):
    return ((x+h)**2 - 2*(x**2) + (x-h)**2) / (h**2)
print(second_finite_deriv())

def error_values(x=4):
    delta_input_list = [0.01,0.001,0.0001,0.00001]
    for h in range(4):
        return back_diff(4,delta_input_list[h]) - cent_diff(4,delta_input_list[h]) 
    '''

# Numerical Adaptive Integration Functions for sqrt(1-x^2):

# cent_diff method for calculating the error

a = -1
b = 1
delta = 0.1

def cent_diff(x=4,h=0.01):
    return ((x+h)**2 - (x-h)**2) / (2 * h) 

def error(a,b,N=100):
    #h = 0.01
    #h = (b-a)/N
    epsilon = (1/12) * h**2 * (cent_diff(a) - cent_diff(b))

def trapezoid(a=-1,b=1,N=100):
    #correct result, prints 1.57 = pi/2
    h = (b-a)/N
    sigma = h * (np.sum(np.array([np.sqrt(1-((a+i*h)**2)) for i in range(1,N)])))
    return h * (0.5 * np.sqrt(1.0 - (a**2.0)) + (0.5 * np.sqrt(1.0 - (b**2.0)))) + sigma

print(2 * trapezoid(),"Trapezoid function check")

def integral(a,hnext):
    return (hnext * np.sum(np.array([2 * np.sqrt(1-(a+k*hnext)**2) for k in range(1,Nnext,2)])))
    return (np.sum(np.array([2 * np.sqrt(1-(a+k*hnext)**2)])))

def adap_int(a=-1,b=1,Nprev=100):
    delta = 0.01 #margin of error within 0.01 accuracy
    Iprev = 2 * trapezoid()
    #Nprev = 100
    epsilon = 1
    hprev = (b-a)/Nprev
    #epsilon = 1 / 3 * (Icurr - Iprev)
    while (np.abs(epsilon)) > delta:
        Nnext = 2 * Nprev
        hnext = hprev / 2
        Inext = ((1.0 / 2.0) * Iprev) + (hnext * np.sum(np.array([2 * np.sqrt(1-(a+k*hnext)**2) for k in range(1,Nnext,2)])))
        #Inext = ((1.0 / 2.0) * Iprev) + (hnext * np.sum(np.array([2 * np.sqrt(1-(a+k*hnext)**2) for k in range(1,Nnext,2)])))
        #epsilon = error()
        epsilon = (0.33) * (Inext - Iprev)
        Iprev = Inext
        Nprev = Nnext
        hprev = hnext
        print(Inext)
    return Inext
        #h = np.sum(np.array([(b-a)/Nprev for N in range(1,N)]))
        
  
    # half the trapezoid rule to N-1, (do i need to include N-1 as parameter?) * h_i * the odd summation
    # return 0.5 * trapezoid() + h * (np.sum(np.array([np.sqrt(1-((a+i*h)**2)) for i in range(1,N)])))


print(adap_int())
