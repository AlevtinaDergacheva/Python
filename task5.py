# Реализуйте алгоритм нахождения(генерации) рандомного(случайного) числа.
# (Не используя библиотеки связанные с рандомом)
import datetime

print(datetime.datetime.now().microsecond)
num = datetime.datetime.now().microsecond % 10
print(num)