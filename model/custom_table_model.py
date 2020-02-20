from PyQt5.QtCore import QAbstractTableModel, QVariant, Qt


class CustomTableModel(QAbstractTableModel):
    def __init__(self, data=None, header=None):
        super().__init__()
        self.data = data or [()]
        self.header = header or [()]

    def rowCount(self, parent):
        return len(self.data)

    def columnCount(self, parent):
        return len(self.data[0])

    def data(self, index, role):
        if not index.isValid():
            return QVariant()
        if role == Qt.TextAlignmentRole:
            if 0 == index.column() :
                return Qt.AlignCenter
            if 1 == index.column() :
                return Qt.AlignVCenter | Qt.AlignLeft
        if role != Qt.DisplayRole:
            return QVariant()

        return self.data[index.row()][index.column()]

    def headerData(self, col, orientation, role):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return QVariant(self.header[col])
        return QVariant()
