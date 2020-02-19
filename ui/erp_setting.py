from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox

from database_init.ddl_sql import DbInit


class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi("../ui/setting.ui")
        self.ui.btn_init.clicked.connect(self.btn_clicked)
        self.ui.show()

    def btn_clicked(self):
        try:
            db = DbInit(filename='../database_init/sql.ini')
            db.init()
            QMessageBox.about(self, "초기화 완료", "데이터베이스 및 테이블 유저생성 완료")
        except Exception as err:
            QMessageBox.about(self, "초기화 실패", "데이터베이스 및 테이블 유저생성 실패")


if __name__ == '__main__':
    app = QApplication([])
    w = MyApp()
    app.exec()