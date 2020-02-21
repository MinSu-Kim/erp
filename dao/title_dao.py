import inspect

from mysql.connector import Error

from dao.abs_dao import Dao, iter_row


class TitleDao(Dao):
    def __init__(self):
        super().__init__()

    def insert_item(self, code=None, name=None):
        print("\n______ {}() ______".format(inspect.stack()[0][3]))
        sql = "insert into title values(%s, %s)"
        args = (code, name)
        print(args)
        try:
            super().do_query(query=sql, kargs=args)
        except Error as err:
            raise err

    def update_item(self, code=None, price=None, saleCnt=None, marginPrice=None, no=None):
        print("\n______ {}() ______".format(inspect.stack()[0][3]))
        sql = "UPDATE sale SET code=%s, price=%s, saleCnt=%s, marginRate=%s WHERE no={}"
        args = (code, price, saleCnt, marginPrice, no)
        try:
            super().do_query(query=sql, kargs=args)
            return True
        except Error:
            return False

    def delete_item(self, no=None):
        print("\n______ {}() ______".format(inspect.stack()[0][3]))
        sql = "DELETE FROM sale WHERE no=%s"
        args = (no,)
        try:
            super().do_query(query=sql, kargs=args)
            return True
        except Error:
            return False

    def select_item(self, no=None):
        print("\n______ {}() ______".format(inspect.stack()[0][3]))
        with self.connection_pool as conn:
            cursor = conn.cursor()
            sql = "SELECT title_no, title_name FROM title"
            where = " where title_no = %s"
            cursor.execute(sql) if no is None else cursor.execute(sql.join(where), (no,))
            res = []
            [res.append(row) for row in iter_row(cursor, 5)]
            print(res)
            cursor.close()
            return res



if __name__ == '__main__':
    # app = QApplication([])
    # d = DepartmentTableViewWidget()
    # t = TitleTableViewWidget()
    # app.exec()
    tdao = TitleDao()
    # tdao.insert_item(6, '인턴')
    tdao.select_item()