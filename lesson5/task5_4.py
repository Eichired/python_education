"""4. Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл"""



def line_counter():
    d = {1: 'Один', 2: 'Два', 3: 'Три', 4: 'Четыре'}
    with open('file_for_task4.txt', 'r') as f:
        data = f.readlines()
        x = []
        for el in range(len(data)):
            x.append(data[el].split())
        print(x)
    with open('for_task4_output.txt', 'w') as out:
        for elem in range(len(x)):
            print(x[elem][0].replace(x[elem][0], d[elem+1]), x[elem][1], x[elem][2], file=out)


line_counter()
