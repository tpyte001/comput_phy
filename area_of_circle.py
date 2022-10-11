import random
import numpy as np
points = 5000
points_in_cir = 0
area_square = 4

for i in range(0, points):
    x = random.uniform(-1,1)
    y = random.uniform(-1,1)
    if (x ** 2 + y ** 2)**0.5 < 1:
        points_in_cir = points_in_cir + 1
            
monte_carlo = points_in_cir / points * area_square    
print(points_in_cir," points in the circle.")
print(monte_carlo," is approximate area of circle.")
    