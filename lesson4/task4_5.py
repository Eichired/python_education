"""Реализовать формирование списка, используя функцию range() и возможности генератора.
В список должны войти четные числа от 100 до 1000 (включая границы).
Необходимо получить результат вычисления произведения всех элементов списка.
Подсказка: использовать функцию reduce()."""

from functools import reduce

new_list = [x for x in range(100, 1001) if x % 2 == 0]
print(f'Сформированный список: {new_list}')
multipli = reduce(lambda x, y: x * y, new_list)
print(f'Результат умножения: {multipli}')
