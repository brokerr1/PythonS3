# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

from random import randint
numbers = []
for i in range(10):
    numbers.append(randint(0, 10))
print('Исходный список', numbers)

result_list = []
for i in range((len(numbers)+1)//2):
    result_list.append(numbers[i]*numbers[len(numbers)-1-i])
print(result_list)