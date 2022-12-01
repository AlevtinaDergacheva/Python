# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях.
# Позиции хранятся в файле file.txt в одной строке одно число.

n = int(input("Введите число - "))
n = -n
list = []
for i in range(n, abs(n)+1):
    list.append(i)
print(list)

with open('file.txt', 'w') as data:
    data.write('0\n')
    data.write('2\n')
    data.write('4\n')

rez = 1
path = 'file.txt'
data = open(path, 'r')
for line in data:
    print(line)
    rez *= list[int(line)]
data.close()
print ("Произведение указанных элементов = ", rez)