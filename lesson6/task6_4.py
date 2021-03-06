"""4.Реализуйте базовый класс Car.
У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод
show_speed, который должен показывать текущую скорость автомобиля. Для классов TownCar и
WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно
выводиться сообщение о превышении скорости."""


class Car:
    def __init__(self, name, speed, color, is_police=False):
        self.name = name
        self.speed = speed
        self.color = color
        self.is_police = is_police

    def go(self):
        return f'The {self.name} went.'

    def stop(self):
        return f'\nThe {self.name} has stopped.'

    def turn(self, direction):
        return f'\nThe {self.name} turned {direction}'

    def show_speed(self):
        return f'\nYour speed is {self.speed}'


class TownCar(Car):

    def show_speed(self):
        if self.speed > 60:
            return f'\nYour speed is higher than allow! Your speed is {self.speed}'
        else:
            return f'Speed of {self.name} is normal'


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            return f'\nYour speed is higher than allow! Your speed is {self.speed}'
        else:
            return f'Speed of {self.name} is normal'


class PoliceCar(Car):
    pass


town = TownCar('Mazda', 60, 'blue', False)
print('1:\n' + town.go(), town.show_speed(), town.turn('right'), town.turn('right'), town.stop())

sport = SportCar('Porsche', 170, 'red', False)
print('2:\n' + sport.go(), sport.show_speed(), sport.turn('left'), sport.stop())

work = WorkCar('KIA', 50, 'black', False)
print('3:\n' + work.go(), work.show_speed(), work.turn('left'), work.stop())

police = PoliceCar('BMW', 100, 'white', True)
print('4:\n' + police.go(), police.show_speed(), police.turn('right'), police.stop())
