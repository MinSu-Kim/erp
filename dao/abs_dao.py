import inspect
from abc import ABCMeta, abstractmethod

from mysql.connector import Error

from dbconnection.db_connecton import DatabaseConnectionPool
from dbconnection.db_pool import DatabasePool, Config


def iter_row(cursor, size=5):
    while True:
        rows = cursor.fetchmany(size)
        if not rows:
            break
        for row in rows:
            yield row


class Dao(metaclass=ABCMeta):

    def __init__(self):
        self.connection_pool = DatabaseConnectionPool.get_instance(filename='../resources/user_properties.ini')

    @abstractmethod
    def insert_item(self, **kwargs):
        raise NotImplementedError("Subclass must implement abstract method")

    @abstractmethod
    def update_item(self, **kwargs):
        raise NotImplementedError("Subclass must implement abstract method")

    @abstractmethod
    def delete_item(self, **kwargs):
        raise NotImplementedError("Subclass must implement abstract method")

    @abstractmethod
    def select_item(self, **kwargs):
        raise NotImplementedError("Subclass must implement abstract method")


    def do_query(self, **kwargs):
        print("\n______ {}() ______".format(inspect.stack()[0][3]))
        try:
            config = Config('resources/user_properties.ini')
            with DatabasePool.get_instance(config) as conn:
                cursor = conn.cursor()
                if 'SELECT'.lower() in kwargs['query'].lower():
                    if kwargs['kargs'] is not None:
                        cursor.execute(kwargs['query'], kwargs['kargs'])
                    else:
                        cursor.execute(kwargs['query'])
                    conn.commit()
                    affected = f"{cursor.rowcount} rows affected."
                    return affected
                else:
                    cursor.execute(kwargs['query'])
                    res = []
                    [res.append(row) for row in iter_row(cursor, 5)]
                    print(res)
                    return res
        except Error as e:
            print(e)
            raise e
