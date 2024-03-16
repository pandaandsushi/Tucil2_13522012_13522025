import matplotlib.pyplot as plt
import numpy as np
import functions as fn
import timeit

def formula(num_of_points):
    list = [1]       
    for k in range(max(num_of_points,0)):             
         list.append(list[k]*(num_of_points-k)//(k+1))             
    return list

def inbetween(t,list_of_points):
    const = formula(len(list_of_points)-1)
    Rox = 0
    Roy = 0
    for i in range (len(const),0,-1):
        Rox += const[len(const)-i] * pow((1-t),i-1) * pow(t,(len(const)-i)) * list_of_points[len(const)-i][0]
        Roy += const[len(const)-i] * pow((1-t),i-1) * pow(t,(len(const)-i)) * list_of_points[len(const)-i][1]
    return ((Rox,Roy))

num_of_control_points,control_points,num_of_iteration = fn.takeinput()
start = timeit.default_timer()
# temporary
# num_of_control_points = 5
# control_points = [(-2,-3),(-3,-2),(0,-2),(1,-3),(2,1)]
# num_of_iteration = 20
res = []
t_val = np.linspace(0, 1, num_of_iteration)

for i in range (len(t_val)):
    res.append(inbetween(t_val[i],control_points))


# Draw the curve
plt.figure()
points = res
# Iterate through the points then plot the curve
for i in range(1, len(points)):
    x_values = [points[j][0] for j in range(i+1)]
    y_values = [points[j][1] for j in range(i+1)]
    plt.grid(True)
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Final Bezier Curve')
    plt.plot([p[0] for p in control_points], [p[1] for p in control_points], 'ro-', label='Control Points') 
    plt.plot(x_values, y_values, marker='o', color='blue')
    plt.pause(0.5)  # Pause for a short duration

end = timeit.default_timer()
elapsed_time = end - start

print(str(elapsed_time) + " ms\n")
# Plot final curve
x_values = [point[0] for point in points]
y_values = [point[1] for point in points]
plt.plot(x_values, y_values, marker='o', color='blue')
plt.show()