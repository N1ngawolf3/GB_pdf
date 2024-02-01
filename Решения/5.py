import os
import sys


#Easy
# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.
def Easy_first_task():


    def make_dir():
        for i in range(9):
            dir_path = os.path.join(os.getcwd(), f'dir_{i+1}')
            os.mkdir(dir_path)
        print('Папки созданы')


    def del_dir():
        for i in range(9):
            dir_path = os.path.join(os.getcwd(), f'dir_{i+1}')
            os.rmdir(dir_path)
        print('Папки удалены')

    do = {'make_dir':make_dir,
          'del_dir':del_dir,
          'quit':sys.exit}

    while True:
        command = input('Введите команду:')
        do[f'{command}']()

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.
def Easy_second_task():
    dir_path = os.path.join(os.getcwd())
    for file in os.listdir(dir_path):
        if not os.path.isfile(file):
            print(file)


# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.
def Easy_third_task():
    script_name = sys.argv[0].split('\\')[-1]
    with open('copy.py','w',encoding='UTF-8') as copy:
        with open(script_name,'r',encoding='UTF-8') as original:
            for line in original.readlines():
                copy.write(line)


#Normal
# Задача-1:
# Напишите небольшую консольную утилиту,
# позволяющую работать с папками текущей директории.
# Утилита должна иметь меню выбора действия, в котором будут пункты:
# 1. Перейти в папку
# 2. Просмотреть содержимое текущей папки
# 3. Удалить папку
# 4. Создать папку
# При выборе пунктов 1, 3, 4 программа запрашивает название папки
# и выводит результат действия: "Успешно создано/удалено/перешел",
# "Невозможно создать/удалить/перейти"

# Для решения данной задачи используйте алгоритмы из задания easy,
# оформленные в виде соответствующих функций,
# и импортированные в данный файл из easy.py
def Normal_first_task():
    def to_dir():
        while True:
            try:
                name = input('Введите название папки: ')
                os.chdir(os.getcwd()+'\\'+name)
                break
            except:
                print('Невозможно перейти')



    def view_files():
        print(os.listdir())


    def del_dir():
        while True:
            try:
                name = input('Введите название папки: ')
                dir_path = os.path.join(os.getcwd(), f'{name}')
                os.rmdir(dir_path)
                print('Папка удалена')
                break
            except:
                print('Невозможно удалить')



    def make_dir():
        while True:
            name = input('Введите имя папки: ')
            dir_path = os.path.join(os.getcwd(), f'{name}')
            os.mkdir(dir_path)
            print('Папка создана')
            break

    do = {'1':to_dir,
          '2':view_files,
          '3':del_dir,
          '4':make_dir}

    while True:
        print("""Выберите действие из списка ниже:
                 1. Перейти в папку
                 2. Просмотреть содержимое текущей папки
                 3. Удалить папку
                 4. Создать папку """)
        command = input('Введите номер команды: ')
        do[command]()

#Hard
# Задание-1:
# Доработайте реализацию программы из примера examples/5_with_args.py,
# добавив реализацию следующих команд (переданных в качестве аргументов):
# cp <file_name> - создает копию указанного файла
# rm <file_name> - удаляет указанный файл (запросить подтверждение операции)
# cd <full_path or relative_path> - меняет текущую директорию на указанную
# ls - отображение полного пути текущей директории
# путь считать абсолютным (full_path) -
# в Linux начинается с /, в Windows с имени диска,
# все остальные пути считать относительными.

# Важно! Все операции должны выполняться в той директории, в который вы находитесь.
# Исходной директорией считать ту, в которой был запущен скрипт.
# P.S. По возможности, сделайте кросс-платформенную реализацию.

#Фактически тоже самое, что и функция выше с небольшими изменениями

if __name__ == '__main__':
    Normal_first_task()