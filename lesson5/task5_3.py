"""3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов (не менее 10 строк).
Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.
Пример файла:
Иванов 23543.12
Петров 13749.32"""


def salary_count():
    with open('file_for_task3.txt', 'r') as f:
        sal = ''.join(f.readlines()).split("\n")
        sal_list = []
        summ = 0
        print("Менее 20 000 получают следующие люди: ")
        for i in range(len(sal)):
            sal_list.append(sal[i].split(" "))
        for el in sal_list:
            summ += float(el[1])
            if float(el[1]) < 20000:
                print(el[0])



        print(f"Средняя ЗП равна: {summ / len(sal): .2f}")


salary_count()
