"""Реализовать два небольших скрипта:
а) итератор, генерирующий целые числа, начиная с указанного,
б) итератор, повторяющий элементы некоторого списка, определенного заранее.

Подсказка: использовать функцию count() и cycle() модуля itertools.
    Обратите внимание, что создаваемый цикл не должен быть бесконечным. Необходимо предусмотреть условие его завершения.

Например, в первом задании выводим целые числа, начиная с 3, а при достижении числа 10 завершаем цикл.
    Во втором также необходимо предусмотреть условие, при котором повторение элементов списка будет прекращено."""

from itertools import cycle

old_list = input("Введите список элементов, разделённых пробелом: ")
old_list = old_list.split(' ')
new_list = []
a = 0
for el in cycle(old_list):
    if a >= (len(old_list)*2):
        break
    new_list.append(el)
    a = a + 1
print(f'Первоначальный список: {old_list}')
print(f'Новый список: {new_list}')
