import shutil, os
from pathlib import Path

def create_file(name, text=''):
    name = Path(name)
    if not name.is_file():
        with open(name, 'w') as file:
            file.write(text)
    else:
        return "Такой файл уже существует"


def pwd():
    return str(home_dir)


def ls(name=None):
    if name:
        return '; '.join(os.listdir(name))
    return '; '.join(os.listdir(home_dir))


def mkdir(name):
    name = Path(name)
    if not name.is_dir():
        os.mkdir(name)
    else:
        return "Такая папка уже существует"


def rename(name1, name2):
    name1 = Path(name1)
    name2 = Path(name2)
    if name1.exists():
        os.rename(name1, name2)


def rmdir(name):
    name = Path(name)
    if name.is_dir():
        shutil.rmtree(name)
    else:
        return 'Это не папка'


def rm(name):
    name = Path(name)
    if name.is_file():
        os.remove(name)
    else:
        return 'Это не файл'


def move(src, dst):
    src = Path(src)
    dst = Path(dst)
    if src.exists():
        shutil.move(src, dst)


def cat(name):
    name = Path(name)
    if name.is_file():
        return name.read_text()


def hlp():
    return 'help - справка по командам\n' \
           'pwd - узнать название рабочей директории\n' \
           'ls - список файлов в рабочей директории\n' \
           'mkdir -  создать директорию с указанным именем\n' \
           'rmdir -  удалить директорию с указанным именем\n' \
           'cf -  создать файл с указанным именем\n' \
           'rm -  удалить файл с указанным именем\n' \
           'move -  переместить файл/директорию в другую директорию\n' \
           'rename -  переименновывает файл с указанным именем \n' \
           'cat -  показать содержимое файла\n' \
           'exit - выход из системы'

home_dir = Path(os.getcwd(), 'your_nome_dir')