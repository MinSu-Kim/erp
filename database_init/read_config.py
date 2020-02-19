import sys
from configparser import ConfigParser

from PyQt5.QtWidgets import QMessageBox, QWidget


def read_db_config(filename='sql.ini'):
    parser = ConfigParser()
    parser.read(filename, encoding='UTF8')

    db = {}
    for section in parser.sections():
        if parser.has_section(section):
            items = parser.items(section)
            if items.__len__() > 1 and section == 'table':
                sql = {}
                for key, value in items:
                    sql[key] = "".join(value.splitlines())
                db['sql'] = sql
            for item in items:
                db[item[0]] = "".join(item[1].splitlines())
        else:
            raise Exception('{0} not found in the {1} file'.format(section, filename))

    return db


if __name__ == "__main__":
    # db = read_db_config()
    # print(db)

    try:
        db = read_db_config(filename='../resources/db_properties')
    except Exception as err:
        print("error", err)

