def midpoint(p1, p2):
    return ((p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2)

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
        Rox += const[len(const)-i] * pow((1-t),i-1) * pow(t,(len(const)-1)) * list_of_points[len(const)-i][0]
        Roy += const[len(const)-i] * pow((1-t),i-1) * pow(t,(len(const)-1)) * list_of_points[len(const)-i][1]
        # print(Rox)
        # print("")
    return ((Rox,Roy))
# points = [(0, 0), (2, 5), (7, 2), (10, 1), (2,2)]
# t = 0.5
# points = [(0,0),(1,2),(3,4)] -> res (1.0, 1.5)
# point = inbetween(t, points)
# print(f"Point on Bézier curve at t = {t}: {point}")