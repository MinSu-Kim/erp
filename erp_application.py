from PyQt5.QtWidgets import QApplication

from dao.title_dao import TitleDao
from table_view.abstract_table_view import AbstractTableViewWidget
from table_view.department_table_view import DepartmentTableViewWidget
from table_view.title_table_view import TitleTableViewWidget

if __name__ == '__main__':
    # app = QApplication([])
    # d = DepartmentTableViewWidget()
    # t = TitleTableViewWidget()
    # app.exec()
    tdao = TitleDao()
    tdao.insert_item(6, '인턴')
