import os

from mysql.connector import Error

from dbconnection.db_connecton import DatabaseConnectionPool


class BackupRestore:
    OPTION = """
        CHARACTER SET 'UTF8'
        FIELDS TERMINATED by ','
        LINES TERMINATED by '\r\n'
        """

    def __init__(self, source_dir='data/', data_dir='data/'):
        self.source_dir = os.path.abspath(source_dir) + "/"
        self.data_dir = os.path.abspath(data_dir) + "/"

    def data_backup(self, table_name):
        filename = table_name + '.txt'
        try:
            conn = DatabaseConnectionPool.get_instance(filename='../resources/user_properties.ini').get_connection()
            cursor = conn.cursor()
            source_path = self.source_dir + filename
            # print('source_path =', source_path)

            if os.path.exists(source_path):
                os.remove(source_path)

            backup_sql = "SELECT * FROM {} INTO OUTFILE '{}' {}".format(table_name, source_path, BackupRestore.OPTION)
            # print("backup_sql ", backup_sql)
            cursor.execute(backup_sql)

            print(table_name, "backup complete!")
        except Error as err:
            print(err)
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()

    def data_restore(self, table_name):
        filename = table_name + '.txt'
        try:
            conn = DatabaseConnectionPool.get_instance(filename='../resources/user_properties.ini').get_connection()
            cursor = conn.cursor()

            data_path = os.path.abspath(self.data_dir + filename).replace('\\', '/')
            if not os.path.exists(data_path):
                print("파일 '{}' 이 존재하지 않음".format(data_path))
                return
            restore_sql = "LOAD DATA INFILE '{}' INTO TABLE {} {}".format(data_path, table_name,
                                                                          BackupRestore.OPTION)  # ubuntu
            print("restore_sql", restore_sql)
            cursor.execute(restore_sql)
            conn.commit()
            print(table_name, "restore complete!")
        except Error as err:
            print(err)
            print(table_name, "restore Fail!")
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()


if __name__ == "__main__":
    backup_restore = BackupRestore()
    # backup_restore.data_backup('department')
    # backup_restore.data_backup('sale')

    # backup_restore.data_restore('department')
