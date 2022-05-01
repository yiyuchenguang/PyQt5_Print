import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QDialog
from PyQt5.QtGui import QTextCursor
from PyQt5.QtCore import QObject, pyqtSignal

from main_ui import Ui_MainWindow
from sub_diaglou_ui import Ui_Dialog
from nprintf import nprintf


temp = sys.stdout
class Stream(QObject):
    newText = pyqtSignal(str)
    def write(self, text):
        self.newText.emit(str(text))
        QApplication.processEvents()


class ShowDialog(QDialog, Ui_Dialog):  # Python多继承
    def __init__(self, parent=None):
        super(ShowDialog, self).__init__(parent)
        self.setupUi(self)  # 调用写在视图层文件的页面布局函数

    def closeEvent(self, event):
        nprintf("closed dialog")

class MainQt(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        '''流重定向'''
        sys.stdout = Stream(newText=self.onUpdateEdit)
        self.pushButton.clicked.connect(self.print_test)
        self.pushButton_2.clicked.connect(self.show_diaglog)

    def print_test(self):
        nprintf("这是文件main.py")
        from becalled_a import print_a
        from becalled_b import print_b
        print_a()
        print_b()

    def show_diaglog(self):
        nprintf("call sub panel")
        dlg = ShowDialog(self)
        dlg.exec_()


        '''关闭app事件响应'''
    def closeEvent(self, event):
        """Shuts down application on close."""
        # Return stdout to defaults.
        self.ms.close()
        sys.stdout = temp
        super().closeEvent(event)

    '''绑定输出流'''

    def onUpdateEdit(self, text):
        cursor = self.textEdit.textCursor()
        cursor.movePosition(QTextCursor.End)
        cursor.insertText(text)
        self.textEdit.setTextCursor(cursor)
        self.textEdit.ensureCursorVisible()

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    mian_ui = MainQt()
    mian_ui.show()
    sys.exit(app.exec_())