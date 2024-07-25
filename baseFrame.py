from battTestPage import battTestPage
from deviceConfigPage import deviceConfig
from PySide6.QtGui import QFont,QIcon
from PySide6.QtWidgets import  QVBoxLayout, QWidget,QMessageBox,QTabWidget,QRadioButton,QFrame
from PySide6.QtCore import QRunnable, Slot, Signal, QObject, QThreadPool,Qt,QTimer
import time
import qdarktheme
from datetime import datetime
import traceback
import sys
import csv
import os

from datetime import datetime
class WorkerSignals(QObject):
 
    finished = Signal()
    error = Signal(tuple)
    result = Signal(object)
    progress = Signal(int)




class Worker(QRunnable):


    def __init__(self, fn, *args, **kwargs):
        super(Worker, self).__init__()

        # Store constructor arguments (re-used for processing)
        self.fn = fn
        self.args = args
        self.kwargs = kwargs
        self.signals = WorkerSignals()

        # Add the callback to our kwargs
        self.kwargs['progress_callback'] = self.signals.progress

    @Slot()
    def run(self):

        try:
            result = self.fn(*self.args, **self.kwargs)
        except:
            traceback.print_exc()
            exctype, value = sys.exc_info()[:2]
            self.signals.error.emit((exctype, value, traceback.format_exc()))
        else:
            self.signals.result.emit(result)  # Return the result of the processing
        finally:
            self.signals.finished.emit()  # Done


