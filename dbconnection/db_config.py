from database_init.read_config import read_db_config


class Config:
    def __init__(self, con_file=None):
        """environ = read_db_config(filename='../resources/user_properties.ini')"""
        environ = read_db_config(filename=con_file)
        print(environ)
        # Database config
        self.db_user = environ.get('user')
        self.db_password = environ.get('password')
        self.db_host = environ.get('host')
        self.db_port = int(environ.get('port'))
        self.db_name = environ.get('database')
        for k, v in environ.items():
            print(k, type(v))