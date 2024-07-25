import serial.tools.list_ports
from PySide6.QtCore import Qt
from PySide6.QtWidgets import  QLineEdit,QGroupBox,QComboBox,QLabel,QGridLayout,QPushButton


class comPortConfig(QGroupBox):
    def __init__(self,name):
        super().__init__()

        self.comPort=None

        self.titleName=name
        self.setTitle(self.titleName)
        self.bserUpdate = QPushButton(text="Update",parent=self)
        self.bserUpdate.setFixedSize(100, 30)
        self.SerList=QComboBox()
        self.SerList.setFixedSize(500, 30)
        self.bPortConnect = QPushButton(text="Connect",parent=self)
        self.bPortConnect.setFixedSize(100, 30)
        self.bPortConnect.setStyleSheet("background-color: green")
        #self.bPortConnect.setFrameStyle(QFrame.Panel | QFrame.Raised)
        self.lBaudrate=QLabel(text="BaudRate: 9600",parent=self)
        self.lBaudrate.setFixedWidth(90)
        
        self.serHlayOut=QGridLayout(self)
        self.serHlayOut.addWidget(self.bserUpdate,0,0)
        self.serHlayOut.addWidget(self.SerList,0,1)
        self.serHlayOut.addWidget(self.lBaudrate,0,2)
        self.serHlayOut.addWidget(self.bPortConnect,0,3)

        self.commandText=QLabel(text="Command:",parent=self)
        self.deviceCommand=QLineEdit()
        self.deviceCommand.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.deviceCommand.setFixedSize(500,30)
       # self.deviceCommand.setReadOnly(True)
        
        self.send = QPushButton(text="Send",parent=self)
        self.send.setFixedSize(100, 30)
        

        self.serHlayOut.addWidget(self.commandText,1,0)
        self.serHlayOut.addWidget(self.deviceCommand,1,1)
        self.serHlayOut.addWidget(self.send,1,2)

        #self.comPort=None
        self.portlist =serial.tools.list_ports.comports()
       # print(self.portlist)
        print("---------"+name+"------------")
        for comNum in range(len(self.portlist)):
            print(str(comNum+1)+"- "+str(self.portlist[comNum]))
            self.SerList.addItem(str(self.portlist[comNum]))
    def updatePortList(self):
        print("updatePortList")
        self.portlist.clear()
        self.SerList.clear()
        self.portlist =serial.tools.list_ports.comports()
        for comNum in range(len(self.portlist)):
            print(str(comNum+1)+"- "+str(self.portlist[comNum].description))
            self.SerList.addItem(str(self.portlist[comNum]))
    
    def portConnect(self):
        #self.comPort="a"
        if self.bPortConnect.text() == "Connect":
            self.index=self.SerList.currentIndex()
            print(str(self.index))
            try:
                #self.comPort=serial.Serial('com17',9600,timeout=.1,parity="N",stopbits=1)
                self.comPort=serial.Serial(port=(self.portlist[self.index].device),timeout=.01)
                #self.comPort.open()
                print(self.comPort.name)
                self.bPortConnect.setText("Disconnect")
                self.bPortConnect.setStyleSheet("background-color: red")
                
                print(self.portlist[self.index].device +"- Port Connected")
                
                
            except:
                print("Port Connect Func error")
                
                

        else:
            self.comPort.close()
            self.comPort=None
            self.bPortConnect.setText("Connect")
            self.bPortConnect.setStyleSheet("background-color: green")  

    def portDisconnect(self):        
        self.comPort.close()
        
        self.bPortConnect.setText("Connect")
        self.bPortConnect.setStyleSheet("background-color: green")
        
                        


   