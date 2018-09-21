#coding : utf-8

import os, sys
from Easy05 import mk_dir, remove_dirs
# Задача-1:
# Напишите небольшую консольную утилиту,
# позволяющую работать с папками текущей директории.
# Утилита должна иметь меню выбора действия, в котором будут пункты:

def change_dir(folder):
    os.chdir(folder)

def ldir():
    print(os.listdir())

do = {
    1: change_dir,
    2: ldir,
    3: remove_dirs,
    4: mk_dir,
}
while True:
    choice = input('1. Перейти в папку\n'
                   '2. Просмотреть содержимое текущей папки\n'
                   '3. Удалить папку\n'
                   '4. Создать папку\n'
                   '5. Выход\n\n')
    try:
        if len(choice.split()) == 2:
            choice, foldername = choice.split()
            choice = int(choice)
            if do.get(choice):
                do[choice](foldername)
        else:
            choice = int(choice)
            if choice == 5:
                break
            elif do.get(choice):
                print(do[choice]())
    except ValueError:
        print('Неверное значение')
    except TypeError:
        print('Название папки отсутствует')




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