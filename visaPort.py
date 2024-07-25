import pyvisa
from PySide6.QtWidgets import QComboBox,QLineEdit,QLabel,QGridLayout,QGroupBox,QPushButton
from PySide6.QtCore import Qt


class visaPort(QGroupBox):
    def __init__(self,name):
        super().__init__()
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
    
        # try:
        self.rm = pyvisa.ResourceManager()
        self.visaPort = None
        print(self.rm)
        # except:
        #     self.rm=None
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

        self.portlist=list(self.rm.list_resources())
        for comNum in range(len(self.portlist)):
            print(str(comNum+1)+"- "+str(self.portlist[comNum]))
            self.SerList.addItem(str(self.portlist[comNum]))
    def updatePortList(self):
        print("updatePortList  VISA")
        self.portlist.clear()
        self.SerList.clear()
        self.portlist =list(self.rm.list_resources())
        for comNum in range(len(self.portlist)):
            print(str(comNum+1)+"- "+str(self.portlist[comNum]))
            self.SerList.addItem(str(self.portlist[comNum]))

    def portConnect(self):
        
        portName=self.portlist[self.SerList.currentIndex()]
        if self.bPortConnect.text() == "Connect":
            try:
              
                self.visaPort = self.rm.open_resource(portName)
                self.visaPort.write_termination = '\n'
                self.visaPort.read_termination = '\n'
                self.bPortConnect.setText("Disconnect")
                self.bPortConnect.setStyleSheet("background-color: red")                
                print("{} Visa port connected".format(portName))

            except:
                print("Visa portConnect: Fail to Connect")
        else:
            self.visaPort.close()
            self.visaPort=None
            self.bPortConnect.setText("Connect")
            self.bPortConnect.setStyleSheet("background-color: green")  
            print("VISA portConnect: DisConnected")

