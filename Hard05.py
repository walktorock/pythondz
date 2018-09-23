#coding : utf-8

# Задание-1:
# Доработайте реализацию программы из примера examples/5_with_args.py,
# добавив реализацию следующих команд (переданных в качестве аргументов):
#   cp <file_name> - создает копию указанного файла
#   rm <file_name> - удаляет указанный файл (запросить подтверждение операции)
#   cd <full_path or relative_path> - меняет текущую директорию на указанную
#   ls - отображение полного пути текущей директории
# путь считать абсолютным (full_path) -
# в Linux начинается с /, в Windows с имени диска,
# все остальные пути считать относительными.

# Важно! Все операции должны выполняться в той директории, в который вы находитесь.
# Исходной директорией считать ту, в которой был запущен скрипт.

# P.S. По возможности, сделайте кросс-платформенную реализацию.

import os, shutil, sys


print('sys.argv = ', sys.argv)


def print_help():
    print("help - получение справки")
    print("mkdir <dir_name> - создание директории")
    print("ping - тестовый ключ")
    print('cp <file_name> - создает копию указанного файла')
    print('rm <file_name> - удаляет указанный файл (запросить подтверждение операции)')
    print('cd <full_path or relative_path> - меняет текущую директорию на указанную')
    print('ls - отображение полного пути текущей директории')

def copyfile():
    try:
        filename = input('Введите имя файла, для копирования')
        fn, extention = filename.split('.')
        shutil.copy(filename, fn + '.copy.' + extention)
    except FileNotFoundError:
        print('Указанный файл не найден')

def change_dir(folder):
    try:
        print(os.chdir(folder))
    except FileNotFoundError:
        print('Директория не найдена')

def ldir():
    print(os.listdir())

def remove_file(path):
    try:
        ans = input('Вы точно хотите удалить файл? Y/N')
        if ans == 'Y':
            os.remove(path)
            print('Файл успешно удален')
        else:
            print('Удаление отменено')
    except FileNotFoundError:
        print('Файл для удаления не найден')
    except PermissionError:
        print('Недостаточно прав для удаления')

def make_dir():
    if not dir_name:
        print("Необходимо указать имя директории вторым параметром")
        return
    dir_path = os.path.join(os.getcwd(), dir_name)
    try:
        os.mkdir(dir_path)
        print('директория {} создана'.format(dir_name))
    except FileExistsError:
        print('директория {} уже существует'.format(dir_name))


def ping():
    print("pong")

do = {
    "help": print_help,
    "mkdir": make_dir,
    "ping": ping,
    'rm': remove_file,
    'cp': copyfile,
    'cd': change_dir,
    'ls': ldir()
}

try:
    dir_name = sys.argv[2]
except IndexError:
    dir_name = None

try:
    key = sys.argv[1]
except IndexError:
    key = None


if key:
    if do.get(key):
        do[key]()
    else:
        print("Задан неверный ключ")
        print("Укажите ключ help для получения справки")