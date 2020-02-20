from PyQt5.QtWidgets import QApplication

from table_view.custom_table_view import CustomTableViewWidget
from table_view.department_table_view import DepartmentTableViewWidget

if __name__ == '__main__':
    app = QApplication([])
    w = CustomTableViewWidget()
    d = DepartmentTableViewWidget()
    app.exec()