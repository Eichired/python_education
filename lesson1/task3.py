# посчитать сумму, например, 33+3333+333333
num = input("Введите число: ")
num_list = list(num)

x = int(''.join(num_list))
y = int(''.join(num_list*2))
z = int(''.join(num_list*3))

print("Сумма чисел равна:", x+y+z)