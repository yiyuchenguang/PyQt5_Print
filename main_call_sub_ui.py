from PyQt5.QtWidgets import QMainWindow, QApplication, QDialog
from main_ui import Ui_MainWindow
from sub_diaglou_ui import Ui_Dialog

class ShowDialog(QDialog, Ui_Dialog): # 子面板
    def __init__(self, parent=None):
        super(ShowDialog, self).__init__(parent)
        self.setupUi(self)  # 调用写在视图层文件的页面布局函数

    def closeEvent(self, event):
        print("closed dialog")


class MainQt(QMainWindow,Ui_MainWindow): # 主面板
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton_2.clicked.connect(self.show_diaglog)

    def show_diaglog(self):
        print("call sub panel")
        dlg = ShowDialog(self)
        dlg.exec_()

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    mian_ui = MainQt()
    mian_ui.show()
    sys.exit(app.exec_())