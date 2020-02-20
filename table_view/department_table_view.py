from PyQt5 import uic
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QAbstractItemView, QHeaderView

from model.department_table_model import DepartmentTableModel
from table_view.abstract_table_view import AbstractTableViewWidget


class DepartmentTableViewWidget(AbstractTableViewWidget):
    def __init__(self):
        super().__init__()

        tble_data = [(1,'인사', 20),(2, '개발', 10)]
        header = ['부서 번호', '부서 명', '위치']

        # table에 data 로드
        self.model = DepartmentTableModel(data=tble_data, header=header)
        self.tableView.setModel(self.model)

        self.ui.setGeometry(300, 300, 600, 200) # 창의 좌표(x, y) 크기(width, height)
        self.ui.show()

    def set_column_size(self):
        self.tableView.horizontalHeader().resizeSection(0, 40)
        self.tableView.horizontalHeader().resizeSection(1, 50)
        self.tableView.horizontalHeader().resizeSection(2, 30)
