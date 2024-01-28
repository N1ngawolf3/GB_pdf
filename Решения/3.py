import os
## 3
#Easy
# Постарайтесь использовать то, что мы прошли на уроке при решении этого ДЗ,
# вспомните про zip(), map(), lambda, посмотрите где лучше с ними, а где они излишни!

# Задание - 1
# Создайте функцию, принимающую на вход Имя, возраст и город проживания человека
# Функция должна возвращать строку вида "Василий, 21 год(а), проживает в городе Москва"

def Easy_first_task(name, age, occupation):
    print(name, age, f'проживает в городе {occupation}', sep=', ')



# Задание - 2
# Создайте функцию, принимающую на вход 3 числа, и возвращающую наибольшее из них
def Easy_second_task(*args):
    print(max(args))


# Задание - 3
# Создайте функцию, принимающую неограниченное количество строковых аргументов,
# верните самую длинную строку из полученных аргументов

def Easy_third_task(*args):
    length = 0
    nstr = ''
    for estr in args:
        if len(estr)>length:
            length = len(estr)
            nstr = estr
    print(nstr)

#Normal
# Задание - 1
# Вам даны 2 списка одинаковой длины, в первом списке имена людей, во втором зарплаты,
# вам необходимо получить на выходе словарь, где ключ - имя, значение - зарплата.
# Запишите результаты в файл salary.txt так, чтобы на каждой строке было 2 столбца,
# столбцы разделяются пробелом, тире, пробелом. в первом имя, во втором зарплата, например: Vasya - 5000
# После чего прочитайте файл, выведите построчно имя и зарплату минус 13% (налоги ведь),
# Есть условие, не отображать людей получающих более зарплату 500000, как именно
#  выполнить условие решать вам, можете не писать в файл
# можете не выводить, подумайте какой способ будет наиболее правильным и оптимальным,
#  если скажем эти файлы потом придется передавать.
# Так же при выводе имя должно быть полностью в верхнем регистре!
# Подумайте вспоминая урок, как это можно сделать максимально кратко, используя возможности языка Python.

def Normal_first_task():
    names = input('Введите имена через пробел: ').split(' ')
    salary = input('Введите зарплаты через пробел: ').split(' ')
    pairs = list(zip(names,salary))
    path = os.path.join('','salary.txt')
    with open(path,'w',encoding='UTF-8') as f:
        for el in pairs:
            f.write(f'{str(el[0])} - {el[1]}\n')
    with open(path,encoding='UTF-8') as f:
        for line in f.readlines():
            worker = line[:-1].split(' ') #срез без \n чтобы был нормальный вывод в консоль
            name = worker[0]
            salary = int(worker[2])
            if salary > 500000:
                continue
            print(name.upper(), salary*0.87,sep=' - ' )
#Hard
# Задание - 1
# Давайте опишем пару сущностей player и enemy через словарь,
# который будет иметь ключи и значения:
# name - строка полученная от пользователя,
# health - 100,
# damage - 50.
# Поэксперементируйте с значениями урона и жизней по желанию.
# Теперь надо создать функцию attack(person1, person2), аргументы можете указать свои,
# функция в качестве аргумента будет принимать атакующего и атакуемого,
# функция должна получить параметр damage атакующего и отнять это количество
# health от атакуемого. Функция должна сама работать с словарями и изменять их значения.

def Hard_first_task():
    name_pl = input('Введите имя игрока: ')
    name_en = input('Введите имя врага: ')
    player = {'name':name_pl,'health':100,'damage':19}
    enemy = {'name': name_en,'health':120,'damage':9}
    def attack(attacker, defenser):
        defenser['health'] -= attacker['damage']
        print(f'Игрок {attacker['name']} наносит удар игроку {defenser['name']}')
        print(f'Здоровье {defenser['name']} теперь равно: {defenser['health']}')
    attack(player, enemy)

# Задание - 2
# Давайте усложним предыдущее задание, измените сущности, добавив новый параметр - armor = 1.2
# Теперь надо добавить функцию, которая будет вычислять и возвращать полученный урон по формуле damage / armor
# Следовательно у вас должно быть 2 функции, одна наносит урон, вторая вычисляет урон по отношению к броне.
# Сохраните эти сущности, полностью, каждую в свой файл,
# в качестве названия для файла использовать name, расширение .txt
# Напишите функцию, которая будет считывать файл игрока и его врага, получать оттуда данные, и записывать их в словари,
# после чего происходит запуск игровой сессии, где сущностям поочередно наносится урон,
# пока у одного из них health не станет меньше или равен 0.
# После чего на экран должно быть выведено имя победителя, и количество оставшихся единиц здоровья.

def Hard_second_task():
    name_player = input('Введите имя игрока: ')
    health = int(input('Введите здоровье игрока: '))
    damage = int(input('Введите урон игрока: '))
    armor = float(input('Введите броню игрока: '))
    path_player = os.path.join('',f'{name_player}.txt')
    with open(path_player,'w',encoding='UTF-8') as f:
        f.write(f'{name_player} - {health} - {damage} - {armor}')
    name_enemy = input('Введите имя противника: ')
    health = int(input('Введите здоровье противника: '))
    damage = int(input('Введите урон противника: '))
    armor = float(input('Введите броню противника: '))
    path_enemy = os.path.join('', f'{name_enemy}.txt')
    with open(path_enemy,'w',encoding='UTF-8') as f:
        f.write(f'{name_enemy} - {health} - {damage} - {armor}')
    def read():
        player = {'name':'','health':0,'damage':0,'armor':0}
        with open(path_player,'r',encoding='UTF-8') as f:
            line = f.readline().split(' ')
            player['name'] = line[0]
            player['health'] = int(line[2])
            player['damage'] = int(line[4])
            player['armor'] = float(line[6])
        enemy = {'name':'','health':0,'damage':0,'armor':0}
        with open(path_enemy,'r',encoding='UTF-8') as f:
            line = f.readline().split(' ')
            enemy['name'] = line[0]
            enemy['health'] = int(line[2])
            enemy['damage'] = int(line[4])
            enemy['armor'] = float(line[6])
        return player,enemy


    player, enemy = read()

    def reducewithArm(damage,armor):
        actual_dmg = damage / armor
        return actual_dmg


    def attack(attacker,attacked):
        attacked['health'] -= reducewithArm(attacker['damage'],attacked['armor'])
        print(f'Игрок {attacker['name']} наносит удар игроку {attacked['name']},'
              f'Урон без брони:{attacker['damage']},'
              f'Урон с броней:{reducewithArm(attacker['damage'],attacked['armor']):.2f}')
        print(f'Здоровье {attacked['name']} теперь равно: {attacked['health']:.2f}')


    game = input('Начать сражение(y/n)?: ')
    if game == 'n':
        print('Сворачиваем сражение...')
    elif game == 'y':
        while True:
            attack(player,enemy)
            if (enemy['health'] <= 0) and (player['health'] > 0):
                print(f'Победил {player['name']} c {enemy['health']:.2f} ОЗ')
                break
            attack(enemy,player)
            if (enemy['health'] > 0) and (player['health'] <= 0):
                print(f'Победил {enemy['name']} c {enemy['health']:.2f} ОЗ')
                break


if __name__ == "__main__":
    Hard_second_task()