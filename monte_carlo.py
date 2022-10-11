#Monte carlo method, calculate area with random numbers

#look up proof of montecarlo method
#r = 1
#area_circle = np.pi * (r ** 2)
#area_square = 4
#A = circle_points / total_points * area 
#n = random.random(a,b) # the bounds of your square

# generate points for x and y
# choose domain and codomain
def monte_carlo(points=5000):
    import random
    import numpy as np
    #points = 5000
    points_in_cir = 0
    area_square = 4

    for i in range(0, points):
        x = random.uniform(-1,1)
        y = random.uniform(-1,1)
        if (x ** 2 + y ** 2)**0.5 < 1:
            points_in_cir = points_in_cir + 1
            
    monte_carlo = points_in_cir / points * area_square    
    return monte_carlo
    return points_in_cir
    print(points_in_cir," points in the circle.")
    print(monte_carlo," = area of circle.")

print(monte_carlo(5000))