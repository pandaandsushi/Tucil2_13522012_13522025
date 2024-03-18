def takeinput():
    while True:
        try:
            num_of_control_points = int(input("Jumlah titik kontrol: "))
            if num_of_control_points<3:
                print("Untuk Bezier Curve titik harus lebih dari 2\n")
            else:
                control_points = []
                i=0
                while i < num_of_control_points:
                    x = float(input("Nilai x ke-" + str(i) + ": " ))
                    y = float(input("Nilai y ke-" + str(i) + ": " ))
                    control_points.append((x,y))
                    i+=1
                

                num_of_iteration = int(input("Masukkan jumlah iterasi: "))
                while num_of_iteration < 2:
                    print("Minimal dilakukan 2 iterasi.\n")
                    num_of_iteration = int(input("Masukkan jumlah iterasi: "))
                return num_of_control_points,control_points,num_of_iteration
        except ValueError:
            print("Masukkan harus berupa angka. Silakan masukkan input kembali.\n")
