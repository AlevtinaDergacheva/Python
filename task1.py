# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# (Сделать для строки)
#
#     *Пример:*
#
#     - 6782 -> 23
#     - 0,56 -> 11

num = input("Введите число - ")
sum = 0
for i in num:
    if i == ".":
        continue
    sum += int(i)
print("Сумма цифр числа = ", sum)