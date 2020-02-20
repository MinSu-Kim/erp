import csv
import imghdr
import os

import mysql
from mysql.connector import Error

from database_init.read_config import read_db_config
from dbconnection.db_connecton import DatabaseConnectionPool


class BackupRestore:

    def __init__(self, db_conf=None):
        self.db_conf = db_conf
        self._db = read_db_config(db_conf)

    def backup_data(self):
        self.__backup_data()

    def __backup_data(self, data_dir='backup', sql_filename='../resources/select_sql.ini'):
        self.__check_exists_dir(data_dir)
        sql_info = read_db_config(sql_filename)
        print(sql_info)
        for table_name, table_sql in sql_info.items():
            self.__backup_query(data_dir, table_sql, table_name)
        print("OK")

    def __check_exists_dir(self, data_dir):
        if os.path.exists(data_dir):
            for f in os.scandir(data_dir):
                if os.path.isdir(f):
                    for sub_f in os.scandir(f):
                        os.remove(sub_f.path)
                    os.rmdir(f)
                else:
                    os.remove(f.path)
            os.rmdir(data_dir)
        os.mkdir(data_dir)

    def __backup_query(self, data_dir, select_sql, table_name):
        try:
            file_name = "{}/{}.txt".format(data_dir, table_name)
            con = DatabaseConnectionPool.get_instance(filename=self.db_conf).get_connection()
            print("__backup_query-----------", self.db_conf)
            cursor = con.cursor()
            cursor.execute(select_sql)
            rows = cursor.fetchall()
            with open(file_name, 'w', newline='\n', encoding='utf-8') as tuple_fp:
                for row in rows:
                    img_path = data_dir+'/img'
                    if not os.path.exists(img_path):
                        os.mkdir(img_path)
                    filename = "{}/{}".format(img_path, row[0])
                    row_item = []
                    for item in row:
                        # print('=====================', type(item))
                        if isinstance(item, bytes) or isinstance(item, bytearray):
                            img_path = self.__write_file(item, filename)
                            row_item.append(img_path)
                            continue
                        row_item.append(item)
                    csv.writer(tuple_fp).writerow(row_item)
        except Error as e:
            raise e
        finally:
            cursor.close()
            con.close()

    def __load_data(self, con=None, sql_filename='../resources/insert_sql.ini'):
        _db = read_db_config(sql_filename)
        try:
            cursor = con.cursor()
            for table_name, table_sql in _db.items():
                print('==============__load_data', table_name, table_sql)
                cursor.execute(table_sql)
            con.commit()
            print("OK")
        except mysql.connector.Error as err:
            raise err
        finally:
            cursor.close()

    def __load_img(self, con=None, data_dir='../restore_backup/backup/img', query='update employee set pic=%s where emp_no=%s'):

        if os.path.exists(data_dir):
            for f in os.scandir(data_dir):
                data = self.__read_file(os.path.abspath(f))
                img_file = os.path.basename(f).split('.')[0]
                try:
                    cursor = con.cursor()
                    cursor.execute(query, (data, img_file))
                    con.commit()
                except mysql.connector.Error as err:
                    raise err
                finally:
                    cursor.close()

    def __read_file(self, filename):
        with open(filename, 'rb') as f:
            photo = f.read()
        return photo

    def __write_file(self, data, filename):
        with open(filename, 'wb') as f:
            f.write(data)
        file_ext = imghdr.what(filename)
        os.rename(filename, filename+'.'+file_ext)
        return str(filename+'.'+file_ext)

    def load_data(self):
        con = DatabaseConnectionPool.get_instance(filename=self.db_conf).get_connection()
        try:
            self.__load_data(con)
            self.__load_img(con)
        except mysql.connector.Error as err:
            raise err
        finally:
            con.close()


if __name__ == "__main__":

    backup_restore = BackupRestore(db_conf='../resources/user_properties.ini')
    # backup_restore.backup_data()
    backup_restore.load_data()
    # backup_restore.__load_img(query='update employee set pic=%s where emp_no=%s')

