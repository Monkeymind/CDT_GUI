from PySide6.QtWidgets import  QLabel,QComboBox,QGroupBox,QHBoxLayout,QPushButton,QDoubleSpinBox,QPlainTextEdit, QVBoxLayout, QWidget
#from datetime import datetime
from comport import comPortConfig
from visaPort import visaPort

class deviceConfig(QWidget):
    def __init__(self, parent=None):
    
        self.power=comPortConfig("Power Supply (Serial)")
        self.load=visaPort("DC Load (VISA)")
        #self.temp=comPortConfig("Temperature")
        
        self.mainVLayOut1=QVBoxLayout()
        self.textOutput=QPlainTextEdit()

        self.chargVoltLabel=QLabel("Voltage")
        self.chargVoltSet=QDoubleSpinBox()
        self.chargVoltSet.setMinimum(0)
        self.chargVoltSet.setMaximum(40)
        self.chargVoltSet.setValue(24.3)
        self.chargVoltSet.setSingleStep(.1)
        self.chargVoltSet.setSuffix(" V")
        self.chargVoltSet.setDecimals(1)
        
        self.bchargVoltSet=QPushButton(text="Set")
        
        self.chargAmpLabel=QLabel("Current")
        self.chargAmpSet=QDoubleSpinBox()
        self.chargAmpSet.setMinimum(0)
        self.chargAmpSet.setMaximum(10)
        self.chargAmpSet.setValue(1)
        self.chargAmpSet.setSingleStep(.1)
        self.chargAmpSet.setSuffix(" A")
        self.chargAmpSet.setDecimals(1)
        
        self.bchargAmpSet=QPushButton(text="Set")

        self.chargAmpThreLabel=QLabel("Threshold")
        self.chargAmpThreSet=QDoubleSpinBox()
        self.chargAmpThreSet.setMinimum(0)
        self.chargAmpThreSet.setMaximum(1)
        self.chargAmpThreSet.setValue(.1)
        self.chargAmpThreSet.setSingleStep(.1)
        self.chargAmpThreSet.setSuffix(" A")
        self.chargAmpThreSet.setDecimals(1)
        
        self.bchargAmpThreSet=QPushButton(text="Set")
       
        self.chargSet1=QHBoxLayout()
        self.chargSet1.addWidget(self.chargVoltLabel)
        self.chargSet1.addWidget(self.chargVoltSet)
        self.chargSet1.addWidget(self.bchargVoltSet)
        
        self.chargSet2=QHBoxLayout()
        self.chargSet2.addWidget(self.chargAmpLabel)
        self.chargSet2.addWidget(self.chargAmpSet)
        self.chargSet2.addWidget(self.bchargAmpSet)

        self.chargSet3=QHBoxLayout()
        self.chargSet3.addWidget(self.chargAmpThreLabel)
        self.chargSet3.addWidget(self.chargAmpThreSet)
        self.chargSet3.addWidget(self.bchargAmpThreSet)

        

        self.chargSetbox=QVBoxLayout()
        self.chargSetbox.addLayout(self.chargSet1)
        self.chargSetbox.addLayout(self.chargSet2)
        self.chargSetbox.addLayout(self.chargSet3)
        
        self.ChargGroup = QGroupBox("Charge Settings")
        self.ChargGroup.setLayout( self.chargSetbox)

        self.disChargModeLabel=QLabel("Mode")
        self.disChargModeSet = QComboBox()
        self.disChargModeSet.addItem('CC')
        self.disChargModeSet.addItem('CV')        
        self.disChargModeSet.addItem('CR')
        self.disChargModeSet.addItem('CP')
        
        self.bDisChargModeSet=QPushButton(text="Set")

        self.disChargVoltLabel=QLabel("Voltage")
        self.disChargVoltSet=QDoubleSpinBox()
        self.disChargVoltSet.setMinimum(0)
        self.disChargVoltSet.setMaximum(40)
        self.disChargVoltSet.setValue(24.3)
        self.disChargVoltSet.setSingleStep(.1)
        self.disChargVoltSet.setSuffix("V")
        self.disChargVoltSet.setDecimals(1)
        self.disChargVoltSet.setEnabled(False)
        
        self.bDisChargVoltSet=QPushButton(text="Set")
        self.bDisChargVoltSet.setEnabled(False)
        
        self.disChargAmpLabel=QLabel("Current")
        self.disChargAmpSet=QDoubleSpinBox()
        self.disChargAmpSet.setMinimum(0)
        self.disChargAmpSet.setMaximum(10)
        self.disChargAmpSet.setValue(1)
        self.disChargAmpSet.setSingleStep(.1)
        self.disChargAmpSet.setSuffix("A")
        self.disChargAmpSet.setDecimals(1)
        self.disChargAmpSet.setEnabled(False)

        self.bDisChargAmpSet=QPushButton(text="Set")
        self.bDisChargAmpSet.setEnabled(False)
       
        self.disChargResLabel=QLabel("Resistor")
        self.disChargResSet=QDoubleSpinBox()
        self.disChargResSet.setMinimum(0)
        self.disChargResSet.setMaximum(10)
        self.disChargResSet.setValue(1)
        self.disChargResSet.setSingleStep(.1)
        self.disChargResSet.setSuffix("R")
        self.disChargResSet.setDecimals(1)
        self.disChargResSet.setEnabled(False)
        
        self.bDisChargResSet=QPushButton(text="Set")
        self.bDisChargResSet.setEnabled(False)
       
        self.disChargPowLabel=QLabel("Power")
        self.disChargPowSet=QDoubleSpinBox()        
        self.disChargPowSet.setMinimum(0)
        self.disChargPowSet.setMaximum(10)
        self.disChargPowSet.setValue(1)
        self.disChargPowSet.setSingleStep(.1)
        self.disChargPowSet.setSuffix("W")
        self.disChargPowSet.setDecimals(1)
        self.disChargPowSet.setEnabled(False)
        
        self.bDisChargPowSet=QPushButton(text="Set")
        self.bDisChargPowSet.setEnabled(False)
        
        self.disChargThreVoltLabel=QLabel("Threshold")
        self.disChargThreVoltSet=QDoubleSpinBox()        
        self.disChargThreVoltSet.setMinimum(.1)
        self.disChargThreVoltSet.setMaximum(30)
        self.disChargThreVoltSet.setValue(18)
        self.disChargThreVoltSet.setSingleStep(.01)
        self.disChargThreVoltSet.setSuffix("V")
        self.disChargThreVoltSet.setDecimals(2)
        self.disChargThreVoltSet.setEnabled(True)
        
        self.bdisChargThreVoltSet=QPushButton(text="Set")
        self.bdisChargThreVoltSet.setEnabled(True)
        
        
      
        self.disChargSet1=QHBoxLayout()
        self.disChargSet1.addWidget(self.disChargModeLabel)
        self.disChargSet1.addWidget(self.disChargModeSet)
        self.disChargSet1.addWidget(self.bDisChargModeSet)
        
        self.disChargSet2=QHBoxLayout()
        self.disChargSet2.addWidget(self.disChargAmpLabel)
        self.disChargSet2.addWidget(self.disChargAmpSet)
        self.disChargSet2.addWidget(self.bDisChargAmpSet)

        self.disChargSet3=QHBoxLayout()
        self.disChargSet3.addWidget(self.disChargVoltLabel)
        self.disChargSet3.addWidget(self.disChargVoltSet)
        self.disChargSet3.addWidget(self.bDisChargVoltSet)
        


        self.disChargSet4=QHBoxLayout()
        self.disChargSet4.addWidget(self.disChargResLabel)
        self.disChargSet4.addWidget(self.disChargResSet)
        self.disChargSet4.addWidget(self.bDisChargResSet)

        self.disChargSet5=QHBoxLayout()
        self.disChargSet5.addWidget(self.disChargPowLabel)
        self.disChargSet5.addWidget(self.disChargPowSet)
        self.disChargSet5.addWidget(self.bDisChargPowSet)
        self.disChargSet6=QHBoxLayout()
        self.disChargSet6.addWidget(self.disChargThreVoltLabel)
        self.disChargSet6.addWidget(self.disChargThreVoltSet)
        self.disChargSet6.addWidget(self.bdisChargThreVoltSet)
        
        self.disChargSetbox=QVBoxLayout()
        self.disChargSetbox.addLayout(self.disChargSet1)
        self.disChargSetbox.addLayout(self.disChargSet2)
        self.disChargSetbox.addLayout(self.disChargSet3)
        self.disChargSetbox.addLayout(self.disChargSet4)
        self.disChargSetbox.addLayout(self.disChargSet5)
        self.disChargSetbox.addLayout(self.disChargSet6)
        
        self.DischargGroup = QGroupBox("Discharge Settings")
        self.DischargGroup.setLayout( self.disChargSetbox)

        self.testTimeIntervalLabel=QLabel("DA Time Interval")
        self.testTimeIntervalSet=QDoubleSpinBox()        
        self.testTimeIntervalSet.setMinimum(0)
        self.testTimeIntervalSet.setMaximum(60)
        self.testTimeIntervalSet.setValue(1)
        self.testTimeIntervalSet.setSingleStep(.1)
        self.testTimeIntervalSet.setDecimals(1)
        self.testTimeIntervalSet.setSuffix(" Seconds")
                
        self.btestTimeIntervalSet=QPushButton(text="Set")

        self.timeIntervalHLayout=QHBoxLayout()
        self.timeIntervalHLayout.addWidget(self.testTimeIntervalLabel)
        self.timeIntervalHLayout.addWidget(self.testTimeIntervalSet)
        self.timeIntervalHLayout.addWidget(self.btestTimeIntervalSet)
        
        self.timeIntervalGroup = QGroupBox("DA Time Interval")
        self.timeIntervalGroup.setLayout( self.timeIntervalHLayout)
        
        
        self.testSetHlayout=QHBoxLayout()
        #self.testSetHlayout.addLayout(self.chargSetbox)
        #self.testSetHlayout.addLayout(self.disChargSetbox)
        self.testSetHlayout.addWidget(self.ChargGroup)
        self.testSetHlayout.addWidget(self.DischargGroup)

        self.mainVLayOut1.addWidget(self.power)
        self.mainVLayOut1.addWidget(self.load)
        self.mainVLayOut1.addLayout(self.testSetHlayout)
      #  self.mainVLayOut1.addWidget(self.temp)
        self.mainVLayOut1.addWidget(self.timeIntervalGroup)
        self.mainVLayOut1.addWidget(self.textOutput)
        
    def disableLoadSetting(self):
          self.bDisChargAmpSet.setEnabled(False)
          self.disChargAmpSet.setEnabled(False)
          self.bDisChargVoltSet.setEnabled(False)   
          self.disChargVoltSet.setEnabled(False)
          self.bDisChargResSet.setEnabled(False)   
          self.disChargResSet.setEnabled(False)
          self.bDisChargPowSet.setEnabled(False) 
          self.disChargPowSet.setEnabled(False)

    def SetButtonEnable(self,command):

          self.bchargVoltSet.setEnabled(command)
          self.bchargAmpSet.setEnabled(command)
          self.bchargAmpThreSet.setEnabled(command)

          self.bDisChargModeSet.setEnabled(command)
          self.bDisChargVoltSet.setEnabled(command)   
          self.bDisChargAmpSet.setEnabled(command)
          self.bDisChargResSet.setEnabled(command)             
          self.bDisChargPowSet.setEnabled(command) 
          self.bdisChargThreVoltSet.setEnabled(command) 

          self.btestTimeIntervalSet.setEnabled(command)
          
         
    