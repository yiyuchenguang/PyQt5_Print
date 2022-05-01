
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QTextCursor
from PyQt5.QtCore import QObject, pyqtSignal

from main_ui import Ui_MainWindow
from nprintf import nprintf

temp = sys.stdout
class Stream(QObject):
    newText = pyqtSignal(str)
    def write(self, text):
        self.newText.emit(str(text))
        # 实时刷新界面
        QApplication.processEvents()

class MainQt(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        '''流重定向'''
        sys.stdout = Stream(newText=self.onUpdateEdit)
        self.pushButton.clicked.connect(self.print_test)

    def print_test(self):
        #self.textEdit.setText("adasdada")
        nprintf("这是文件main.py")
        from becalled_a import print_a
        from becalled_b import print_b
        print_a()
        print_b()
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