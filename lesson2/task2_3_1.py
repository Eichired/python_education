# 3. Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.

list = ["Зима", "Весна", "Лето", "Осень"]
number = int(input("Введите номер месяца в виде целого числе от 1 до 12: "))
if number in (12, 1, 2):
    print(list[0])
elif number in (3, 4, 5):
    print(list[1])
elif number in (6, 7, 8):
    print(list[2])
elif number in (9, 10, 11):
    print(list[3])
else:
    print("Введённое число некорректно")