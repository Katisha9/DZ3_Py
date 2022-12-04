# Задача 1. Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов
# списка с нечетными индексами.
# Пример: [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

from random import randint as rand

size = int(input('Введите длину списка: '))
list = []

for i in range(size):
    list.append(rand(0, 100))
print(list)

summNechet = 0
naNechetPoz = []

for i in range(1, size, 2):
    naNechetPoz.append(list[i])
    summNechet += list[i]

print(f'На нечетных позициях элементы:')
print(*naNechetPoz, sep=', ')
print(f'ответ: {summNechet}')

