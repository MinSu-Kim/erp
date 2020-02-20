import inspect

from mysql.connector import Error

from dao.abs_dao import Dao, iter_row


class TitleDao(Dao):

    def insert_item(self, code=None, name=None):
        print("\n______ {}() ______".format(inspect.stack()[0][3]))
        sql = "insert into title values(%s, %s)"
        args = (code, name)
        try:
            self.do_query(query=sql, kargs=args)
        except Error as err:
            raise err

    def update_item(self, code=None, price=None, saleCnt=None, marginPrice=None, no=None):
        print("\n______ {}() ______".format(inspect.stack()[0][3]))
        sql = "UPDATE sale SET code=%s, price=%s, saleCnt=%s, marginRate=%s WHERE no={}"
        args = (code, price, saleCnt, marginPrice, no)
        try:
            self.do_query(query=sql, kargs=args)
            return True
        except Error:
            return False

    def delete_item(self, no=None):
        print("\n______ {}() ______".format(inspect.stack()[0][3]))
        sql = "DELETE FROM sale WHERE no=%s"
        args = (no,)
        try:
            self.do_query(query=sql, kargs=args)
            return True
        except Error:
            return False

    def select_item(self, no=None):
        print("\n______ {}() ______".format(inspect.stack()[0][3]))
        try:
            conn = self.connection_pool.get_connection()
            cursor = conn.cursor()
            sql = "SELECT no, code, price, saleCnt, marginRate FROM sale"
            where = " where no = %s"
            cursor.execute(sql) if no is None else cursor.execute(sql.join(where), (no,))
            res = []
            [res.append(row) for row in iter_row(cursor, 5)]
            print(res)
            return res
        except Error as e:
            print(e)
        finally:
            cursor.close()
            conn.close()
