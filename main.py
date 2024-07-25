from PySide6.QtWidgets import QApplication
from baseFrame import baseFrame
import sys
if __name__ == '__main__':
   
    app= QApplication(sys.argv)    
    window =baseFrame()
    #window.show()
    #threadpool = QThreadPool()
    app.exec()
    




