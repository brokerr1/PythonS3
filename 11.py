#Задайте список. Напишите программу, которая определит, присутствует ли в заданном списке строк некое число.

from random import randint
import itertools

n = 7
    
mylist = ['asfasf', 'asfr', 'kjaetgrhsd', '12', 'qwq', '5']

def find_number(n, lst):
    return str(n) in lst

print(find_number(n, mylist))

# Нахождение числа во вложенном списке

def get_list(raw, col, frst, last):
    return [[randint(frst, last) for j in range(col)] for i in range (raw)]

def find_number(n, mylist):
    return n in list(itertools.chain(*mylist))

raw = 3
col = 3
frst = 1
last = 100
mylist = get_list(raw, col, frst, last)

print(mylist)
n = int(input(('Введите число: ')))
print(find_number(n, mylist))