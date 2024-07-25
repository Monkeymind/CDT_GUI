from plotbox import plotBox
from PySide6.QtWidgets import QRadioButton,QComboBox,QDoubleSpinBox,QLabel,QLineEdit,QPushButton, QVBoxLayout, QHBoxLayout,QGroupBox
from PySide6.QtCore import Qt,QRect

class battTestPage():
    def __init__(self, parent=None):
        #super().__init__(parent)
        #self.bserUpdate = QPushButton(text="Update",parent=self)
       
        self.vPlot=plotBox("Voltage")
        self.cPlot=plotBox("Current")


        self.batterySlnoLabel=QLabel("Battery Sl.no")
        self.batterySlno=QLineEdit()
        
        self.testEngLabel=QLabel("Test Engineer")
        self.testEng=QLineEdit()
  
        self.testDetailHlayout=QHBoxLayout()
        self.testDetailHlayout.addWidget(self.batterySlnoLabel)
        self.testDetailHlayout.addWidget(self.batterySlno)
        self.testDetailHlayout.addWidget(self.testEngLabel)
        self.testDetailHlayout.addWidget(self.testEng)

              
        self.battDetailsBox = QGroupBox("Test Details")
        #self.chrgBox.setAlignment(Qt.AlignCenter)
        self.battDetailsBox.setLayout(self.testDetailHlayout)
      



        self.rChargDisc=QRadioButton("Charge then Discharge")
        self.rChargDisc.setChecked(True)
        self.rDiscCharg=QRadioButton("Discharge then Charge")


        self.radioHLayout=QHBoxLayout()
        self.radioHLayout.addWidget(self.rChargDisc)
        self.radioHLayout.addWidget(self.rDiscCharg)
        
        self.TestOrderGroup = QGroupBox("Test Order")
        self.TestOrderGroup.setLayout(self.radioHLayout)


        self.rloopRadio=QRadioButton("Loop Test")
        self.rloopRadio.setChecked(False)

        self.noOfCycleSpinBox=QDoubleSpinBox()        
        self.noOfCycleSpinBox.setMinimum(0)
        self.noOfCycleSpinBox.setMaximum(30)
        self.noOfCycleSpinBox.setValue(1)
        self.noOfCycleSpinBox.setSingleStep(1)
        self.noOfCycleSpinBox.setDecimals(0)
        self.noOfCycleSpinBox.setSuffix(" Cycle")
  
        
        self.cyclecHLayout=QHBoxLayout()
        self.cyclecHLayout.addWidget(self.rloopRadio)
        self.cyclecHLayout.addWidget(self.noOfCycleSpinBox)

        self.cycleBoxGroup = QGroupBox("Test Cycle")
        self.cycleBoxGroup.setLayout(self.cyclecHLayout)
        
        self.bMasterTest = QPushButton(text="Test Start")
        self.bMasterTest.setFixedSize(100,40)
        self.bMasterTest.setStyleSheet("background-color : Green")
        
        self.testInputHbox=QHBoxLayout()
        self.testInputHbox.addWidget(self.TestOrderGroup)
        self.testInputHbox.addWidget(self.cycleBoxGroup)
        self.testInputHbox.addWidget(self.bMasterTest)

  


        self.bChargTest = QPushButton(text="Start")
        self.bChargTest.setFixedSize(120,30)
        self.bChargTest.setStyleSheet("background-color: green")
        
        self.dVolt=QLineEdit()
        self.dVolt.setPlaceholderText("0.0 V")
        self.dVolt.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.dVolt.setFixedSize(120,20)
        
        self.dAmp=QLineEdit()
        self.dAmp.setPlaceholderText("0.0 A")
        self.dAmp.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.dAmp.setFixedSize(120,20)
        
        self.dCapcity=QLineEdit()
        self.dCapcity.setPlaceholderText("0.0 mAh")
        self.dCapcity.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.dCapcity.setFixedSize(120,20)

        self.dtestState = QLineEdit()
        self.dtestState.setPlaceholderText("Battery State")
        self.dtestState.setAlignment(Qt.AlignBottom | Qt.AlignRight)

        self.dTimeShow = QLineEdit()
        self.dTimeShow.setPlaceholderText("Time")
        self.dTimeShow.setAlignment(Qt.AlignBottom | Qt.AlignRight)


        self.meterHlayout=QHBoxLayout()
        self.meterHlayout.addWidget(self.dVolt,alignment=Qt.AlignHCenter)
        self.meterHlayout.addWidget(self.dAmp,alignment=Qt.AlignHCenter)
        self.meterHlayout.addWidget(self.dCapcity,alignment=Qt.AlignHCenter)
        self.meterHlayout.addWidget(self.dtestState,alignment=Qt.AlignHCenter)
        self.meterHlayout.addWidget(self.dTimeShow,alignment=Qt.AlignHCenter)
        
        self.meterBox = QGroupBox("Test Parameter")
        #self.chrgBox.setAlignment(Qt.AlignCenter)
        self.meterBox.setLayout(self.meterHlayout)

                  
      


            
    
        self.voltHlayout=QVBoxLayout()
        self.voltHlayout.addWidget(self.vPlot)

        self.currHlayout=QVBoxLayout()
        self.currHlayout.addWidget(self.cPlot)

        self.plotHlayout=QHBoxLayout()
        self.plotHlayout.addLayout(self.voltHlayout)
        self.plotHlayout.addLayout(self.currHlayout)

        self.plotBox = QGroupBox("Graph")
        #self.chrgBox.setAlignment(Qt.AlignCenter)
        self.plotBox.setLayout(self.plotHlayout)

        self.mainVLayOut2=QVBoxLayout()        
        self.mainVLayOut2.addWidget(self.battDetailsBox)
        self.mainVLayOut2.addLayout(self.testInputHbox)
        # self.mainVLayOut2.addWidget(self.TestOrderGroup)
        # self.mainVLayOut2.addWidget(self.cycleBoxGroup)
        self.mainVLayOut2.addWidget(self.meterBox)
        self.mainVLayOut2.addWidget(self.plotBox)
        self.mainVLayOut2.setAlignment(Qt.AlignCenter)


    def testStart(self):
        self.bMasterTest.setText("Test End")
        self.bMasterTest.setStyleSheet("background-color: red")
        
    def testEnd(self):
        self.bMasterTest.setText("Test Start")
        self.bMasterTest.setStyleSheet("background-color: green")
        

    def battTestPageClear(self):
        self.batterySlno.clear()
        self.testEng.clear()
        self.dVolt.clear()
        self.dAmp.clear()
        self.dCapcity.clear()
        self.dtestState.clear()
        self.dTimeShow.clear()

