import pymysql

from database_init.read_config import read_db_config

"""Config values."""


class Config:
    environ = read_db_config(filename='../resources/user_properties.ini')
    print(environ)
    # Database config
    db_user = environ.get('user')
    db_password = environ.get('password')
    db_host = environ.get('host')
    db_port = environ.get('port')
    db_name = environ.get('database')


class Database:
    """Database connection class."""

    def __init__(self, config):
        self.host = config.db_host
        self.username = config.db_user
        self.password = config.db_password
        self.port = config.db_port
        self.dbname = config.db_name
        self.conn = None

    def open_connection(self):
        """Connect to MySQL Database."""
        try:
            if self.conn is None:
                self.conn = pymysql.connect(self.host,
                                            user=self.username,
                                            passwd=self.password,
                                            db=self.dbname,
                                            connect_timeout=5)
        except pymysql.MySQLError as e:
            raise e
        finally:
            print('Connection opened successfully.')

    def run_query(self, query):
        """Execute SQL query."""
        try:
            self.open_connection()
            with self.conn.cursor() as cur:
                if 'SELECT' in query:
                    records = []
                    cur.execute(query)
                    result = cur.fetchall()
                    for row in result:
                        records.append(row)
                    cur.close()
                    return records
                else:
                    result = cur.execute(query)
                    self.conn.commit()
                    affected = f"{cur.rowcount} rows affected."
                    cur.close()
                    return affected
        except pymysql.MySQLError as e:
            print(e)
        finally:
            if self.conn:
                self.conn.close()
                self.conn = None
                print('Database connection closed.')


if __name__ == '__main__':
    # erp_setting.py가 있는 위치를 기준으로 작성해야 됨.
    # Config()
    db = Database(Config())
    res = db.run_query('SELECT title_no, title_name from title where title_no=1')
    print(res)