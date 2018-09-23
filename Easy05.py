#coding : utf-8

import os, shutil, sys


# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.


# def create_dir():
#         i = 1
#         while i < 10:
#             dir_path = os.path.join(os.getcwd(), 'dir_{}'.format(i))
#             os.mkdir(dir_path)
#             i += 1

def mk_dir(path):
    try:
        os.mkdir(path)
        print('Директория успешно создана')
    except FileExistsError:
        print('Недостаточно прав для создания директории')



def remove_dirs(path):
    try:
        os.removedirs(path)
        print('Директории успешно удалены')
    except FileNotFoundError:
        print('Директория для удаления не найдена')
    except PermissionError:
        print('Недостаточно прав для удаления')




# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.


def list_dir():
    print([i for i in os.listdir() if os.path.isdir(i)])



# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.


def copyfile():
    filename = sys.argv[0]
    fn, extention = filename.split('.')
    shutil.copy(filename, fn + '.copy.' + extention)


