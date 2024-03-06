import maya.cmds as cmds
import maya.OpenMayaUI as omui
from PySide2 import QtCore, QtWidgets, QtGui
from shiboken2 import wrapInstance

def maya_main_window():
    main_window_ptr = omui.MQtUtil.mainWindow()
    return wrapInstance(int(main_window_ptr), QtWidgets.QWidget)

class EDeleteConfirmWindow(QtWidgets.QDialog):

    def __init__(self, parent=maya_main_window()):
        super(EDeleteConfirmWindow, self).__init__(parent)

        self.setWindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.Tool)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground, True)

        self.setWindowOpacity(0.9)
        self.installEventFilter(self)

        self.frame = QtWidgets.QWidget(self)
        self.frame.setStyleSheet("""
            QWidget {
                background-color: rgba(38, 38, 38, 240);
                border-radius: 10px;
                min-width: 150px;
                min-height: 90px;
            }
        """)

        self.main_layout = QtWidgets.QVBoxLayout(self.frame)
        self.setLayout(self.main_layout)

        font = QtGui.QFont()
        font.setBold(True)
        font.setPointSize(12)

        self.label = QtWidgets.QLabel("Delete?")
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.main_layout.addWidget(self.label)

        self.button_layout = QtWidgets.QHBoxLayout()
        self.main_layout.addLayout(self.button_layout)

        self.yes_button = QtWidgets.QPushButton("Yes")
        self.yes_button.setStyleSheet("""
            QPushButton {
                background-color: rgba(10, 10, 10, 240);
                border-radius: 10px;
                min-width: 60px;
                min-height: 30px;
            }
        """)
        self.yes_button.clicked.connect(self.yes_button_clicked)
        self.button_layout.addWidget(self.yes_button)

        self.no_button = QtWidgets.QPushButton("No")
        self.no_button.setStyleSheet("""
            QPushButton {
                background-color: rgba(10, 10, 10, 240);
                border-radius: 10px;
                min-width: 60px;
                min-height: 30px;
            }
        """)
        self.no_button.clicked.connect(self.close)
        self.button_layout.addWidget(self.no_button)

        self.adjustSize()

        cursor = QtGui.QCursor()
        self.move(cursor.pos() - self.rect().center())

        self.show()

        yes_button_center = self.yes_button.mapToGlobal(self.yes_button.rect().center())
        cursor.setPos(yes_button_center)


    def yes_button_clicked(self):
        cmds.delete()
        self.close()


    def eventFilter(self, object, event):
        if event.type() == QtCore.QEvent.Leave:
            self.close()
        return False

def create_popup_window():
    global popup_window
    if popup_window is not None and popup_window.isVisible():
        popup_window.close()
    popup_window = EDeleteConfirmWindow()

popup_window = None

create_popup_window()
