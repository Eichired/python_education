# Пользователь вводит строку из нескольких слов, разделённых пробелами. Вывести каждое слово с новой строки.
# Строки необходимо пронумеровать. Если в слово длинное, выводить только первые 10 букв в слове.

work_string = input("Введите слова через пробел: ")
work_list = work_string.split(' ')
lenght = len(work_list)
for i in range(lenght):
    print(i + 1, work_list[i][:10])
