import sys
from PySide6.QtCore import QtMsgType
from PySide6.QtWidgets import QApplication, QMainWindow, QStatusBar
from PySide6.QtGui import QIcon
import login_class

class Login(QMainWindow, login_class.Ui_window_login):
    def __init__(self, parent=None):
        super(Login, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Login - Padaria do Seu Zé")
        self.setWindowIcon(QIcon("assets/icon.ico"))
        self.statusbar = QStatusBar()
        self.setStatusBar(self.statusbar)
        self.statusbar.showMessage("Teste de mensagem na barra de status", 5000)

    def __del__(self):
        sys.stdout = sys.__stdout__
        sys.stderr = sys.__stderr__

    def __log(self, msg, level=QtMsgType.QtInfoMsg):
        if level == QtMsgType.QtInfoMsg:
            sys.stdout.write(msg)
        elif level == QtMsgType.QtWarningMsg:
            sys.stderr.write(msg)
        elif level == QtMsgType.QtCriticalMsg:
            sys.stderr.write(msg)
        elif level == QtMsgType.QtFatalMsg:
            sys.stderr.write(msg)
        else:
            sys.stderr.write(msg)

    def __log_info(self, msg):
        self.__log(msg, QtMsgType.QtInfoMsg)

    def __log_warning(self, msg):
        self.__log(msg, QtMsgType.QtWarningMsg)

    def __log_critical(self, msg):
        self.__log(msg, QtMsgType.QtCriticalMsg)

    def __log_fatal(self, msg):
        self.__log(msg, QtMsgType.QtFatalMsg)

    def __log_debug(self, msg):
        self.__log(msg, QtMsgType.QtDebugMsg)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window_login = Login()
    window_login.show()
    sys.exit(app.exec())