class baseFrame(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        qdarktheme.setup_theme()
       
        
        # self.timer = QTimer()
        # self.timer.setInterval(1000)
        # self.timer.timeout.connect(self.recurring_timer)
        # self.timer.start()

        # Button with a parent widget
        # page config
   
      # Window config
        self.setWindowTitle("ATE Battery b3.0")
        self.font = QFont('SF Pro Display', 12)
        self.font.setWeight(QFont.Weight.DemiBold) # 900
        self.setWindowIcon(QIcon("E:\PYQT_DUT1\ate.ico"))       
        
        self.daTimeInterval=None
        self.TestRunning=None
        self.msg_box = QMessageBox() 
        self.msg_box.setIcon(QMessageBox.Warning)

        self.preTestCondition=None
        
        self.cycleDirection=True
        self.noOfCycle=0
     
        self.loopCycle=False
        self.cycleCount=0

        self.voltList=[]
        self.ampList=[]
        self.capcityList=[]
        self.timeStampList=[]
        self.xAxisList=[]
        self.battStateList=[]
        self.capacityList=[]
       
        self.device=deviceConfig()
        self.battTest=battTestPage()
        #self.count=0
        self.chargCurrThreshold=2.0
        self.discVoltThreshold=18

        self.main1=QWidget()
        self.main1.setLayout(self.device.mainVLayOut1) 

        self.main2=QWidget()
        self.main2.setLayout(self.battTest.mainVLayOut2)    

        self.tabLayout=QTabWidget()
        self.tabLayout.addTab(self.main1,"Device Congiguration")
        self.tabLayout.addTab(self.main2,"Battery Test")

        self.mainVLayOut=QVBoxLayout()   
        self.mainVLayOut.addWidget(self.tabLayout)
        self.setLayout(self.mainVLayOut)
        
         # Button config
        self.device.power.send.clicked.connect(self.serialCommandCommon)
        self.device.load.send.clicked.connect(self.visaCommandCommon)
        
        self.device.power.bserUpdate.clicked.connect(self.device.power.updatePortList)
        self.device.power.bPortConnect.clicked.connect(self.device.power.portConnect)
        self.device.load.bserUpdate.clicked.connect(self.device.load.updatePortList)
        self.device.load.bPortConnect.clicked.connect(self.device.load.portConnect)
        self.device.bchargVoltSet.clicked.connect(self.psChargVoltSet)
        self.device.bchargAmpSet.clicked.connect(self.psChargAmpSet)
        self.device.bchargAmpThreSet.clicked.connect(self.psChargThresholdAmpSet)
        
        
        self.device.bDisChargModeSet.clicked.connect(self.loadMode)
        self.device.bDisChargVoltSet.clicked.connect(self.loadVoltSet)
        self.device.bDisChargAmpSet.clicked.connect(self.loadAmpSet)
        self.device.bDisChargResSet.clicked.connect(self.loadResSet)
        self.device.bDisChargPowSet.clicked.connect(self.loadPowSet)
        self.device.bdisChargThreVoltSet.clicked.connect(self.loadThreVoltSet)
        self.device.btestTimeIntervalSet.clicked.connect(self.testIntervalTimeSet)

        
        self.battTest.rChargDisc.clicked.connect(self.orderTestSet)
        self.battTest.rDiscCharg.clicked.connect(self.orderTestSet)
        self.battTest.rloopRadio.clicked.connect(self.loopRadioSet)
        self.battTest.noOfCycleSpinBox.valueChanged.connect(self.noOfCycleSet)
        self.battTest.bMasterTest.clicked.connect(self.batteryMasterTest)

      
        self.show()
        

        self.threadpool = QThreadPool()
    
  
        
    def batteryMasterTest(self):
        print("batteryCDTest")
        if self.TestRunning:
            print("ending test")
            self.TestRunning=False
            self.cycleCount=self.noOfCycle
            self.loopCycle=False
            return
        
        self.preTestCheck()
        if not self.daTimeInterval:
            self.daTimeInterval=1
            print("defualt TimeInterval=1 set")
        if self.preTestCondition:
            print("Time Interval set ="+str(self.daTimeInterval))
     
            if not self.TestRunning:
                self.battTest.testStart()
                self.device.SetButtonEnable(False)
                self.TestRunning=True
                self.count=1
                if(not self.loopCycle) and (not self.noOfCycle):
                    self.noOfCycle=1

                worker = Worker(self.batteryTestLoop) # Any other args, kwargs are passed to the run function                             
                worker.signals.progress.connect(self.GraphUpdate)
                worker.signals.result.connect(self.TestResult)   
                worker.signals.finished.connect(self.TestThreadEnd)
                self.threadpool.start(worker)
            
              


    def batteryTestLoop(self,progress_callback):
        print("Loop Cycle: ",self.loopCycle)
        print("cycleCount: ",self.cycleCount)
        print("noOfCycle: ",self.noOfCycle)
        while (self.cycleCount<=self.noOfCycle) or (self.loopCycle):
            if self.cycleDirection:
                self.chargeTest(progress_callback)
                self.disChargeTest(progress_callback)
        
            else:
                self.disChargeTest(self,progress_callback)
                self.chargeTest(self,progress_callback)
            self.cycleCount=self.cycleCount+1


   
    def chargeTest(self, progress_callback):
        self.visaWrite("INP OFF")  # DC LOAD OFF
        time.sleep(1)
        self.comWrite("OUT1")      # Power SupplyOn
        time.sleep(1)
        self.battTest.dtestState.setText("Charge State")
        print("chargeTestLoop")       
        self.psChargV=self.comRead("VOUT1?")
        self.psChargA=self.comRead("IOUT1?")
        while self.psChargA > self.chargCurrThreshold:
            if self.TestRunning:   # To end Test
                
                self.voltList.append(self.psChargV)
                self.ampList.append(self.psChargA)
                self.timeStampList.append(str(datetime.now().strftime("%Y-%m-%d %H:%M:%S:%f")))
                self.xAxisList.append(self.count)
                self.battStateList.append("Charge")
                self.count=self.count+1
                print("Charg Count: ",self.count)
                
                
                time.sleep(self.daTimeInterval)
                
               
                self.psChargV=self.comRead("VOUT1?")
                self.psChargA=self.comRead("IOUT1?")
                
                progress_callback.emit(self.count)
            else:
                break
      
        return "Done."
    

    def disChargeTest(self, progress_callback):

        self.comWrite("OUT0")      # Power SupplyOFF
        time.sleep(1)
        self.visaWrite("INP ON")  # DC LOAD ON
        time.sleep(1)
        self.battTest.dtestState.setText("Discharge State")
        print("disChargeTestLoop")       
    
        self.ldDiscVolt=self.visaRead("MEAS:VOLT?")
        self.ldDiscAmp=self.visaRead("MEAS:CURR?")

        while self.ldDiscVolt > self.discVoltThreshold:
            if self.TestRunning:
        
                self.voltList.append(self.ldDiscVolt)
                self.ampList.append(self.ldDiscAmp)
                self.xAxisList.append(self.count)
                self.timeStampList.append(str(datetime.now().strftime("%Y-%m-%d %H:%M:%S:%f")))
                
                self.count=self.count+1
                
                print("Disc Count",self.count)
                time.sleep(self.daTimeInterval)
                
                self.ldDiscVolt=self.visaRead("MEAS:VOLT?")
     
     
                self.ldDiscAmp=self.visaRead("MEAS:CURR?")
                
                print(self.voltList)
                print(self.ampList)
                print(self.xAxisList)
                print(datetime.now())                       
                progress_callback.emit(self.count)
            else:
                break
      
        return "Done."
   


    def GraphUpdate(self, n):
        print("Prograss count: {}".format(self.count))
        print(n)

        self.battTest.dVolt.setText(str(self.voltList[len(self.voltList)-1])+" V")
        self.battTest.dAmp.setText(str(self.ampList[len(self.ampList)-1])+" A")
        self.battTest.dTimeShow.setText(str(datetime.now().strftime("%H:%M:%S:%f")))
        self.battTest.vPlot.graph.plot(self.xAxisList,self.voltList,linewidth=10,pen={'color':'b', 'width':2})
        self.battTest.cPlot.graph.plot(self.xAxisList,self.ampList,linewidth=10,pen={'color':'k', 'width':2})
        print("volt ",self.voltList)
        print("Amp ",self.ampList)      
         

    def TestResult(self, s):
        print("Battery Charge Test Completed")

    def TestThreadEnd(self): 
        self.comWrite("OUT0")
        self.visaWrite("INP OFF")
        self.CsvExport()

        self.voltList.clear()
        self.ampList.clear()
        self.capacityList.clear()
        self.xAxisList.clear()
        self.battStateList.clear()
        self.battStateList.clear()    
        self.cycleCount=0
        self.loopCycle=True
        self.battTest.testEnd()

        self.messageAlert("CSV File","Charge Test Downloaded")
        self.battTest.vPlot.graph.clear()
        self.battTest.cPlot.graph.clear()        
        self.battTest.battTestPageClear()
        self.device.SetButtonEnable(True)
      
        print("THREAD COMPLETE!")
        
       
         
    def preTestCheck(self):
        if not self.device.power.comPort:
            print("No Com Port Connected")
            self.messageAlert("Power Supply","No COM Port Connected")
            
            self.preTestCondition=False
        elif not self.device.load.visaPort:
            print("No Visa Port Connected")
            self.messageAlert("Electronic Load","No Visa Port Connected")
            
            self.preTestCondition=False
        elif not self.battTest.batterySlno.text():
            self.messageAlert("Battery Sl.no", "Enter Battery Sl. No")  
            self.preTestCondition=False
            print("no batterySlno")
        elif not self.battTest.testEng.text():
            self.messageAlert("Test Engineer", "Enter Test Engineer Name")  
            self.preTestCondition=False
            print("No testEng Name ")
        else:
            print("preTestCheck ok")
            self.preTestCondition=True






    def comRead(self, command):
        if not self.device.power.comPort:
            print("no Port")
            return None
        bCommand =bytes(command,'ascii')
        self.device.power.comPort.write(bCommand)
        self.device.power.comPort.flush()
    
        rx = ''
        time.sleep(1)
        rx=self.device.power.comPort.readline().strip().decode() #decode('ascii') 
        rx=round(float(rx),2)      
        return rx
    
    def comWrite(self, command):
        if not self.device.power.comPort:
            print("no Port")
            return None
        bCommand =bytes(command,'ascii')
        self.device.power.comPort.write(bCommand)
        self.device.power.comPort.flush()

    def visaWrite(self,command):
        self.device.load.visaPort.write(command)

    def visaRead(self,command):
        print("Visa Read")
        rx= self.device.load.visaPort.query(command)
        print("visaRea= {}".format(rx))
        return float(rx.strip())
    
    def messageAlert(self,title,text):
        self.msg_box.setWindowTitle(title)
        self.msg_box.setText(text)  
        self.msg_box.exec_()

    def psChargVoltSet(self):
        if not self.device.power.comPort:            
            self.messageAlert("Power Supply","No COM Port Connected")
            self.device.chargTestEnd()
            return None
        
        chargVolt=self.device.chargVoltSet.value()
        command="VSET1:"+str(chargVolt)
        self.comWrite(command)
        print(command)
    
    def psChargAmpSet(self):
        if not self.device.power.comPort:
            print("No Com Port Connected")
            self.messageAlert("Power Supply","No COM Port Connected")
            self.device.chargTestEnd()
            return None
        chargAmp=self.device.chargAmpSet.value()
        command="ISET1:"+str(chargAmp)
        self.comWrite(command)
        print(command)
    
    def psChargThresholdAmpSet(self):
        if not self.device.power.comPort:
            print("No Com Port Connected")
            self.messageAlert("Power Supply","No COM Port Connected")
            self.device.chargTestEnd()
            return None
        ampThreshold=self.device.chargAmpThreSet.value()
        self.chargCurrThreshold=ampThreshold
        
        print("Amp Thres= "+str(self.chargCurrThreshold))

    def loadMode(self):
        if not self.device.load.visaPort:
            print("No Visa Port Connected")
            self.messageAlert("Electronic Load","No Visa Port Connected")
            
            return None
        mode=self.device.disChargModeSet.currentIndex()
 
        if mode==0:
            self.visaWrite("MODE:CC")
            self.device.disableLoadSetting()
            self.device.bDisChargAmpSet.setEnabled(True)
            self.device.disChargAmpSet.setEnabled(True)
         
        if mode==1:

            self.visaWrite("MODE:CV")
            self.device.disableLoadSetting()
            self.device.bDisChargVoltSet.setEnabled(True)   
            self.device.disChargVoltSet.setEnabled(True) 
        if mode==2:
            self.visaWrite("MODE:CR")
            self.device.disableLoadSetting()
            self.device.bDisChargResSet.setEnabled(True)   
            self.device.disChargResSet.setEnabled(True) 
        if mode==3:
            self.visaWrite("MODE:CP")
            self.device.disableLoadSetting()
            self.device.bDisChargPowSet.setEnabled(True)   
            self.device.disChargPowSet.setEnabled(True) 

    def loadVoltSet(self):
        if not self.device.load.visaPort:            
            self.messageAlert("Electronic Load","No Visa Port Connected")           
            return None       
        command="VOLT "+str(self.device.disChargVoltSet.value())
        self.visaWrite(command)
       

    def loadAmpSet(self):
        if not self.device.load.visaPort:          
            self.messageAlert("Electronic Load","No Visa Port Connected")            
            return None       
        command="CURR "+str(self.device.disChargAmpSet.value())
        self.visaWrite(command)


    def loadResSet(self):
        if not self.device.load.visaPort:            
            self.messageAlert("Electronic Load","No Visa Port Connected")            
            return None        
        command="RES "+str(self.device.disChargResSet.value())
        self.visaWrite(command)
      

    def loadPowSet(self):
        if not self.device.load.visaPort:         
            self.messageAlert("Electronic Load","No Visa Port Connected")            
            return None        
        command="POW "+str(self.device.disChargPowSet.value())
        self.visaWrite(command)
        
   
    def loadThreVoltSet(self):
        if not self.device.load.visaPort:           
            self.messageAlert("Electronic Load","No Visa Port Connected")            
            return None
        self.discVoltThreshold=self.device.disChargThreVoltSet.value()      
        print("discVoltThreshold= {}".format(self.discVoltThreshold))

        
    def testIntervalTimeSet(self):
        self.daTimeInterval=float("{:.1f}".format(self.device.testTimeIntervalSet.value()))
        print("time interval: "+str(self.daTimeInterval))
  

    def CsvExport(self):

        timestamp = datetime.now().strftime("%Y_%m_%d-%H_%M_%S")
        file_name = 'ATE_BATT_CDT-'+timestamp+'.csv'
        # Determine the path to the Downloads folder
        downloads_folder = os.path.join(os.path.expanduser('~'), 'Downloads')
       
        # Construct the full file path
        file_path = os.path.join(downloads_folder, file_name)
        heade=["Sl.no","Time","Voltage","Current"]
        # Write to the CSV file
        with open(file_path, 'w', newline='') as csvfile:
            csv_writer = csv.writer(csvfile)        
            csv_writer.writerow(["Battery Sl no: "+self.battTest.batterySlno.text()])
            csv_writer.writerow(["Test Eng: "+self.battTest.testEng.text()])
            csv_writer.writerow(heade)
            print("Len of list ",len(self.voltList))
            for i in range(len(self.voltList)):
                print("i: ",i)
                csv_writer.writerow([self.xAxisList[i],self.timeStampList[i],self.voltList[i],self.ampList[i]])

    
    def serialCommandCommon(self):
        command=str(self.device.power.deviceCommand.text())
        
        self.device.textOutput.appendPlainText("TX: "+command)
        
        bCommand =bytes(command,'ascii')
        self.device.power.comPort.write(bCommand)
        self.device.power.comPort.flush()
    
        rx = ''
        time.sleep(1)
        replay=self.device.power.comPort.readline().strip() #.decode() #decode('ascii')        
        
        print("replay= ".format(replay))
        self.device.textOutput.appendPlainText("RX: "+str(replay))
    
    def visaCommandCommon(self):
        command=str(self.device.load.deviceCommand.text())
        self.device.textOutput.appendPlainText("TX: "+command)
        replay=self.visaRead(command)
        print("replay= ".format(replay))
        self.device.textOutput.appendPlainText("RX: "+replay)
        
    def orderTestSet(self):
        if self.battTest.rChargDisc.isChecked(): 
            self.cycleDirection=True
            print("rChargDisc selected",self.cycleDirection)
        elif self.battTest.rDiscCharg.isChecked():
            self.cycleDirection=False
            print("rDiscCharg selected",self.cycleDirection)

    def loopRadioSet(self):
        if self.battTest.rloopRadio.isChecked():   
            self.loopCycle=True 
            self.battTest.noOfCycleSpinBox.setValue(0)
            self.battTest.rloopRadio.setChecked(True)           
            print("loopCycle ",self.loopCycle)
        else:
            self.loopCycle=False
            self.battTest.rloopRadio.setChecked(False)
            print("loopCycle ",self.loopCycle)

      
    def noOfCycleSet(self):
        self.noOfCycle=self.battTest.noOfCycleSpinBox.value()
        self.battTest.rloopRadio.setChecked(0)
        self.loopCycle=False
        print("self.noOfCycle ",self.noOfCycle)
        print("self.loopCycle ",self.loopCycle)
        


   
    def radioButtonEnabled(self,command):
        self.battTest.rChargDisc.setEnabled(command)
        self.battTest.rDiscCharg.setEnabled(command)

    

    def masterTest():
        print("HI")