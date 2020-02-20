from abc import ABCMeta, abstractmethod

from PyQt5.QtCore import QAbstractTableModel, QVariant, Qt


class AbstractTableModel(QAbstractTableModel):
    def __init__(self, data=None, header=None):
        super().__init__()
        self.data = data or [()]
        self.header = header or [()]

    def rowCount(self, parent):
        return len(self.data)

    def columnCount(self, parent):
        return len(self.data[0])

    @abstractmethod
    def data(self, index, role):
        raise NotImplementedError("Subclass must implement abstract method")
        # if not index.isValid():
        #     return QVariant()
        # if role == Qt.TextAlignmentRole:
        #     if 0 == index.column() :
        #         return Qt.AlignCenter
        #     if 1 == index.column() :
        #         return Qt.AlignVCenter | Qt.AlignLeft
        # if role != Qt.DisplayRole:
        #     return QVariant()
        # return self.data[index.row()][index.column()]

    def headerData(self, col, orientation, role):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return QVariant(self.header[col])
        return QVariant()
