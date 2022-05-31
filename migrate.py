import sqlite3
from os.path import join, isfile
from config import *


def get_sql(filename):
    """Получает чмстый sql из файла
    Keyword arguments:
    argument -- полный путь до файла
    Return: строка с sql запросом
    """

    content = ''
    if isfile(filename):
        with open(filename) as file:
            content = file.read()

    return content


def main():
    """ 
    Основная функция выполняет миграцию данных
    
    """

    connection = sqlite3.connect(DATABASE_PATH)
    cursor = connection.cursor()

# Создаем структуру базы
    sql_script = get_sql(join(SQL_DIR_PATH, INIT_MIGRATION_FILE_PATH))
    cursor.executescript(sql_script)

# Заполняем данными
    data_sql = get_sql(join(SQL_DIR_PATH, DATA_MIGRATION_FILE_PATH))
    cursor.executescript(data_sql)

    cursor.close()
    connection.close()


if __name__ == '__main__':
    main()
