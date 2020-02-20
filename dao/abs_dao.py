import inspect
from abc import ABCMeta, abstractmethod

from mysql.connector import Error

from dbconnection.db_connecton import DatabaseConnectionPool


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
            conn = self.connection_pool.get_connection()
            cursor = conn.cursor()
            if kwargs['p_args'] is not None:
                cursor.execute(kwargs['query'], kwargs['kargs'])
            else:
                cursor.execute(kwargs['query'])
            conn.commit()
        except Error as e:
            print(e)
            raise e
        finally:
            cursor.close()
            conn.close()