import tkinter

class MyInterfaceEndstops:
    colorPressed = "orange"
    colorOpen = "green"
    labelWidth = 5
    labelHeight = 2
    startRow = 0
    startCol =  0
    def __init__(self,startRow,startCol,window):
        self.startRow = startRow
        self.startCol = startCol
        self.window = window
        labelWidth = self.labelWidth
        labelHeight = self.labelHeight

        self.XMin = tkinter.Label(window, text="X min", width=labelWidth, height=labelHeight)
        self.XMin.grid(row=startRow, column=startCol)
        self.AMin = tkinter.Label(window, text="A min", width=labelWidth, height=labelHeight)
        self.AMin.grid(row=startRow, column=startCol + 1)
        self.BMin = tkinter.Label(window, text="B min", width=labelWidth, height=labelHeight)
        self.BMin.grid(row=startRow, column=startCol + 2)
        self.CMin = tkinter.Label(window, text="C min", width=labelWidth, height=labelHeight)
        self.CMin.grid(row=startRow, column=startCol + 3)
        self.DMin = tkinter.Label(window, text="D min", width=labelWidth, height=labelHeight)
        self.DMin.grid(row=startRow, column=startCol + 4)
        self.FMin = tkinter.Label(window, text="F min", width=labelWidth, height=labelHeight)
        self.FMin.grid(row=startRow, column=startCol + 5)
        self.MinArray = [self.XMin,self.AMin,self.BMin,self.CMin,self.DMin,self.FMin]

        self.XMax = tkinter.Label(window, text="X max", width=labelWidth, height=labelHeight)
        self.XMax.grid(row=startRow-1, column=startCol)
        self.AMax = tkinter.Label(window, text="A max", width=labelWidth, height=labelHeight)
        self.AMax.grid(row=startRow-1, column=startCol + 1)
        self.BMax = tkinter.Label(window, text="B max", width=labelWidth, height=labelHeight)
        self.BMax.grid(row=startRow-1, column=startCol + 2)
        self.CMax = tkinter.Label(window, text="C max", width=labelWidth, height=labelHeight)
        self.CMax.grid(row=startRow-1, column=startCol + 3)
        self.DMax = tkinter.Label(window, text="D max", width=labelWidth, height=labelHeight)
        self.DMax.grid(row=startRow-1, column=startCol + 4)
        self.FMax = tkinter.Label(window, text="F max", width=labelWidth, height=labelHeight)
        self.FMax.grid(row=startRow-1, column=startCol + 5)
        self.MaxArray = [self.XMax,self.AMax,self.BMax,self.CMax,self.DMax,self.FMax]

    def SetMinStatus(self, newArrayMin):
        if newArrayMin == None:
            print(f'@interfaceEndstops:setminstatus: newArrayMin cant be None')
            return
        if not len(newArrayMin) == len(self.MinArray):
            print(f'@interfaceEndstops:setMinStatus: wrong length {newArrayMin}')
            return
        for i in range(0,len(newArrayMin)):
            if newArrayMin[i] == '0':
                self.MinArray[i].configure(bg=self.colorOpen)
            else:
                self.MinArray[i].configure(bg=self.colorPressed)

    def SetMaxStatus(self, newArrayMax):
        if newArrayMax == None:
            print(f'@interfaceEndstops:SetMaxStatus: newArrayMin cant be None')
            return
        if not len(newArrayMax) == len(self.MaxArray):
            print(f'@interfaceEndstops:setMaxStatus: wrong length {newArrayMax}')
            return
        for i in range(0,len(newArrayMax)):
            if newArrayMax[i] == '0':
                self.MaxArray[i].configure(bg=self.colorOpen)
            else:
                self.MaxArray[i].configure(bg=self.colorPressed)




