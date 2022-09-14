# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

from random import randint
numbers = []
for i in range(10):
    numbers.append(randint(0, 10))
print('Исходный список', numbers)

print(sum(numbers[1::2]))