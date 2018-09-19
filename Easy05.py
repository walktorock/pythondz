#coding : utf-8

import os, shutil

# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.
def create_dir():
        i = 1
        while i < 10:
            dir_path = os.path.join(os.getcwd(), 'dir_{}'.format(i))
            os.mkdir(dir_path)
            i += 1

def remove_dir():
    files = os.listdir()
    i = 0
    while i < len(files):
        dirs = os.path.join(os.getcwd(), files[i])
        if dirs.endswith('_{}'.format(i)):
            os.remove(dirs)
        i += 1

#Отказ в доступе при попытке выполнить скрипт

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.


# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.