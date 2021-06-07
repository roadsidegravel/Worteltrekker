import tkinter

class MyInterfaceMovementDirections:
    #X,A,B,C,D,F
    width = 4
    height = 2
    colorMoving = "green"
    colorNeutral = "grey"
    colorStopped = "orange"
    def __init__(self,startgridrow,startgridcolumn,window):
        self.startRow = startgridrow
        self.startCol = startgridcolumn
        self.window = window
        #stop button row
        self.S = tkinter.Button(self.window, text="S", command=self.pressS, width=self.width, height=self.height)
        self.S.grid(row=self.startRow, column=self.startCol +6)
        #I and D pairings
        self.XI = tkinter.Button(self.window, text="XI", command=self.pressXI, width= self.width, height = self.height)
        self.XI.grid(row=self.startRow+1, column=self.startCol)
        self.XD = tkinter.Button(self.window, text="XD", command=self.pressXD, width= self.width, height = self.height)
        self.XD.grid(row=self.startRow+2, column=self.startCol)

        self.AI = tkinter.Button(self.window, text="AI", command=self.pressAI, width= self.width, height = self.height)
        self.AI.grid(row=self.startRow+1, column=self.startCol+1)
        self.AD = tkinter.Button(self.window, text="AD", command=self.pressAD, width= self.width, height = self.height)
        self.AD.grid(row=self.startRow+2, column=self.startCol+1)

        self.BI = tkinter.Button(self.window, text="BI", command=self.pressBI, width= self.width, height = self.height)
        self.BI.grid(row=self.startRow+1, column=self.startCol+2)
        self.BD = tkinter.Button(self.window, text="BD", command=self.pressBD, width= self.width, height = self.height)
        self.BD.grid(row=self.startRow+2, column=self.startCol+2)

        self.CI= tkinter.Button(self.window, text="CI", command=self.pressCI, width= self.width, height = self.height)
        self.CI.grid(row=self.startRow+1, column=self.startCol+3)
        self.CD= tkinter.Button(self.window, text="CD", command=self.pressCD, width= self.width, height = self.height)
        self.CD.grid(row=self.startRow+2, column=self.startCol+3)

        self.DI= tkinter.Button(self.window, text="DI", command=self.pressDI, width= self.width, height = self.height)
        self.DI.grid(row=self.startRow+1, column=self.startCol+4)
        self.DD = tkinter.Button(self.window, text="DD", command=self.pressDD, width= self.width, height = self.height)
        self.DD.grid(row=self.startRow+2, column=self.startCol+4)

        self.FI= tkinter.Button(self.window, text="FI", command=self.pressFI, width= self.width, height = self.height)
        self.FI.grid(row=self.startRow+1, column=self.startCol+5)
        self.FD= tkinter.Button(self.window, text="FD", command=self.pressFD, width= self.width, height = self.height)
        self.FD.grid(row=self.startRow+2, column=self.startCol+5)

        self.AllI = [self.XI,self.AI,self.BI,self.CI,self.DI,self.FI]
        self.AllD = [self.XD,self.AD,self.BD,self.CD,self.DD,self.FD]

    def pressS(self):
        print(f'Stop pressed!')
        print(f'TODO send stop command!!!!')
        for i in range(0,len(self.AllI)):
            self.AllI[i].configure(bg=self.colorStopped)
        for i in range(0,len(self.AllD)):
            self.AllD[i].configure(bg=self.colorStopped)

    def pressXI(self):
       print(f'XI')
    def pressXD(self):
        print(f'XD')

    def pressAI(self):
        print(f'AI')
    def pressAD(self):
        print(f'AD')

    def pressBI(self):
        print(f'BI')
    def pressBD(self):
        print(f'BD')

    def pressCI(self):
       print(f'CI')
    def pressCD(self):
        print(f'CD')

    def pressDI(self):
        print(f'DI')
    def pressDD(self):
        print(f'DD')

    def pressFI(self):
        print(f'FI')
    def pressFD(self):
        print(f'FD')

    def MinStatus(self,newMinStatus):
        if newMinStatus == None:
            print(f'@interfaceMovementDirections:MinStatus: newMinStatus cant be None')
            return
        if not len(newMinStatus) == len(self.AllI):
            print(f'@interfaceMovementDirections:MinStatus: lengths do not match {newMinStatus}')
            return
        for i in range(0,len(newMinStatus)):
            if newMinStatus:
                self.AllI[i].configure(bg=self.colorNeutral)
            else:
                self.AllI[i].configure(bg=self.colorStopped)

    def MaxStatus(self,newMaxStatus):
        if newMaxStatus == None:
            print(f'@interfaceMovementDirections:MaxStatus: newMaxStatus cant be None')
            return
        if not len(newMaxStatus) == len(self.AllI):
            print(f'@interfaceMovementDirections:MaxStatus: lengths do not match {newMaxStatus}')
            return
        for i in range(0,len(newMaxStatus)):
            if newMaxStatus:
                self.AllD[i].configure(bg=self.colorNeutral)
            else:
                self.AllD[i].configure(bg=self.colorStopped)


    def IndicateMoving(self, newMoving):
        if newMoving == None:
            print(f'@interfaceMovementDirections:IndicateMoving: newMoving cant be None')
            return
        if not len(newMoving) == 2:
            print(f'@interfaceMoventDirections:IndicateMoving: {newMoving} is not length 2')
        whoM = newMoving[0]
        whoNumber = -1
        if whoM == 'S':
            #stopped, or nobody is moving
            return
        if whoM == 'X':
            whoNumber = 0
        elif whoM == 'A':
            whoNumber = 1
        elif whoM == 'B':
            whoNumber = 2
        elif whoM == 'C':
            whoNumber = 3
        elif whoM == 'D':
            whoNumber = 4
        elif whoM == 'F':
            whoNumber = 5
        else:
            #not understood
            print(f'@InterfaceMovementDirections:IndicateMoving: {newMoving} not understood')
            return
        whereM = newMoving[1]
        if whereM == 'I':
            self.AllI[whoNumber].configure(bg=self.colorMoving)
        elif whereM == 'D':
            self.AllD[whoNumber].configure(bg=self.colorMoving)
        else:
            # not understood
            print(f'@InterfaceMovementDirections:IndicateMoving: {newMoving} not understood')
            return
