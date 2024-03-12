import matplotlib.pyplot as plt
import numpy as np
import functions as fn

# getting the inputs
num_of_control_points = int(input("Jumlah titik kontrol: "))
# control_points = []
# for i in range (num_of_control_points):
#     x = int(input("Nilai x ke-" + str(i) + ": " ))
#     y = int(input("Nilai y ke-" + str(i) + ": " ))
#     control_points.append((x,y))
num_of_iteration = int(input("Masukkan jumlah iterasi: "))

# temporary
control_points = [(1,2),(3,4),(2,2)]

x_coordinates, y_coordinates = zip(*control_points)
plt.scatter(x_coordinates, y_coordinates, color='red', label='Control Points')
plt.title('Control Points')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.legend()
plt.show()