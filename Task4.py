# Задача 4. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Без применения встроенных методов (арифметически)
# Пример:
# 45 -> 101101
# 3 -> 11
# 2 -> 10


binaryNumberСonversion = ''
number = int(input("Введите десятичное число для преобразования в двоичное:\n"))
while number != 0:
    binaryNumberСonversion = str(number % 2) + binaryNumberСonversion
    number //= 2
print(binaryNumberСonversion)
