"""5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран."""


def meaningless_function():
    with open('file_for_task5.txt', 'w') as file:
        for i in range(1, 21):
            file.write(str(i) + ' ')
    with open('file_for_task5.txt', 'r') as new_f:
        data = new_f.readline()
        print(data)
        data = data.split()
        summ = 0
        for i in data:
            summ += int(i)
        print(summ)


meaningless_function()