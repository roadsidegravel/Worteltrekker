import tkinter
import SerialCommunication
import time
import sys
import PhysicalMovement
import InterfaceEndstops
import InterfaceMovementDirections
import InterfaceComPorts
import InterfaceStepCount

#https://effbot.org/zone/tkinter-callbacks.htm
#onderste'using bound methods' in de fix me sectie heeft de dag gered

class MyInterface:
    #colors http://www.science.smith.edu/dftwiki/index.php/Color_Charts_for_TKinter
    #https://www.delftstack.com/howto/python-tkinter/how-to-set-tkinter-backgroud-color/
    #https://python-textbok.readthedocs.io/en/1.0/Introduction_to_GUI_Programming.html
    BackgroundColor = 'lemon chiffon'
    ActiveColor = 'cyan'
    window = tkinter.Tk()
    window.title('My Window')
    window.geometry('800x600')
    window.configure(bg=BackgroundColor)
    #layout configuration
    ManualMovementLabelRow = 0
    ManualMovementInputRow = ManualMovementLabelRow+1
    ManualMovementStartColumn = 0
    InformationLabelsStartRow = ManualMovementInputRow+3
    InformationLabelsStartColumn = 0
    ArduinoCom = SerialCommunication.ArduinoSerial()
    Running = True

    taskList = []
    currentTask = ""

    #http://www.effbot.org/tkinterbook/label.htm
    whoLabel = tkinter.Label(window, bg=BackgroundColor, text='who?')
    whoLabel.grid(row=ManualMovementLabelRow,column=ManualMovementStartColumn, columnspan = 2)
    dirLabel = tkinter.Label(window,bg=BackgroundColor, text='direction?')
    dirLabel.grid(row=ManualMovementLabelRow,column=ManualMovementStartColumn+2, columnspan = 2)

    def whoSelection(self,value):
        self.whoLabel.config(text='Who: ' + value)
    def dirSelection(self,value):
        self.dirLabel.config(text='direction: '+ value)

    #http://www.effbot.org/tkinterbook/optionmenu.htm
    #https://stackoverflow.com/questions/26744366/adding-command-to-a-tkinter-optionmenu
    whoVar = tkinter.StringVar()
    whoOptions = ('X','A','B','C','D','F')
    whoVar.set(whoOptions[0])
    dirVar = tkinter.StringVar()
    dirOptions = ('I', 'D')
    dirVar.set(dirOptions[0])

    #def stepsSelection(self,value):
    #    self.stepsLabel.config(text='steps: '+ value)
    #http://www.effbot.org/tkinterbook/entry.htm
    #https://riptutorial.com/tkinter/example/27780/adding-validation-to-an-entry-widget
    def onlyNumbers(char):
       return char.isdigit()
    validationFun = window.register(onlyNumbers)
    stepsEntry = tkinter.Entry(window, validate="key", validatecommand=(validationFun, '%S'), width = 10)
    stepsEntry.grid(row=ManualMovementInputRow,column=ManualMovementStartColumn+4, columnspan = 2)


    def __init__(self):
        #https://effbot.org/tkinterbook/grid.htm
        self.WhoChoice = tkinter.OptionMenu(self.window, self.whoVar, *self.whoOptions,command=self.whoSelection)
        self.WhoChoice.grid(row=self.ManualMovementInputRow,column=self.ManualMovementStartColumn, columnspan = 2)
        self.dirChoice = tkinter.OptionMenu(self.window,self.dirVar,*self.dirOptions,command=self.dirSelection)
        self.dirChoice.grid(row=self.ManualMovementInputRow,column=self.ManualMovementStartColumn+2, columnspan = 2)
        self.ExitButton = tkinter.Button(self.window, text="Exit", command=self.CleanExit)
        self.ExitButton.grid(row=self.ManualMovementLabelRow, column=10, columnspan = 2)
        self.ManualMoveButton = tkinter.Button(self.window, text="send", command=self.ManualMovePressed)
        self.ManualMoveButton.grid(row=self.ManualMovementInputRow, column=self.ManualMovementStartColumn + 8)
        self.MyInterfaceEndstops = InterfaceEndstops.MyInterfaceEndstops(3,0,self.window)
        self.MyInterfaceMovementDirections = InterfaceMovementDirections.MyInterfaceMovementDirections(5,0,self.window)
        self.MyInterfaceComPorts = InterfaceComPorts.MyInterfaceComPorts(0,6,self.window)
        self.MyinterfaceStepCount = InterfaceStepCount.MyInterfaceStepCount(5,0,self.window)

    def ManualMovePressed(self):
        requestedCount = self.stepsEntry.get()
        if not requestedCount == '':
            if int(requestedCount) > 0:
                #the purpose of the str(int( is to get rid of leading zero's
                AssembledMessage =self.whoVar.get()+self.dirVar.get()+str(int(requestedCount))
                print(AssembledMessage)
                success = self.ArduinoCom.WriteArduino(AssembledMessage)
                print(f'sending {AssembledMessage}... {success}')
            else:
                print(f'invalid step count requested: {requestedCount}')


    #InfoLabelX = tkinter.Label(window,bg=BackgroundColor,activebackground=ActiveColor,text='X info')
    #InfoLabelX.grid(row=InformationLabelsStartRow,column=InformationLabelsStartColumn)
    #InfoLabelY = tkinter.Label(window,bg=BackgroundColor,text='Y info')
    #InfoLabelY.grid(row=InformationLabelsStartRow+1,column=InformationLabelsStartColumn)

    #ReceivedMessageLabel = tkinter.Label(window,bg=BackgroundColor,activebackground=ActiveColor,text='...')
    #ReceivedMessageLabel.grid(row=InformationLabelsStartRow,column=InformationLabelsStartColumn+2)

    def CleanExit(self):
        self.ArduinoCom.CloseConnection()
        print(f'exiting...')
        self.Running = False

    def IncomingMessageCleanUp(self,IncomingMessage):
        #https://www.journaldev.com/23674/python-remove-character-from-string
        CleanedUp = None
        if not IncomingMessage == None:
            CleanedUp = IncomingMessage[1:]
            CleanedUp = CleanedUp.translate({ord(i): None for i in '\''})
            #https://stackoverflow.com/questions/5188792/how-to-check-a-string-for-specific-characters
            position = CleanedUp.find('\\')
            if position > 0:
                #if find returned -1, it's not in the string
                CleanedUp = CleanedUp[0:position]
        return CleanedUp

    NumberOfAxis = 6
    AxisX = PhysicalMovement.MovementAxis
    AxisA = PhysicalMovement.MovementAxis
    AxisB = PhysicalMovement.MovementAxis
    AxisC = PhysicalMovement.MovementAxis
    AxisD = PhysicalMovement.MovementAxis
    AxisF = PhysicalMovement.MovementAxis

    def InterpretationIncMsg(self,newMessage):
        if newMessage == None:
            return
        #print(f'{newMessage}')
        if len(newMessage) <= 0:
            print(f'incoming message too short, ignored')
            return
        if newMessage[0] == 'U':
            print(f'statusupdate received: {newMessage}')
            if newMessage.count('*') < self.NumberOfAxis:
                print(f'statusupdate incomplete, disregarded')
            who = newMessage[1] #s,x,y,z,...
            where = newMessage[2]#increasing or decreasing
            min = newMessage[6:12]
            max = newMessage[15:21]
            counts = newMessage[22:]
            print(f'{who} is {where}, MIN: {min}, MAX:{max}, counts: {counts}')
            self.MyInterfaceMovementDirections.MinStatus(min)
            self.MyInterfaceMovementDirections.MaxStatus(max)
            self.MyInterfaceMovementDirections.IndicateMoving(who+where)
            #1 is endstop pressed or connection broken, 0 is endstop open all is well
            self.MyInterfaceEndstops.SetMinStatus(min)
            self.MyInterfaceEndstops.SetMaxStatus(max)
            #https://stackoverflow.com/questions/743806/how-to-split-a-string-into-a-list
            countSplit = counts.split('*')
            countArray = countSplit[:-1]
            self.MyinterfaceStepCount.SetStepCount(countArray)
            #TODO in MyInterface, communicatiedingen queuen, in loop afgaan en van de stack nemen

    def GetTasks(self):
        if not self.MyInterfaceComPorts.tasks == None:
            if not len(self.MyInterfaceComPorts.tasks) == 0:
                self.taskList.insert(0,self.MyInterfaceComPorts.tasks.pop())
                #print(self.taskList)

    def PerformTasks(self):
        if self.currentTask == "":
            if len(self.taskList) > 0:
                self.currentTask = self.taskList.pop()
                print(self.currentTask)
        else:
            if self.currentTask == "ConnectToComPort":
                comPortName = self.MyInterfaceComPorts.returnComPortName()
                self.ArduinoCom.setPort(comPortName)
                #we just changed the comport (or tried to), clear tasks to avoid unexpected movements
                self.taskList.clear()
                print(f'Task attempt connection to {comPortName} done')
                self.currentTask = ""
            else:
                print(f'Task {self.currentTask} not understood')



    #https://stackoverflow.com/questions/29158220/tkinter-understanding-mainloop
    #window.mainloop()
    previousFrame = time.time()
    def RunInterface(self):

        while self.Running:
            self.window.update_idletasks()
            self.window.update()
            self.GetTasks()
            self.PerformTasks()
            try:
                IncomingMessage = self.ArduinoCom.ReadArduino()
                IncomingMessage = self.IncomingMessageCleanUp(IncomingMessage)
                self.InterpretationIncMsg(IncomingMessage)
                #https://forum.arduino.cc/index.php?topic=396450.0 arduino communication
            except Exception as ex:
                print(ex)
                pass

        if not self.Running:
            self.window.destroy()
            sys.exit('Exiting')

