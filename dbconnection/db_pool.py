from pymysqlpool.pool import Pool

from dbconnection.db_config import Config


class DatabasePool(object):
    INSTANCE = None

    def __init__(self, config):
        if self.INSTANCE is not None:
            raise ValueError("An instantiation already exists!")
        else:
            self.__cnxPool = Pool(host=config.db_host, port=config.db_port, user=config.db_user
                                  , password=config.db_password, db=config.db_name)
            self.__cnxPool.init()

    @classmethod
    def get_instance(cls, config):
        if cls.INSTANCE is None:
            cls.INSTANCE = DatabasePool(config)
        return cls.INSTANCE;

    def get_connection(self):
        return self.__cnxPool.get_conn()

    @classmethod
    def pool_close(cls):
        cls.INSTANCE = None;

    def __enter__(self):
        self.conn = self.__cnxPool.get_conn()
        return self.conn

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.__cnxPool.release(self.conn)


if __name__ == "__main__":
    config = Config(con_file='../resources/user_properties.ini')
    print(config)
    with DatabasePool.get_instance(config) as conn:
        print("conn", conn)

    DatabasePool.pool_close()

    with DatabasePool.get_instance(config) as conn:
        print("conn", conn)