# 3. Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.

month_year = {1: "Зима", 2: "Весна", 3: "Лето", 4: "Осень"}
number = int(input("Введите номер месяца в виде целого числа от 1 до 12: "))
if number in (12, 1, 2):
    print(month_year.get(1))
elif number in range(3, 6):
    print(month_year.get(2))
elif number in range(6, 9):
    print(month_year.get(3))
elif number in range(9, 12):
    print(month_year.get(4))
else:
    print("Введённое число некорректно")
