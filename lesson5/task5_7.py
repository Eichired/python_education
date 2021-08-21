"""7. Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая строка должна содержать
данные о фирме: название, форма собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
Подсказка: использовать менеджер контекста."""

import json


def firm_profit():
    with open('file_for_task7.txt', 'r', encoding='utf-8') as file:
        profit = {}
        average_profit = {}
        prof = 0
        i = 0
        for line in file:
            name, firm, earning, damage = line.split()
            total = int(earning) - int(damage)
            if total >= 0:
                i = i + 1
                prof = prof + total
            profit[name] = total
        average_profit['average_profit'] = round(prof / i)

    with open('file_for_task7_output.json', 'w', encoding='utf-8') as json_f:
        print(json.dumps([profit, average_profit]))
        print(json.dumps([profit, average_profit]), file=json_f)


firm_profit()
