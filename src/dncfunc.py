import matplotlib.pyplot as plt

titik = []

def midpoint(p1, p2):
    return[(p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2]

def deleteganjil(list):
    hapus = []
    for i in range(1, len(list), 2):
        hapus.append(i)
    for i in sorted(hapus, reverse=True):
        del list[i]

num_of_iteration = int(input("Masukkan jumlah iterasi: "))
num_of_control_points = 3
control_points = [(0,0),(-4,2.5),(5,0.5)]
initial_control_points = control_points.copy()  # Make a copy of the original control points

garban = 0
garisbantu = []
garisbantu.append(midpoint(control_points[0],control_points[1]))
garisbantu.append(midpoint(control_points[1],control_points[2]))
garban+=2

titik.append(control_points[0])
titik.append(garisbantu[0])
titik.append(midpoint(garisbantu[0],garisbantu[1]))
titik.append(garisbantu[1])
titik.append(control_points[2])

# Function to plot Bezier curve
def plot_bezier_curve(titik):
    plt.grid(True)
    plt.plot([p[0] for p in initial_control_points], [p[1] for p in initial_control_points], 'bo-', label='Control Points') 
    for i in range(0,len(garisbantu),2):
        plt.plot([garisbantu[i][0], garisbantu[i+1][0]], [garisbantu[i][1], garisbantu[i+1][1]], 'yo-', markersize=3)
    for i in range(len(titik)-1):
        x_values = [titik[i][0], titik[i+1][0]]
        y_values = [titik[i][1], titik[i+1][1]]
        plt.plot(x_values, y_values, 'r-')

# Plotting initial control points and intermediate points
plt.plot([p[0] for p in initial_control_points], [p[1] for p in initial_control_points], 'bo-', label='Control Points') 
for i in range(0,len(garisbantu),2):
    plt.plot([garisbantu[i][0], garisbantu[i+1][0]], [garisbantu[i][1], garisbantu[i+1][1]], 'yo-', markersize=3)

plt.xlabel('X')
plt.ylabel('Y')
plt.title('Iterasi Titik-titik')
plt.legend()

# Plotting Bezier curve for each iteration
for i in range(num_of_iteration-1):
    plot_bezier_curve(titik)
    plt.pause(1) 
    plt.clf()  # Clear plot for the next iteration

    length = len(titik)//2
    bag1= titik[:length+1]
    bag2= titik[length:]
    
    b1 = 0
    b2 = 0

    garban2 = garban
    mid1 = []
    mid2 = []

    for i in range(len(bag1)//2):
        garisbantu.append(midpoint(bag1[b1],bag1[b1+1]))
        garisbantu.append(midpoint(bag1[b1+1],bag1[b1+2]))
        b1+=2

    for i in range(len(bag1)//2):
        garisbantu.append(midpoint(bag2[b2],bag2[b2+1]))
        garisbantu.append(midpoint(bag2[b2+1],bag2[b2+2]))
        b2+=2

    for i in range(garban,b1+garban,2):
        mid1.append(midpoint(garisbantu[i],garisbantu[i+1]))
        garban+=2
    
    for i in range(garban,len(garisbantu),2):
        mid2.append(midpoint(garisbantu[i],garisbantu[i+1]))
        garban+=2

    deleteganjil(titik)

    j=1
    for i in range(len(mid1)):
        if(mid1[i] not in titik):
            titik.insert(j,mid1[i])
            j+=2
    
    j=1
    for i in range(len(mid1)):
        if(mid2[i] not in titik):
            titik.insert(j+length,mid2[i])
            j+=2

    j = garban2

    for i in range(1,len(titik)+len(garisbantu)-j,2):
        titik.insert(i,garisbantu[garban2])
        garban2+=1

# Final Bezier curve
plot_bezier_curve(titik)
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Final Bezier Curve')
plt.grid(True)
plt.show()
