# Создать список и заполнить его элементами различных типов данных. Реализовать скрипт проверки типа данных каждого элемента.
# Использовать функцию type() для проверки типа. Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.

list = ["Яблоко", 12, 5.5, True]
lenght = len(list)
for i in range(lenght):
    print(type(list[i]))
