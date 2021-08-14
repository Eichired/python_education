"""Представлен список чисел. Определить элементы списка, не имеющие повторений.
Сформировать итоговый массив чисел, соответствующих требованию.
Элементы вывести в порядке их следования в исходном списке.
Для выполнения задания обязательно использовать генератор.
Пример исходного списка: [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11].
Результат: [23, 1, 3, 10, 4, 11]"""

import random

old_list = [random.randint(0, 50) for _ in range(15)]
print(old_list)
new_list = []

for i in range(len(old_list)-1):
    for j in range(i+1, len(old_list)):
        if old_list[i] != old_list[j]:
            j = j + 1
            if j == len(old_list):
                new_list.append(old_list[i])
            else:
                continue
        else:
            break

print(new_list)
