"""2. Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс) этого
проекта — одежда, которая может иметь определенное название. К типам одежды в этом проекте относятся пальто и костюм.
У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и
H, соответственно. Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 +
0.5), для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных. Реализовать общий подсчет расхода
ткани. Проверить на практике полученные на этом уроке знания: реализовать абстрактные классы для основных классов
проекта, проверить на практике работу декоратора @property. """

from abc import ABC, abstractmethod


class Clothes(ABC):
    @abstractmethod
    def expenses(self):
        pass


class Coat(Clothes):
    def __init__(self, size=0):
        self._size = size

    @property
    def expenses(self):
        return round((self._size / 6.5) + 0.5, 2)


class Costume(Clothes):
    def __init__(self, height=0):
        self._height = height

    @property
    def expenses(self):
        return round(2 * self._height + 0.3, 2)

quantity1 = Coat(100)
quantity2 = Costume(100)
print(f'Расходы на пальто: {quantity1.expenses}')
print(f'Расходы на костюм: {quantity2.expenses}')
print(f'Расходы на пальто и костюм: {quantity1.expenses + quantity2.expenses}')