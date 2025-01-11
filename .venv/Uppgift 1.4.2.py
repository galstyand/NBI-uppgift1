import math

side1 = int(input("Ange längd för sida 1: "))
side2 = int(input("Ange längd för sida 2: "))
side3 = math.sqrt(side1*side1 + side2*side2)
print("Sida 3 har längd: " + str(side3))