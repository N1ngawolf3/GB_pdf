# Easy
# Задача - 1
# Опишите несколько классов TownCar, SportCar, WorkCar, PoliceCar
# У каждого класса должны быть следующие аттрибуты:
# speed, color, name, is_police - Булево значение.
# А так же несколько методов: go, stop, turn(direction) - которые должны сообщать,
#  о том что машина поехала, остановилась, повернула(куда)

def Easy_first_task():
    class TownCar:
        def __init__(self,speed,color,name,is_polise,role):
            self.speed = speed
            self.color = color
            self.name = name
            self.is_police = is_polise
            self.role = role


        def go(self):
            print(f'{self.name} поехала')

        def stop(self):
            print(f'{self.name} остановилась')

        def turn(self,direction):
            print(f'{self.name} повернула({direction})')

    class SportCar:
        def __init__(self, speed, color, name, is_polise,weight):
            self.speed = speed
            self.color = color
            self.name = name
            self.is_police = is_polise
            self.weight = weight

        def go(self):
            print(f'{self.name} поехала')

        def stop(self):
            print(f'{self.name} остановилась')

        def turn(self, direction):
            print(f'{self.name} повернула({direction})')

    class WorkCar:
        def __init__(self, speed, color, name, is_polise,access):
            self.speed = speed
            self.color = color
            self.name = name
            self.is_police = is_polise
            self.access = access

        def go(self):
            print(f'{self.name} поехала')

        def stop(self):
            print(f'{self.name} остановилась')

        def turn(self, direction):
            print(f'{self.name} повернула({direction})')

    class PoliceCar:
        def __init__(self, speed, color, name, is_polise, on_duty):
            self.speed = speed
            self.color = color
            self.name = name
            self.is_police = is_polise
            self.on_duty = on_duty

        def go(self):
            print(f'{self.name} поехала')

        def stop(self):
            print(f'{self.name} остановилась')

        def turn(self, direction):
            print(f'{self.name} повернула({direction})')


# Задача - 2
# Посмотрите на задачу-1 подумайте как выделить общие признаки классов
# в родительский и остальные просто наследовать от него.

def Easy_second_task():
    class Car:
        def __init__(self, speed, color, name, is_polise):
            self.speed = speed
            self.color = color
            self.name = name
            self.is_police = is_polise

        def go(self):
            print(f'{self.name} поехала')

        def stop(self):
            print(f'{self.name} остановилась')

        def turn(self, direction):
            print(f'{self.name} повернула({direction})')

    class TownCar(Car):
        def __init__(self, speed, color, name, is_polise,role):
            super().__init__(speed,color,name,is_polise)
            self.role = role

        def info(self):
            print(f'{self.name} имеет роль {self.role}')

    class SportCar(Car):
        def __init__(self, speed, color, name, is_polise,weight):
            super().__init__(speed,color,name,is_polise)
            self.weight = weight

        def info(self):
            print(f'{self.name} весит {self.weight}')

    class WorkCar(Car):
        def __init__(self, speed, color, name, is_polise,access):
            super().__init__(speed,color,name,is_polise)
            self.access = access

        def info(self):
            print(f'{self.name} сейчас {'Доступна' if self.access else 'Недоступна'}')

    class PoliceCar(Car):
        def __init__(self, speed, color, name, is_polise,on_duty):
            super().__init__(speed,color,name,is_polise)
            self.on_duty = on_duty


        def info(self):
            print(f'{self.name} сейчас {'на службе' if self.on_duty else 'не на службе'}')


# Normal
# Задача - 1
# Ранее мы с вами уже писали игру, используя словари в качестве
# структур данных для нашего игрока и врага, давайте сделаем новую, но уже с ООП
# Опишите базовый класс Person, подумайте какие общие данные есть и у врага и у игрока
# Не забудьте, что у них есть помимо общих аттрибутов и общие методы.
# Теперь наследуясь от Person создайте 2 класса Player, Enemy.
# У каждой сущности должы быть аттрибуты health, damage, armor
# У каждой сущности должно быть 2 метода, один для подсчета урона, с учетом брони противника,
# второй для атаки противника.
# Функция подсчета урона должна быть инкапсулирована
# Вам надо описать игровой цикл так же через класс.
# Создайте экземпляры классов, проведите бой. Кто будет атаковать первым оставляю на ваше усмотрение.
def Normal_first_task():
    class Person:
        def __init__(self, name, health, armor, damage):
            self.name = name
            self.health = health
            self.armor = armor
            self.damage = damage
            self._lvl = 1

        def _calculate_damage(self, enemy):
            return self.damage / enemy.armor

        def attack(self, enemy):
            enemy.health -= self._calculate_damage(enemy)

    class Player(Person):

        def __init__(self, name, health, armor, damage):
            super().__init__(name, health, armor, damage)
            self._experience = 0
            self._exp_to_next_level = 100

        def _is_next_lvl(self):
            if self._experience >= self._exp_to_next_level:
                self._lvl += 1
                self._exp_to_next_level *= 2

        def battle_won(self, experience_count):
            self._experience += experience_count
            self._is_next_lvl()

    class Enemy(Person):

        def __init__(self, name, health, armor, damage, lvl):
            super().__init__(name, health, armor, damage)
            self._experience_for_won = 50
            self._lvl = lvl

        def get_experience_for_won(self):
            return self._experience_for_won * self._lvl

    class Game:
        def __init__(self, player, enemy):
            self._player = player
            self._enemy = enemy

        def start(self):
            last_attacker = self._player
            while self._player.health > 0 and self._enemy.health > 0:
                if last_attacker == self._player:
                    self._enemy.attack(self._player)
                    last_attacker = self._enemy
                else:
                    self._player.attack(self._enemy)
                    last_attacker = self._player
            if self._player.health > 0:
                print(f'Игрок {self._player.name} победил.')
                self._player.battle_won()
            else:
                print(f'Враг {self._enemy.name} победил.')

    player = Player('Igor', 100, 1.2, 10)
    enemy = Enemy('Vasya', 100, 1.2, 10, 2)

    game = Game(player, enemy)
    game.start()


# Hard
# Задача - 1
# Вам необходимо создать завод по производству мягких игрушек для детей.
# Вам надо продумать структуру классов,
# чтобы у вас был класс, который создает игрушки на основании:
#  Названия, Цвета, Типа (животное, персонаж мультфильма)
# Опишите процедуры создания игрушки в трех методах:
# -- Закупка сырья, пошив, окраска
# Не усложняйте пусть методы просто выводят текст о том, что делают.
# В итоге ваш класс по производству игрушек должен вернуть объект нового класса Игрушка.

def Hard_first_task():
    class Toy:
        def __init__(self,name,color):
            self.name = name
            self.color = color

    class ToyAnimal(Toy):
        def __init__(self,name,color):
            super().__init__(name, color)
            self._toy = 'animal'

    class ToyMult(Toy):
        def __init__(self, name, color):
            super().__init__(name, color)
            self._type = 'Мультфильм'

    class ToyFactory:

        def create_toy(self, name, color, toy_type):
            self._buy_raw_materials()
            self._sewing()
            self._set_color()
            if toy_type == 'Животное':
                return ToyAnimal(name, color)
            else:
                return ToyMult(name, color)

        def _buy_raw_materials(self):
            print('Закупка материалов.')

        def _sewing(self):
            print('Пошивка игрушки.')

        def _set_color(self):
            print('Окраска игрушки.')

    factory = ToyFactory()
    print(factory.create_toy('name','y','Животное'))


if __name__ == '__main__':
    Hard_first_task()