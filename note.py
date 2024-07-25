# # importing libraries 
# from PySide6.QtWidgets import *
# from PySide6.QtGui import *
# from PySide6.QtCore import *
# import sys 


# class Window(QMainWindow): 
# 	def __init__(self): 
# 		super().__init__() 

# 		# setting title 
# 		self.setWindowTitle("Python ") 

# 		# setting geometry 
# 		self.setGeometry(100, 100, 600, 400) 

# 		# calling method 
# 		self.UiComponents() 

# 		# showing all the widgets 
# 		self.show() 

# 	# method for widgets 
# 	def UiComponents(self): 

# 		# creating a push button 
# 		button = QPushButton("CLICK", self) 

# 		# setting geometry of button 
# 		button.setGeometry(200, 150, 100, 60) 

# 		# changing color of button 
# 		button.setStyleSheet("background-color : yellow") 

# 		# adding action to a button 
# 		button.clicked.connect(self.clickme) 


# 	# action method 
# 	def clickme(self): 


# 		# printing pressed 
# 		print("pressed") 

# # create pyqt5 app 
# App = QApplication(sys.argv) 

# # create the instance of our Window 
# window = Window() 

# # start the app 
# sys.exit(App.exec()) 



import time


count=0
noOfCycle=10
loopCycle=None
i=0
CD=True
def charg():
    print("Charge")
def discharg():
    print("Discharge")

print("Logic ",count<noOfCycle)
print("loop ",loopCycle)
while (i<noOfCycle) or (loopCycle):
    if CD==True:
        charg()
        discharg()
        
    else:
        discharg()
        charg()
    

    i=i+1
    print("i: ",i)    
    print("----------------------")    
    time.sleep(1)    



    


















# #         self.disChargVoltSet=QDoubleSpinBox()
# #         self.disChargVoltSet.setMinimum(0)
# #         self.disChargVoltSet.setMaximum(40)
# #         self.disChargVoltSet.setValue(24.3)
# #         self.disChargVoltSet.setSingleStep(.1)
# #         self.disChargVoltSet.setSuffix(" V")
# #         self.disChargVoltSet.setDecimals(1)
        
# #         self.bDischargVoltSet=QPushButton(text="Set")

# #         self.disChargAmpSet=QDoubleSpinBox()
# #         self.disChargAmpSet.setMinimum(0)
# #         self.disChargAmpSet.setMaximum(10)
# #         self.disChargAmpSet.setValue(1)
# #         self.disChargAmpSet.setSingleStep(.1)
# #         self.disChargAmpSet.setSuffix(" A")
# #         self.disChargAmpSet.setDecimals(1)
        
# #         self.bDisChargAmpSet=QPushButton(text="Set")
       
# #         self.disChargResSet=QDoubleSpinBox()
# #         self.disChargResSet.setMinimum(0)
# #         self.disChargResSet.setMaximum(10)
# #         self.disChargResSet.setValue(1)
# #         self.disChargResSet.setSingleStep(.1)
# #         self.disChargResSet.setSuffix(" A")
# #         self.disChargResSet.setDecimals(1)
        
# #         self.bDisChargResSet=QPushButton(text="Set")
       

# #         self.disChargPowSet=QDoubleSpinBox()
# #         self.disChargPowSet.setMinimum(0)
# #         self.disChargPowSet.setMaximum(10)
# #         self.disChargPowSet.setValue(1)
# #         self.disChargPowSet.setSingleStep(.1)
# #         self.disChargPowSet.setSuffix(" A")
# #         self.disChargPowSet.setDecimals(1)
        
# #         self.bDisChargPowSet=QPushButton(text="Set")
      


# #         self.disChargSet1=QHBoxLayout()
# #         self.disChargSet1.addWidget(self.disChargVoltSet)
# #         self.disChargSet1.addWidget(self.bDisChargVoltSet)
        
# #         self.disChargSet2=QHBoxLayout()
# #         self.disChargSet2.addWidget(self.disChargAmpSet)
# #         self.disChargSet2.addWidget(self.bDisChargAmpSet)

# #         self.disChargSet3=QHBoxLayout()
# #         self.disChargSet3.addWidget(self.disChargResSet)
# #         self.disChargSet3.addWidget(self.bDisChargResSet)

# # 3       self.disChargSet4=QHBoxLayout()
# #         self.disChargSet4.addWidget(self.disChargPowSet)
# #         self.disChargSet4.addWidget(self.bDisChargPowSet)

# #         self.disChargSetbox=QVBoxLayout()
# #         self.disChargSetbox.addLayout(self.disChargSet1)
# #         self.disChargSetbox.addLayout(self.disChargSet2)
# #         self.disChargSetbox.addLayout(self.disChargSet3)
# #         self.disChargSetbox.addLayout(self.disChargSet4)
        
# #         self.testSetHlayout=QHBoxLayout()
# #         self.testSetHlayout.addLayout(self.chargSetbox)
# #         self.testSetHlayout.addLayout(self.disChargSetbox)




# # # # self.l.setText("Counter: %d" % self.counter)
# # # # self.timer = QTimer()
# # # # self.timer.setInterval(1000)
# # # # self.timer.timeout.connect(self.recurring_timer)
# # # # self.timer.start()


# # # import threading


# # # def print_cube(num):
# # #     print("Cube: {}" .format(num * num * num))


# # # def print_square(num):
# # #     print("Square: {}" .format(num * num))


# # # if __name__ =="__main__":
# # #     print_cube(10)
# # #     print_square(10)


# # #     # t1 = threading.Thread(target=print_square, args=(10,))
# # #     # t2 = threading.Thread(target=print_cube, args=(10,))

# # #     # t1.start()
# # #     # t2.start()

# # #     # t1.join()
# # #     # t2.join()

# # #     print("Done!")



# # #         # self.battTest.vPlot.graph(x,y)
# # #                     # futures = self.battTest.dPsVolt.setText(str(k)+" V")
# # #                     # loop = asyncio.get_event_loop()
# # #                     # loop.run_until_complete(asyncio.wait(futures))
# # #                    # QtAsyncio.run(self.battTest.dPsVolt.setText(str(k)+" V"))
# # # # QtAsyncio.run(self.battTest.dPsVolt.setText(str(k)+" V"))
# # #  #self.battTest.dPsVolt.setText(str(k)+" V")