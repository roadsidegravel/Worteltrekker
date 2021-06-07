import tkinter

class MyInterfaceStepCount:
    labelWidth = 5
    labelHeight = 2
    def __init__(self,startgridrow,startgridcolumn,window):
        startRow = startgridrow
        startCol = startgridcolumn
        self.window = window
        labelWidth = self.labelWidth
        labelHeight = self.labelHeight
        #https://stackoverflow.com/questions/2603169/update-tkinter-label-from-variable
        self.XCount = tkinter.StringVar()
        self.XCount.set('X')
        self.ACount = tkinter.StringVar()
        self.ACount.set('A')
        self.BCount = tkinter.StringVar()
        self.BCount.set('B')
        self.CCount = tkinter.StringVar()
        self.CCount.set('C')
        self.DCount = tkinter.StringVar()
        self.DCount.set('D')
        self.FCount = tkinter.StringVar()
        self.FCount.set('F')

        self.XLabel = tkinter.Label(window, textvariable=self.XCount, width=labelWidth, height=labelHeight)
        self.XLabel.grid(row=startRow, column=startCol)
        self.ALabel = tkinter.Label(window, textvariable=self.ACount, width=labelWidth, height=labelHeight)
        self.ALabel.grid(row=startRow, column=startCol + 1)
        self.BLabel = tkinter.Label(window, textvariable=self.BCount, width=labelWidth, height=labelHeight)
        self.BLabel.grid(row=startRow, column=startCol + 2)
        self.CLabel = tkinter.Label(window, textvariable=self.CCount, width=labelWidth, height=labelHeight)
        self.CLabel.grid(row=startRow, column=startCol + 3)
        self.DLabel = tkinter.Label(window, textvariable=self.DCount, width=labelWidth, height=labelHeight)
        self.DLabel.grid(row=startRow, column=startCol + 4)
        self.FLabel = tkinter.Label(window, textvariable=self.FCount, width=labelWidth, height=labelHeight)
        self.FLabel.grid(row=startRow, column=startCol + 5)
        self.CountArray = [self.XCount,self.ACount,self.BCount,self.CCount,self.DCount,self.FCount]

    def SetStepCount(self,newCountArray):
        if newCountArray == None:
            print(f'@interfaceStepCount:SetStepCount: newCountArray cant be None')
            return
        if not len(newCountArray) == len(self.CountArray):
            print(f'@interfaceStepCount:setStepCount: wrong length {newCountArray}')
            return
        for i in range(0,len(newCountArray)):
            self.CountArray[i].set(newCountArray[i])