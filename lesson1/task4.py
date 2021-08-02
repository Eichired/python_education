a = int(input("Введите число: "))
b = a % 10
a1 = a
while a1 != 0:
    a1 = a1 // 10
    a2 = a1 % 10
    if a2 > b:
        b = a2
    else:
        continue
print("Максимальное число = ", b)
