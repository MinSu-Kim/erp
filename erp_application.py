from dao.abs_dao import iter_row
from dao.title_dao import TitleDao
from dbconnection.db_pool import DatabasePool, Config

if __name__ == '__main__':
    # app = QApplication([])
    # d = DepartmentTableViewWidget()
    # t = TitleTableViewWidget()
    # app.exec()


    tdao = TitleDao()
    # tdao.select_item()
    # tdao.insert_item(6, '인턴')

    config = Config('resources/user_properties.ini')
    with DatabasePool.get_instance(config) as conn:
        cursor = conn.cursor()
        sql = "SELECT title_no, title_name FROM title"
        cursor.execute(sql)
        res = []
        [res.append(row) for row in iter_row(cursor, 5)]
        print(res)


    config = Config('resources/user_properties.ini')
    with DatabasePool.get_instance(config) as conn:
        print("conn", conn)

    DatabasePool.pool_close()

    with DatabasePool.get_instance(config) as conn:
        print("conn", conn)