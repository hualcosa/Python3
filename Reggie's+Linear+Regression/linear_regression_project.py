# This was a project that i developped during my studies of python in codeCademy.
# The briefing of the project is the following:
#   Reggie is a mad scientist who has been hired by the local fast food joint to build 
#   their newest ball pit in the play area. As such, he is working on researching the bounciness
#   of different balls so as to optimize the pit. He is running an experiment to bounce different 
#   sizes of bouncy balls, and then fitting lines to the data points he records. He has heard of 
#   linear regression, but needs your help to implement a version of linear regression in Python.

def get_y(m, b, x):
  y = m*x + b
  return y

#print(get_y(1, 0, 7) == 7)
#print(get_y(5, 10, 3) == 25)

def calculate_error(m, b, point):
    x_point, y_point = point
    y_line = get_y(m, b, x_point)
    diff = y_line - y_point
    return abs(diff)
#this is a line that looks like y = x, so (3, 3) should lie on it. thus, error should be 0:
print(calculate_error(1, 0, (3, 3)))
#the point (3, 4) should be 1 unit away from the line y = x:
print(calculate_error(1, 0, (3, 4)))
#the point (3, 3) should be 1 unit away from the line y = x - 1:
print(calculate_error(1, -1, (3, 3)))
#the point (3, 3) should be 5 units away from the line y = -x + 1:
print(calculate_error(-1, 1, (3, 3)))

datapoints = [(1, 2), (2, 0), (3, 4), (4, 4), (5, 3)]

#Write your calculate_all_error function here
def calculate_all_error(m, b, points):
    total_error = 0
    for point in points:
        point_error = calculate_error(m, b, point)
        total_error += point_error
    return total_error

#every point in this dataset lies upon y=x, so the total error should be zero:
datapoints = [(1, 1), (3, 3), (5, 5), (-1, -1)]
print(calculate_all_error(1, 0, datapoints))

#every point in this dataset is 1 unit away from y = x + 1, so the total error should be 4:
datapoints = [(1, 1), (3, 3), (5, 5), (-1, -1)]
print(calculate_all_error(1, 1, datapoints))

#every point in this dataset is 1 unit away from y = x - 1, so the total error should be 4:
datapoints = [(1, 1), (3, 3), (5, 5), (-1, -1)]
print(calculate_all_error(1, -1, datapoints))


#the points in this dataset are 1, 5, 9, and 3 units away from y = -x + 1, respectively, so total error should be
# 1 + 5 + 9 + 3 = 18
datapoints = [(1, 1), (3, 3), (5, 5), (-1, -1)]
print(calculate_all_error(-1, 1, datapoints))


# The way Reggie wants to find a line of best fit is by trial and error. He wants to try a bunch of different slopes
# (m values) and a bunch of different intercepts (b values) and see which one produces the smallest error value for his dataset.
# Using a list comprehension, let's create a list of possible m values to try. Make the list possible_ms that goes from -10 to 10 inclusive, in increments of 0.1.
possible_ms = [value * 0.1 for value in range(-100,101)]
possible_bs = [value * 0.1 for value in range(-200, 201)]

datapoints = [(1, 2), (2, 0), (3, 4), (4, 4), (5, 3)]
smallest_error = float("inf")
best_m = 0
best_b = 0
for m in possible_ms:
    for b in possible_bs:
        error = calculate_all_error(m, b, datapoints)
        if error < smallest_error:
            best_m, best_b = m, b
            smallest_error = error

print(best_m, best_b, smallest_error)

# What does our model predict?
print(get_y(0.3, 1.7, 6))
#Our model predicts that the 6cm ball will bounce 3.5m.

