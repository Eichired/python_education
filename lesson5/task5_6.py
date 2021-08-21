"""6. Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие
лекционных, практических и лабораторных занятий по этому предмету и их количество.
Важно, чтобы для каждого предмета не обязательно были все типы занятий.
Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести словарь на экран.
Примеры строк файла: Информатика: 100(л) 50(пр) 20(лаб).
Физика: 30(л) — 10(лаб)
Физкультура: — 30(пр) —
Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
x = less_list[::4]
hours = less_list[1::4]
"""

def meaningless_function():
    d = {}
    with open("file_for_task6.txt", encoding='utf-8') as fobj:
        for line in fobj:
            name, stats = line.split(':')
            summ = sum(map(int, ''.join([i for i in stats if i == ' ' or (i.isdigit())]).split()))
            d[name] = summ
        print(f"{d}")

meaningless_function()