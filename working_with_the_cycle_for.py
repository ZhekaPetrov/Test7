# Write a program that outputs the words "Python is awesome!" (without quotes) 10 times.

# Напишите программу, которая выводит слова «Python is awesome!» (без кавычек) 10 раз.

for i in range(10):
    print("Python is awesome!")
    
    
# The sentence is given and the number of times it needs to be repeated. Write a program that repeats this sentence the right number of times.

# Дано предложение и количество раз которое его надо повторить. Напишите программу, которая повторяет данное предложение нужное количество раз.

a, b = input(), int(input())
for i in range(b):
    print(a)
    
    
# Write a program that uses exactly three for loops to print the following sequence of characters:

# Напишите программу, которая использует ровно три цикла for для печати следующей последовательности символов:

# AAA
# AAA
# AAA
# AAA
# AAA
# AAA
# BBBB
# BBBB
# BBBB
# BBBB
# BBBB
# E
# TTTTT
# TTTTT
# TTTTT
# TTTTT
# TTTTT
# TTTTT
# TTTTT
# TTTTT
# TTTTT
# G

for i in range(6):
    print("A" * 3)
for i in range(5):
    print("B" * 4)
print("E")
for i in range(9):
    print("T" * 5)
print("G")


# The input to the program is a natural number n. Write a program that prints a star rectangle with dimensions n *19.

# На вход программе подается натуральное число n. Напишите программу, которая печатает звездный прямоугольник размерами n * 19.

n = int(input())
for i in range(n):
    print("*" * 19)
    
    
# Write a program that reads one line of text and outputs 10 lines numbered from 0 to 9, each with a specified line of text.

# Напишите программу, которая считывает одну строку текста и выводит 10 строк, пронумерованных от 0 до 9, каждая с указанной строкой текста.

a = input()
for i in range(10):
    print(i, a)
    
    
# The input to the program is a natural number nn. Write a program that for each of the numbers from 00 to nn (inclusive) outputs the phrase: "The square of the 
# number [number] is equal to [number]" (without quotes).

# На вход программе подается натуральное число nn. Напишите программу, которая для каждого из чисел от 00 до nn (включительно) выводит фразу: «Квадрат числа
# [число] равен [число]» (без кавычек).

n = int(input())
for i in range(n + 1):
    print("Квадрат числа", i, "равен", i ** 2)
    
    
# The input to the program is a natural number n (n >= 2) – the cathet of a rectangular isosceles triangle. Write a program that outputs
# the star triangle according to the example.

# На вход программе подается натуральное число n (n >= 2) – катет прямоугольного равнобедренного треугольника. Напишите программу, которая выводит
# звездный треугольник в соответствии с примером.

n = int(input())
for i in range(n):
    print((n - i) * "*")
    
    
# The program is fed three natural numbers m, \, p, \, nm,p,n:
# m: the starting number of organisms;
# p: average daily increase in %;
# n: number of days for breeding.
# Write a program that predicts the size of a population of organisms. The program should output the population size on each day, starting from 11 and ending with
# nn-th day.

# На вход программе подается три натуральных числа m, \, p, \, nm,p,n:
# m: стартовое количество организмов;
# p: среднесуточное увеличение в %;
# n: количество дней для размножения.
# Напишите программу, которая предсказывает размер популяции организмов. Программа должна выводить размер популяции в каждый день, начиная с 11 и заканчивая
# nn-м днем.

m, p, n = int(input()), int(input()), int(input())
for i in range(n):
    print((i + 1), float((m * (p / 100 + 1) ** i)))

# m * (p / 100 + 1) ** i
# m - стартовое количество организмов
# p -  среднесуточное увеличение в %
# i - переменная цикла
