import matplotlib.pyplot as plt
import functions as fn
import timeit
titik = []
garisbantu = []
# Find the midpoint between two points 
def midpoint(p1, p2):
    return[(p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2]

# Function to delete odd indexed elements in a list
# List starts from index 0
def deleteganjil(list):
    hapus = []
    for i in range(1, len(list), 2):
        hapus.append(i)
    for i in sorted(hapus, reverse=True):
        del list[i]

def firstinitiation(control_points):
    garban = 0
    for i in range(len(control_points)-1):
        garisbantu.append(midpoint(control_points[i],control_points[i+1]))
        garban+=1

    titik.append(control_points[0])
    titik.append(garisbantu[0])
    for j in range(1,len(garisbantu)):
        titik.append(midpoint(garisbantu[j-1],garisbantu[j]))
        titik.append(garisbantu[j])
    titik.append(control_points[len(control_points)-1])

    return garban
    
# getting the inputs
num_of_control_points,control_points,num_of_iteration = fn.takeinput()

# temporary
# num_of_iteration = int(input("Masukkan jumlah iterasi: "))
# num_of_control_points = 10
# control_points = [(0, 0), (1, 1), (2, 3), (4, 1), (5, 2), (6, 1), (7, 2), (8, 3), (9, 1), (10, 0)]
start = timeit.default_timer()
initial_control_points = control_points.copy()  # Make a copy of the original control points
garban = firstinitiation(control_points)

# print(titik)
# print(garban)
# Function to plot Bezier curve
def plot_bezier_curve(titik):
    plt.grid(True)
    plt.plot([p[0] for p in initial_control_points], [p[1] for p in initial_control_points], 'bo-', label='Control Points')
    #garban awal
    awal = num_of_control_points-2
    for i in range(awal):
        plt.plot([garisbantu[i][0], garisbantu[i+1][0]], [garisbantu[i][1], garisbantu[i+1][1]], 'yo-', markersize=3)
    for i in range(awal+1,len(garisbantu),2):
        plt.plot([garisbantu[i][0], garisbantu[i+1][0]], [garisbantu[i][1], garisbantu[i+1][1]], 'yo-', markersize=3)
    for i in range(len(titik)-1):
        x_values = [titik[i][0], titik[i+1][0]]
        y_values = [titik[i][1], titik[i+1][1]]
        plt.plot(x_values, y_values, 'r-')

# # Plotting initial control points and intermediate points
# plt.plot([p[0] for p in initial_control_points], [p[1] for p in initial_control_points], 'bo-', label='Control Points') 
# for i in range(num_of_control_points-2):
#     plt.plot([garisbantu[i][0], garisbantu[i+1][0]], [garisbantu[i][1], garisbantu[i+1][1]], 'yo-', markersize=3)
# titik2 = titik.copy()
# deleteganjil(titik2)
# plot_bezier_curve(titik2)
# plt.pause(0.5) 
# plt.clf()


# Plotting Bezier curve for each iteration
for i in range(num_of_iteration-1):
    titik2 = titik.copy()
    deleteganjil(titik2)
    plot_bezier_curve(titik2)
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Iterasi Titik-titik')
    plt.legend()
    plt.pause(0.5) 
    plt.clf()  # Clear plot for the next iteration

    length = len(titik)//2
    bag1= titik[:length+1]
    bag2= titik[length:]
    
    b1 = 0
    b2 = 0

    garban2 = garban
    mid1 = []
    mid2 = []

    # print(bag1,bag2)

    for i in range(len(bag1)-1):
        garisbantu.append(midpoint(bag1[b1],bag1[b1+1]))
        b1+=1

    for i in range(len(bag1)-1):
        garisbantu.append(midpoint(bag2[b2],bag2[b2+1]))
        b2+=1

    for i in range(garban,b1+garban,2):
        mid1.append(midpoint(garisbantu[i],garisbantu[i+1]))
        garban+=2
    
    for i in range(garban,len(garisbantu),2):
        mid2.append(midpoint(garisbantu[i],garisbantu[i+1]))
        garban+=2

    # print(mid1,mid2)
    deleteganjil(titik)

    j=1
    if(len(mid1)<len(mid2)):
        j+=1
    for i in range(len(mid1)):
        if(mid1[i] not in titik):
            titik.insert(j,mid1[i])
            j+=2
    
    j=1
    if(len(mid2)<len(mid1)):
        j+=1
    for i in range(len(mid2)):
        if(mid2[i] not in titik):
            titik.insert(j+length,mid2[i])
            j+=2

    j = garban2

    for i in range(1,len(titik)+len(garisbantu)-j,2):
        titik.insert(i,garisbantu[garban2])
        garban2+=1
# Final Bezier curve
deleteganjil(titik)
plot_bezier_curve(titik)
end = timeit.default_timer()
elapsed_time = end - start
print(str(elapsed_time) + " ms\n")
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Final Bezier Curve')
plt.grid(True)
plt.show()
