# On the Euclidean plane between two points (x1; y1) and (x2; y2) is defined as follows: p = Root((x1 - x2) ** 2) + ((y1 - y2) ** 2)

# На плоскости евклидово между двумя точками (x1; y1) и (x2; y2) определяется так: p = Корень((x1 - x2) ** 2) + ((y1 - y2) ** 2)

import math
x1, y1, x2, y2 = float(input()), float(input()), float(input()), float(input())
p = (math.sqrt(((x1 - x2) ** 2) + ((y1 - y2) ** 2)))
print(p)


# Write a program that determines the area of a circle and the length of a circle by a given radius R.

# Напишите программу определяющую площадь круга и длину окружности по заданному радиусу R.

from math import pi 
r = float(input())
S = pi * (r ** 2)
C = 2 * pi * r
print(S, C, sep="\n")


# In mathematics , the following average values are distinguished:

# В математике выделяют следующие средние значения:
  
  from math import sqrt
a, b = float(input()), float(input())
x = (a + b) / 2
y = sqrt(a * b)
w = (2 * a * b) / (a + b)
z = sqrt(((a ** 2) + (b ** 2)) / 2)
print(x, y, w, z, sep = "\n")


# Write a program that calculates the value of a trigonometric expression

# Напишите программу, вычисляющую значение тригонометрического выражения

#sin(x) + cos(x) + (tan(x) ** 2)

from math import *
x = float(input())
r = radians(x)
y = sin(r) + cos(r) + (tan(r) ** 2)
print(y)


# Write a program that calculates the value of ⌈x⌉ + ⌊x⌋ for a given real number x.

# Напишите программу, вычисляющую значение ⌈x⌉ + ⌊x⌋ по заданному вещественному числу x.

rom math import ceil, floor
x = float(input())
print(int(ceil(x)) + int(floor(x)))
