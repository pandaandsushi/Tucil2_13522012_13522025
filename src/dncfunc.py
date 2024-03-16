import matplotlib.pyplot as plt
import functions as fn
import timeit

class Dncfunc():
    def __init__(self):
        self.titik = [] # to save all the curve points (red line)
        self.garisbantu = [] # to save the helping points (yellow line)
        self.garban = 0 # jumlah titik garis bantu

    # Find the midpoint between two points 
    def midpoint(self, p1, p2):
        return[(p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2]

    # Function to delete odd indexed elements in a list
    # List starts from index 0
    def deleteganjil(self, list):
        hapus = []
        for i in range(1, len(list), 2):
            hapus.append(i)
        for i in sorted(hapus, reverse=True):
            del list[i]

    # Function to make the first iteration on bezier curve
    def firstinitiation(self, control_points):
        for i in range(len(control_points)-1):
            self.garisbantu.append(self.midpoint(control_points[i],control_points[i+1])) # mencari titik tengah
            self.garban+=1

        # menyimpan semua titik-titik yang dibutuhkan untuk membangun kurva
        self.titik.append(control_points[0])
        self.titik.append(self.garisbantu[0])
        for j in range(1,len(self.garisbantu)):
            self.titik.append(self.midpoint(self.garisbantu[j-1],self.garisbantu[j]))
            self.titik.append(self.garisbantu[j])
        self.titik.append(control_points[len(control_points)-1])


    # Function to plot Bezier curve
    def plot_bezier_curve(self, titik, num_of_control_points, initial_control_points):
        # mengcopy titik dan menghapus elemen ganjil untuk menyisakan titik kurva saja
        titik2 = titik.copy()
        self.deleteganjil(titik2)

        plt.grid(True)
        plt.plot([p[0] for p in initial_control_points], [p[1] for p in initial_control_points], 'bo-', label='Control Points')
        # garban awal
        awal = num_of_control_points-2
        for i in range(awal):
            plt.plot([self.garisbantu[i][0], self.garisbantu[i+1][0]], [self.garisbantu[i][1], self.garisbantu[i+1][1]], 'yo-', markersize=3)
        # garban setelah iterasi pertama
        for i in range(awal+1,len(self.garisbantu)-1,2):
            plt.plot([self.garisbantu[i][0], self.garisbantu[i+1][0]], [self.garisbantu[i][1], self.garisbantu[i+1][1]], 'yo-', markersize=3)
        # menggambar titik kurva
        for i in range(len(titik2)-1):
            x_values = [titik2[i][0], titik2[i+1][0]]
            y_values = [titik2[i][1], titik2[i+1][1]]
            plt.plot(x_values, y_values, 'r-')

    # method untuk mencari titik-titik yang akan membentuk kurva
    def mencarititik(self, bag1, bag2, mid1, mid2):
        x = 0
        temp1 = []
        temp2 = []

        # mencari titik bantu
        for i in range(len(bag1)-1):
            temp1.append(self.midpoint(bag1[x],bag1[x+1]))
            if(x+1<len(bag2)):
                temp2.append(self.midpoint(bag2[x],bag2[x+1]))
            x+=1

        # mencari titik-titik kurva
        for i in range(len(temp1)-1):
            mid1.append(self.midpoint(temp1[i],temp1[i+1]))
            if(i+1<len(temp2)):
                mid2.append(self.midpoint(temp2[i],temp2[i+1]))

        if len(temp1)%1 == 0:
            mid1.append(self.midpoint(temp1[len(temp1)-1],temp2[0]))

        self.garban = self.garban + len(temp1) + len(temp2)
        # tambah titik bantu tiap bagian ke list garis bantu
        self.garisbantu.extend(temp1)
        self.garisbantu.extend(temp2)

    # method untuk melakukan insert titik kurva di akhir iterasi
    def inserttitik(self, mid1, mid2, length, garban2):
        j=1
        if(len(mid1)<len(mid2)):
            j+=1
        for i in range(len(mid1)):
            if(mid1[i] not in self.titik):
                self.titik.insert(j,mid1[i])
                j+=2
        
        j=1
        for i in range(len(mid2)):
            if(mid2[i] not in self.titik):
                self.titik.insert(j+length,mid2[i])
                j+=2
            elif(self.titik.index(mid2[i])>=j+length):
                j+=1

        j = garban2
        for i in range(1,len(self.titik)+len(self.garisbantu)-j,2):
            self.titik.insert(i,self.garisbantu[garban2])
            garban2+=1

    def solvednc(self):
        # getting the inputs
        num_of_control_points,control_points,num_of_iteration = fn.takeinput()
        start = timeit.default_timer()

        initial_control_points = control_points.copy()  # Make a copy of the original control points
        self.firstinitiation(control_points) # Make the first initiation (1st iteration)

        # Plotting initial control points and intermediate points
        plt.plot([p[0] for p in initial_control_points], [p[1] for p in initial_control_points], 'bo-', label='Control Points') 
        for i in range(num_of_control_points-2):
            plt.plot([self.garisbantu[i][0], self.garisbantu[i+1][0]], [self.garisbantu[i][1], self.garisbantu[i+1][1]], 'yo-', markersize=3)
        
        # melakukan plot hasil kurva
        self.plot_bezier_curve(self.titik, num_of_control_points, initial_control_points)
        plt.pause(0.5) 
        plt.clf()

        # Make Bezier curve for each iteration
        for i in range(num_of_iteration-1):
            # Plotting Bezier curve for each iteration
            self.plot_bezier_curve(self.titik,num_of_control_points,initial_control_points)
            plt.xlabel('X')
            plt.ylabel('Y')
            plt.title('Iterasi Titik-titik')
            plt.legend()
            plt.pause(0.5) 
            plt.clf()  # Clear plot for the next iteration

            # DEVIDE AND CONQUER !!
            # membagi kurva menjadi dua bagian
            length = len(self.titik)//2
            bag1= self.titik[:length+1]
            bag2= self.titik[length:]
            garban2 = self.garban
            # mencatat titik tengah di tiap bagian
            mid1 = []
            mid2 = []

            self.mencarititik(bag1,bag2,mid1,mid2)
            self.deleteganjil(self.titik) # menghapus elemen ganjil dari list -> akan di rewrite dengan titik baru
            self.inserttitik(mid1,mid2,length,garban2)

        end = timeit.default_timer()
        elapsed_time = end - start - 0.5*(num_of_iteration-1) # dikurangi waktu pause buat show plot
        print("\n" + str(elapsed_time) + " ms\n")
        # Final Bezier curve
        self.plot_bezier_curve(self.titik,num_of_control_points,initial_control_points)
        plt.text(0.9, -0.1, f"Elapsed Time: {elapsed_time:.2f} ms", fontsize=10, ha='center', transform=plt.gca().transAxes)
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.title('Final Bezier Curve')
        plt.grid(True)
        plt.show()