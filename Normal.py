#coding : utf-8
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

class Person():

    def __init__(self):
        self.health = 100
        self.damage = 20
        self.armor = 12

    def _calculate_damage(self, damage, armor):
            return damage // armor

    def attack(self, who_attack, who_defend):
            damage = calculate_damage(who_attack.self.damage), (who_defend.self.armor)
            who_defend.health -= damage

class Player(Person):
    pass


class Enemy(Person):
    pass


player1 = Player()
enemy1 = Enemy()
#Решил хоть как то попытаться выполнить с копированием, но что-то не получилось
def start():
    last_attacker = player1
    while player1.health > 0 and enemy1.health > 0:
        if last_attacker == player1:
            enemy1.attack(enemy1, player1)
            last_attacker = enemy1
        else:
            player1.attack(player1, enemy1)
            last_attacker = player

    if player1.health > 0:
        print('Игрок победил!')
    else:
        print('Враг победил!')

start()