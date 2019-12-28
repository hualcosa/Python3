
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 20:16:42 2019

@author: hugo
"""
import matplotlib.pyplot as plt
# rainfall data
rainfall_1 = [153, 156, 147, 149, 151]
rainfall_2 = [159, 156, 160, 161, 148]

# horizontal positions of bars
x_values_1 = [x * 2 for x in range(5)]
x_values_2 = [x + 1 for x in x_values_1]

# height of bars
y_values_1 = [value - 140 for value in rainfall_1]
y_values_2 = [value - 140 for value in rainfall_2]

# pyplot bar graph
plt.bar(x_values_1, y_values_1, 0.8, 0)
plt.bar(x_values_2, y_values_2, 0.8, 0)
plt.show()

# another example
x_values_1 = [2*index for index in range(5)]
# [0.0, 2.0, 4.0, 6.0, 8.0] 
x_values_2 = [2*index + 0.8 for index in range(5)]
# [0.8, 2.8, 4.8, 6.8, 8.8]
x_values_midpoints = [(x1 + x2)/2.0 for (x1, x2) in zip(x_values_1, x_values_2)]