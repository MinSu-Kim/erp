import mysql
from mysql.connector import errorcode, Error

from dbconnection.db_connecton import DatabaseConnectionPool
from database_init.read_config import read_db_config


class DbInit:
    def __init__(self, filename='insert_sql.ini', db_con_info=None):
        print(filename)
        self._db = read_db_config(filename)
        self._db_con_info=db_con_info
        print(self._db)

    def __create_database(self, con):
        try:
            cursor = con.cursor()
            cursor.execute("CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(self._db['database_name']))
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_DB_CREATE_EXISTS:
                cursor.execute("DROP DATABASE {} ".format(self._db['database_name']))
                cursor.execute("CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(self._db['database_name']))
            else:
                raise err
        finally:
            cursor.close()

    def __create_table(self, con):
        try:
            cursor = con.cursor()
            cursor.execute("USE {}".format(self._db['database_name']))
            for table_name, table_sql in self._db['sql'].items():
                try:
                    print("Creating table {}: ".format(table_name), end='')
                    cursor.execute(table_sql)
                except mysql.connector.Error as err:
                    if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                        raise err
                    else:
                        raise err
                else:
                    print("OK")
        except mysql.connector.Error as err:
            raise err
        finally:
            cursor.close()

    def __create_user(self, con):
        try:
            cursor = con.cursor()
            print("Creating user: ", end='')
            cursor.execute(self._db['user_sql'])
            cursor.execute(self._db['user_grant'])
            print("OK")
        except mysql.connector.Error as err:
            raise err
        finally:
            cursor.close()

    def init(self):
        print("init()-call")
        try:
            con = DatabaseConnectionPool.get_instance(self._db_con_info).get_connection()
            self.__create_database(con)
            self.__create_table(con)
            self.__create_user(con)
        except mysql.connector.Error as err:
            raise err
        finally:
            con.close()
            DatabaseConnectionPool.pool_close()


if __name__ == "__main__":
    conn = DatabaseConnectionPool.get_instance().get_connection()
    print("conn", conn)

    db = DbInit(filename='../resources/sql.ini')
    # db = DbInit(filename='../resources/db_properties.ini')
    db.init()

