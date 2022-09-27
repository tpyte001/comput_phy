# use taylor series to calculate derivative
#forward difference method
def deriv_sin_fwd(x,h=0.01):
    return(np.sin(x+h) - np.sin(x)) / h

#backwards difference method
def deriv_sin_bck(x,h=0.01):
    return(np.sin(x) - np.sin(x-h)) / h

#central difference method
def deriv_sin(x,h=0.01):
    return(np.sin(x+h)-np.sin(x-h)) / (2 * h)

def taylor_series_sin(x):
    x =