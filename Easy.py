# coding : utf-8

# Задача - 1
# Опишите несколько классов TownCar, SportCar, WorkCar, PoliceCar
# У каждого класса должны быть следующие аттрибуты:
# speed, color, name, is_police - Булево значение.
# А так же несколько методов: go, stop, turn(direction) - которые должны сообщать,
#  о том что машина поехала, остановилась, повернула(куда)

class Cars:

    def __init__(self, speed, color, name):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = False


    def go(self):
        print(self.color, self.name, 'is going')

    def stop(self):
        print(self.color, self.name, 'stopped')

    def turn(self, direction):
        if direction == 'Right':
            print(self.color, self.name, 'turned right')
        elif direction == 'Left':
            print(self.color, self.name, 'turned left')
        else:
            print('Direction unavailable')


class TownCar(Cars):
    pass

class SportCar(Cars):
    pass

class WorkCar(Cars):
    pass

class PoliceCar(Cars):
    def __init__(self,  speed, color, name):
        super().__init__(speed, color, name)
        self.is_police = True


town_car = TownCar('120', 'red', 'BMW')
policec = PoliceCar('140', 'green', 'Toyota')
workc = WorkCar('90', 'grey', 'Honda')
sportc = SportCar('210', 'blue', 'Audi')

town_car.go()
workc.stop()
sportc.turn(direction='Right')
#Почему то программа не хочет возвращать булево значение is_police
policec.is_police()

# Задача - 2
# Посмотрите на задачу-1 подумайте как выделить общие признаки классов
# в родительский и остальные просто наследовать от него.