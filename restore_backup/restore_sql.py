import os

import mysql
from mysql.connector import Error

from database_init.read_config import read_db_config
from dbconnection.db_connecton import DatabaseConnectionPool


class BackupRestore:

    def __init__(self, filename='sql.ini'):
        self._db = read_db_config(filename)

    def load_data(self):
        try:
            con = DatabaseConnectionPool.get_instance(filename='../resources/user_properties.ini').get_connection()
            cursor = con.cursor()
            print(self._db)
            for table_name, table_sql in self._db.items():
                # print(table_name, " ==> ", table_sql)
                cursor.execute(table_sql)
            print("OK")
        except mysql.connector.Error as err:
            raise err
        finally:
            cursor.close()
            con.close()


if __name__ == "__main__":

    backup_restore = BackupRestore()
    backup_restore.load_data()
    # backup_restore.data_backup('department')
    # backup_restore.data_backup('sale')

    # backup_restore.data_restore('department')
