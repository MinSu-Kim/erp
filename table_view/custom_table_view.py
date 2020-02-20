from PyQt5 import uic
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QAbstractItemView

from model.custom_table_model import CustomTableModel


class CustomTableViewWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi('ui/table_view.ui')

        # create the view
        self.tableView = self.ui.custom_table_view

        # table view 설정
        self.set_table_view_config()

        tble_data = [(1,'아메리카노'),(2, '카페모카')]
        header = ['제품 코드', '제품 명']

        # table에 data 로드
        self.model = None
        self.set_table_row_data(tble_data, header)

        self.ui.show()

    def set_table_row_data(self, tble_data, header):
        self.model = CustomTableModel(data=tble_data, header=header)
        self.tableView.setModel(self.model)

    def set_table_view_config(self):
        # header size
        self.tableView.horizontalHeader().resizeSection(0, 40)
        self.tableView.horizontalHeader().resizeSection(1, 60)
        self.tableView.horizontalHeader().setStyleSheet('QHeaderView::section{background:#66666666}')  # 배경색을 녹색
        # Set the alignment to the headers
        self.tableView.horizontalHeader().setDefaultAlignment(Qt.AlignCenter)
        # 셀 내용 수정불가
        self.tableView.setEditTriggers(QAbstractItemView.NoEditTriggers)
        # hide grid
        self.tableView.setShowGrid(True)
        # row단위 선택
        self.tableView.setSelectionBehavior(QAbstractItemView.SelectRows)
        # 헤더의 내용을 tableView의 크기에 맞춤
        self.tableView.horizontalHeader().setStretchLastSection(True)
        # 모든 컬럼의 사이즈를 동일하게 맞춤
        # self.tableView.resizeColumnsToContents()
        # self.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)