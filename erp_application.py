from PyQt5.QtWidgets import QApplication

from table_view.abstract_table_view import AbstractTableViewWidget
from table_view.department_table_view import DepartmentTableViewWidget
from table_view.title_table_view import TitleTableViewWidget

if __name__ == '__main__':
    app = QApplication([])
    # w = CustomTableViewWidget()
    d = DepartmentTableViewWidget()
    t = TitleTableViewWidget()
    app.exec()