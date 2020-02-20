from mysql.connector.pooling import MySQLConnectionPool

from database_init.read_config import read_db_config


class DatabaseConnectionPool(object):
    INSTANCE = None

    def __init__(self, filename='../resources/db_properties.ini'):
        if self.INSTANCE is not None:
            raise ValueError("An instantiation already exists!")
        else:
            db_config = read_db_config(filename)
            self.__cnxPool = MySQLConnectionPool(pool_name="myPool", pool_size=10, **db_config)

    @classmethod
    def get_instance(cls, filename='../resources/db_properties.ini', ):
        print("get_instance() ------------", filename)
        if cls.INSTANCE is None:
            cls.INSTANCE = DatabaseConnectionPool(filename)
        return cls.INSTANCE;

    def get_connection(self):
        return self.__cnxPool.get_connection()

    @classmethod
    def pool_close(cls):
        cls.INSTANCE = None;


if __name__ == "__main__":
    conn = DatabaseConnectionPool.get_instance(filename='../resources/db_properties.ini').get_connection()
    print("conn", conn)
