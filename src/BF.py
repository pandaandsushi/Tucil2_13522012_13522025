import matplotlib.pyplot as plt
import numpy as np
import functions as fn
from matplotlib.widgets import Cursor
import time
# getting the inputs
# num_of_control_points = int(input("Jumlah titik kontrol: "))
# control_points = []
# for i in range (num_of_control_points):
#     x = int(input("Nilai x ke-" + str(i) + ": " ))
#     y = int(input("Nilai y ke-" + str(i) + ": " ))
#     control_points.append((x,y))
# num_of_iteration = int(input("Masukkan jumlah iterasi: "))

start_time = time.time()

# temporary
num_of_control_points = 3
control_points = [(0,0),(-4,2.5),(5,0.5)]
num_of_iteration = 20
res = []
t_val = np.linspace(0, 1, num_of_iteration)

for i in range (len(t_val)):
    print("Titik ke -",i)
    res.append(fn.inbetween(t_val[i],control_points))

end_time = time.time()
elapsed_time = end_time - start_time

print(str(elapsed_time) + " ms\n")

# Draw the curve
plt.figure()
points = res
# Iterate through the points and plot the curve incrementally
for i in range(1, len(points)):
    x_values = [points[j][0] for j in range(i+1)]
    y_values = [points[j][1] for j in range(i+1)]
    plt.grid(True)
    plt.plot(x_values, y_values, marker='o', color='blue')
    plt.pause(0.5)  # Pause for a short duration to see each step

# Plot final curve
x_values = [point[0] for point in points]
y_values = [point[1] for point in points]
plt.plot(x_values, y_values, marker='o', color='blue')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Step-by-step Curve Plot')
plt.show()
# x_values = [point[0] for point in res]
# y_values = [point[1] for point in res]
# for i in range(len(res)):
#     x3 = []
#     y3 = []
#     x3.append(res[i][0])
#     # x3.append(res[i+1][0])

#     y3.append(res[i][1])
#     # y3.append(res[i+1][1])
#     plt.plot(x3, y3, 'yo-')
# plt.xlabel('X')
# plt.ylabel('Y')
# plt.title('Iterasi Titik-titik')
# plt.grid(True)
# plt.show()
    

# # # Plot the curve
# # plt.plot(x_values, y_values)
# # plt.xlabel('X-axis')
# # plt.ylabel('Y-axis')
# # plt.title('Curve from List of Points')
# # x_res, y_res = zip(*res)

# # plt.scatter(x_res, y_res, color='red', label='Control Points')
# # plt.scatter(x_coordinates, y_coordinates, color='blue', label='Input Points')

# # # Show the plot
# # plt.show()
