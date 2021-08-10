# Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.

def my_func(a, b, c):
    my_list = [a, b, c]
    my_list.sort(reverse=True)
    return my_list[0] + my_list[1]


result = my_func(int(input("Введите первое число: ")),
                 int(input("Введите второе число: ")),
                 int(input("Введите третье число: ")))
print(f"Сумма двух наибольших аргументов составляет {result}")
