from dncfunc import Dncfunc as dn
from BF import BF as bf

while True:
    print("Welcome to Bezier Curve Generator!")
    print("You can choose to draw it with the methods below:")
    print("1. Divide and Conquer (Fast and efficient for large sets of points)")
    print("2. Brute Force (Simple and straightforward)")
    method = input("Choose a number: ")

    while method not in ['1', '2']:
        print("Invalid Number! Please choose 1 or 2.")
        method = input("Choose a number: ")

    method = int(method)

    if method == 1:
        print("You have chosen the Divide and Conquer method.")
        kurva = dn()
        kurva.solvednc()
    else:
        print("You have chosen the Brute Force method.")
        kurva = bf()
        kurva.solvebf()

    repeat = input("Do you want to draw another curve? (yes/no): ").lower()
    if repeat != "yes":
        print("Thank you for using Bezier Curve Generator. Goodbye!")
        break
