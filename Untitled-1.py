import math

a = float(input("10"))
b = float(input("8"))
hypotenuse = math.sqrt(a**2 + b**2)
area= 0.5*a*b
print(f"Гипотенуза: {hypotenuse}")
print(f"Площадь: {area}")




a = int(input("25"))
b = int(input("5"))
целая_часть = a // b 
остаток = a % b
print(f"Целая часть: {целая_часть} остаток: {остаток})