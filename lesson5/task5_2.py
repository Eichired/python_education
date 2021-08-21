# 2. Создать текстовый файл (не программно),
# сохранить в нем несколько строк, выполнить подсчет количества строк, количества слов в каждой строке.

# Для выполнения кода используется файл, сформированный при решении задачи № 1

def line_word_counter():
    with open('file_for_task1.txt', 'r') as f:
        text = f.readlines()
        print(text)
        print('Количество строк в файле', len(text))
        for i in range(len(text)):
            print(f'Кол-во слов в строке {i+1}: ', len(''.join(text[i]).split(' ')))

line_word_counter()