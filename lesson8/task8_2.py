"""
Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль.
Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля в
качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с
ошибкой.
"""


class MyException(Exception):

    def my_division(self, a, b):
        try:
            res = round(a / b, 2)
        except ZeroDivisionError:
            print(f"{a} / {b} -> на ноль делить нельзя!\n")
        else:
            print(f"{a} / {b} = {res} \n")


m_e = MyException()

m_e.my_division(10, 2)
m_e.my_division(3, 1)
m_e.my_division(1, 0)
m_e.my_division(-4, 4)
