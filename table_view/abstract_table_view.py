from abc import ABCMeta, abstractmethod

from PyQt5 import uic
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QAbstractItemView

from model.abstract_table_model import AbstractTableModel


class AbstractTableViewWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi('ui/table_view.ui')

        # create the view
        self.tableView = self.ui.custom_table_view
        self.model = None

        # table view 설정
        self.set_table_view_config()

    @abstractmethod
    def set_column_size(self):
        """
        self.tableView.horizontalHeader().resizeSection(0, 40)
        self.tableView.horizontalHeader().resizeSection(1, 50)
        """
        raise NotImplementedError("Subclass must implement abstract method")

    def set_table_view_config(self):
        # header size
        self.set_column_size()

        self.tableView.horizontalHeader().setStyleSheet('QHeaderView::section{background:#66666666}')  # 배경색을 녹색
        # Set the alignment to the headers
        self.tableView.horizontalHeader().setDefaultAlignment(Qt.AlignCenter)
        # 셀 내용 수정불가
        self.tableView.setEditTriggers(QAbstractItemView.NoEditTriggers)
        # hide grid
        self.tableView.setShowGrid(True)
        # row단위 선택
        self.tableView.setSelectionBehavior(QAbstractItemView.SelectRows)
        # 헤더의 내용을 tableView의 크기에 맞춤(아래 3가지 방법)
        self.tableView.horizontalHeader().setStretchLastSection(True)
        # 모든 컬럼의 사이즈를 동일하게 맞춤
        # self.tableView.resizeColumnsToContents()
        # self.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)