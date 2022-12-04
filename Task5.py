# Задача 5. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов (Негафибоначчи).
# Пример: для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

fib1 = fib2 = 1
fib_list = [fib1, fib2]
number = int(input('Введите число: '))

for i in range(2, number):
    fib1, fib2 = fib2, fib1 + fib2
    fib_list.append(fib2)

fib1 = fib2 = 1
for i in range(-number-1, 0):
    fib1, fib2 = fib2, fib1 - fib2
    fib_list.insert(0, fib2)

print(fib_list)
