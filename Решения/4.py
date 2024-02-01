from random import randint
import re

#Easy
# Все задачи текущего блока решите с помощью генераторов списков!

# Задание-1:
# Дан список, заполненный произвольными целыми числами.
# Получить новый список, элементы которого будут
# квадратами элементов исходного списка
# [1, 2, 4, 0] --> [1, 4, 16, 0]

def Easy_first_task():
    mlist = [randint(-10,10) for _ in range(10)]
    sqlist = [el*el for el in mlist]
    print(*mlist)
    print(*sqlist)


# Задание-2:
# Даны два списка фруктов.
# Получить список фруктов, присутствующих в обоих исходных списках.

def Easy_second_task():
    list1 = ['яблоко','груша','банан']
    list2 = ['яблоко','банан']
    list_comb = [fruit for fruit in list1 if fruit in list2]
    print(list_comb)

# Задание-3:
# Дан список, заполненный произвольными числами.
# Получить список из элементов исходного, удовлетворяющих следующим условиям:
# + Элемент кратен 3
# + Элемент положительный
# + Элемент не кратен 4

def Easy_third_task():
    mlist = [randint(-10,10) for _ in range(10)]
    newlist = [el for el in mlist if (el%3==0) and (el>0) and (el%4!=0)]
    print(mlist)
    print(newlist)


#Normal
# Эти задачи необходимо решить используя регулярные выражения!

# Задача - 1
# Запросите у пользователя имя, фамилию, email. Теперь необходимо совершить проверки,
# имя и фамилия должны иметь заглавные первые буквы.
# email - не должен иметь заглавных букв и должен быть в формате: текст в нижнем регистре,
# допускается нижнее подчеркивание и цифры, потом @, потом текст, допускаются цифры, точка, ru или org или com.
# Например:
# Пупкин василий - неверно указано имя, te$T@test.net - неверно указан email
# (спецсимвол, заглавная буква, .net), te_4_st@test.com - верно указан.

def Normal_first_task():
    name = input('Введите имя: ')
    surname = input('Введите фамилию: ')
    email = input('Введите email: ')

    pattern = '^[А-Я][а-я]+$'

    if not re.search(pattern, name):
        print('Имя введено неверно!')
    if not re.search(pattern, surname):
        print('Фамилия введена неверно!')
    if not re.search('^[a-z_0-9]+@[a-z0-9]+\.ru|org|com$', email):
        print('Email введен неверно!')


 # Задача - 2:
    # Вам дан текст:
 # Необходимо с помощью регулярных выражений определить есть ли в тексте подряд
    # более одной точки, при любом исходе сообщите результат пользователю!
def Normal_second_task():
    some_str = '''
    Мороз и солнце; день чудесный!
    Еще ты дремлешь, друг прелестный —
    Пора, красавица, проснись:
    Открой сомкнуты негой взоры
    Навстречу северной Авроры,
    Звездою севера явись!
    Вечор, ты помнишь, вьюга злилась,
    На мутном небе мгла носилась;
    Луна, как бледное пятно,
    Сквозь тучи мрачные желтела,
    И ты печальная сидела —
    А нынче... погляди в окно:
    Под голубыми небесами
    Великолепными коврами,
    Блестя на солнце, снег лежит;
    Прозрачный лес один чернеет,
    И ель сквозь иней зеленеет,
    И речка подо льдом блестит.
    Вся комната янтарным блеском
    Озарена. Веселым треском
    Трещит затопленная печь.
    Приятно думать у лежанки.
    Но знаешь: не велеть ли в санки
    Кобылку бурую запречь?
    Скользя по утреннему снегу,
    Друг милый, предадимся бегу
    Нетерпеливого коня
    И навестим поля пустые,
    Леса, недавно столь густые,
    И берег, милый для меня.'''

    if re.search('\.{2,}',some_str):
        print('Found')
    else:
        print('Not found')


# Hard
# Задание:
# Эта программа являет собой упрощенный симулятор банкомата, пользователь вводит номер карты и пин код,
# в случае успеха программа предлагает меню для выбора действий, где он может проверить счет, или снять деньги.
#
# Эта задача не так похожа на другие, но она, как никогда прежде приближена к реалиям разработки общего проекта.
#
# Ваша задача исправить ошибки логики, и выполнить проверки данных, которые вводит пользователь.
# Обязательно убедитесь, что вы выполнили все проверки, попробуйте сами сломать свою программу вводя неверные данные!
def Hard_first_task():
    person1 = {'card': 4276123465440000, 'pin': 9090, 'money': 100.90}
    person2 = {'card': 4276123465440001, 'pin': 9091, 'money': 200.90}
    person3 = {'card': 4276123465440002, 'pin': 9092, 'money': 300.90}

    bank = [person1, person2, person3]


    def get_person_by_card(card_number):
        for person in bank:
            if person['card'] == card_number:
                return person


    def is_pin_valid(person, pin_code):
        if person['pin'] == pin_code:
            return True
        else:
            return False


    def check_account(person):
        return round(person['money'], 2)


    def withdraw_money(person, money):
        if person['money'] - money >= 0:
            person['money'] -= money
            return 'Вы сняли {} рублей.'.format(money)
        else:
            return 'На вашем счету недостаточно средств!'


    def process_user_choice(choice, person):
        if choice == 1:
            print(check_account(person))
        elif choice == 2:
            count = float(input('Сумма к снятию:'))
            print(withdraw_money(person, count))


    def start():
        card_number, pin_code = input('Введите номер карты и пин код через пробел:').split()

        card_number = int(card_number)
        pin_code = int(pin_code)
        person = get_person_by_card(card_number)
        if person and is_pin_valid(person, pin_code):
            while True:
                choice = int(input('Выберите пункт:\n'
                                   '1. Проверить баланс\n'
                                   '2. Снять деньги\n'
                                   '3. Выход\n'
                                   '---------------------\n'
                                   'Ваш выбор:'))
                if choice == 3:
                    break
                process_user_choice(choice, person)
        else:
            print('Номер карты или пин код введены неверно!')

    start()


if __name__ == '__main__':
    Normal_first_task()