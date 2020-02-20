from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox

from database_init.ddl_sql import DbInit
from restore_backup.restore_sql import BackupRestore


class MyApp(QWidget):
    def __init__(self):
        self.ui = uic.loadUi("ui/setting.ui")
        self.db_init = DbInit(filename='../resources/sql.ini')
        self.backup_restore = BackupRestore(db_conf='../resources/user_properties.ini')
        self.init_ui()

    def init_ui(self):
        self.ui.btn_init.clicked.connect(self.btn_init)
        self.ui.btn_import.clicked.connect(self.btn_import)
        self.ui.btn_backup.clicked.connect(self.btn_backup)
        self.ui.show()

    def btn_init(self):
        print("btn_init()")
        try:
            self.db_init.init()
            QMessageBox.about(self, "초기화 완료", "데이터베이스 및 테이블 유저생성 완료")
        except Exception as err:
            QMessageBox.about(self, "초기화 실패", "데이터베이스 및 테이블 유저생성 실패")

    def btn_import(self):
        print("btn_import()")
        try:
            self.backup_restore.backup_data()
            QMessageBox.about(self, "로드 완료", "데이터 로드 완료")
        except Exception as err:
            QMessageBox.about(self, "로드 실패", "데이터 로드 실패")

    def btn_backup(self):
        print("btn_backup()")
        try:
            self.backup_restore.load_data(query='update employee set pic=%s where emp_no=%s')
            QMessageBox.about(self, "백업 완료", "데이터 백업 완료")
        except Exception as err:
            QMessageBox.about(self, "백업 실패", "데이터 백업 실패")


if __name__ == '__main__':
    app = QApplication([])
    w = MyApp()
    app.exec()

    # db_init = DbInit(filename='../resources/sql.ini')
    # db_init.init()
    #
    # backup_restore = BackupRestore(db_conf='../resources/user_properties.ini')
    # backup_restore.backup_data()
    # backup_restore.load_data()