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

# num_of_control_points = int(input("Jumlah titik kontrol: "))
# control_points = []
# for i in range (num_of_control_points):
#     x = float(input("Nilai x ke-" + str(i) + ": " ))
#     y = float(input("Nilai y ke-" + str(i) + ": " ))
#     control_points.append((x,y))
num_of_iteration = int(input("Masukkan jumlah iterasi: "))

num_of_control_points = 3
control_points = [(0,0),(-4,2.5),(5,0.5)]

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

for i in range(num_of_iteration-1):
    length = len(titik)//2
    bag1= titik[:length+1]
    bag2= titik[length:]
    
    b1 = 0
    b2 = 0

    # nanti dibenrin lah ini masih manual
    garban2 = garban
    mid1 = []
    mid2 = []

    print(bag1,bag2)
    print("first",garisbantu)
    print("")

    for i in range(len(bag1)//2):
        garisbantu.append(midpoint(bag1[b1],bag1[b1+1]))
        garisbantu.append(midpoint(bag1[b1+1],bag1[b1+2]))
        b1+=2

    for i in range(len(bag1)//2):
        garisbantu.append(midpoint(bag2[b2],bag2[b2+1]))
        garisbantu.append(midpoint(bag2[b2+1],bag2[b2+2]))
        b2+=2

    print("second",garisbantu)

    for i in range(garban,b1+garban,2):
        mid1.append(midpoint(garisbantu[i],garisbantu[i+1]))
        print(midpoint(garisbantu[i],garisbantu[i+1]))
        garban+=2
    
    for i in range(garban,len(garisbantu),2):
        mid2.append(midpoint(garisbantu[i],garisbantu[i+1]))
        print(midpoint(garisbantu[i],garisbantu[i+1]))
        garban+=2

    deleteganjil(titik)
    print("mid1",mid1)
    print("mid2",mid2)
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
    # titik.sort(key=lambda p: p[0])
    print(titik)


# Mengambil koordinat x dan y dari semua titik
titik2 = titik
deleteganjil(titik2)
print(titik2)
x = [p[0] for p in titik2]
y = [p[1] for p in titik2]

x2 = [p[0] for p in control_points]
y2 = [p[1] for p in control_points]

# Menampilkan titik-titik dan garis-garis antara titik-titik
plt.plot(x2, y2, 'bo-') 
for i in range(0,len(garisbantu),2):
    x3 = []
    y3 = []
    x3.append(garisbantu[i][0])
    x3.append(garisbantu[i+1][0])

    y3.append(garisbantu[i][1])
    y3.append(garisbantu[i+1][1])
    plt.plot(x3, y3, 'yo-',markersize=3)
plt.plot(x, y, 'ro-')  
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Iterasi Titik-titik')
plt.grid(True)
plt.show()