# pip install pymysql-pooling
# Note: you can also add any parameters relates to `pymysql.connections.Connection` object

from pymysqlpool.pool import Pool

pool = Pool(host='localhost', port=3306, user='user_pyqt_erp', password='rootroot', db='pyqt_erp')
pool.init()

connection = pool.get_conn()
cur = connection.cursor()
cur.execute('select title_no, title_name from title where title_no=%s', args=("1", ))
print(cur.fetchone())

pool.release(connection)