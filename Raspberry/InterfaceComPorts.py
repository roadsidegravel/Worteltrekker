import tkinter
import serial.tools.list_ports

class MyInterfaceComPorts:
    def __init__(self,startgridrow,startgridcolumn,window):
        self.tasks = []
        self.comVar = tkinter.StringVar()
        self.comOptions = ["None"]
        self.comVar.set(self.comOptions[0])
        self.window = window
        self.startgridrow = startgridrow
        self.startgridcolumn = startgridcolumn
        self.RefreshComPortsButton = tkinter.Button(self.window, text="refresh", command=self._ReloadComPortOptions)
        self.RefreshComPortsButton.grid(row=self.startgridrow, column=self.startgridcolumn, columnspan=2)
        self.ComPortSelector = tkinter.OptionMenu(self.window, self.comVar, *self.comOptions, command=self._SelectComPorts)
        self.ComPortSelector.grid(row=self.startgridrow+1, column=self.startgridcolumn, columnspan = 2)
        self._ReloadComPortOptions()

    def _SelectComPorts(self):
        self.comPortName = str(self.comVar.get())
        print(f'Selected {self.comPortName}')
        self.tasks.insert(0,"ConnectToComPort")

    def returnComPortName(self):
        return self.comPortName


    def _ReloadComPortOptions(self):
        self.comOptions = []
        listPortInfosRaw = self._getComPorts()
        #https://pythonhosted.org/pyserial/tools.html#serial.tools.list_ports.ListPortInfo
        #port, description, hwid = info
        if (len(listPortInfosRaw)) > 0:
            for i in range(len(listPortInfosRaw)):
               self.comOptions.append(listPortInfosRaw[i][0])
        else:
            self.comOptions.append("None")
        #https://stackoverflow.com/questions/17580218/changing-the-options-of-a-optionmenu-when-clicking-a-button
        self.ComPortSelector['menu'].delete(0,'end')
        self.comVar.set(self.comOptions[0])
        for comPortOption in self.comOptions:
            self.ComPortSelector['menu'].add_command(label=comPortOption,command=self._SelectComPorts)

    def _getComPorts(self):
        # https://stackoverflow.com/questions/12090503/listing-available-com-ports-with-python
        ListPortInfosRaw = serial.tools.list_ports.comports()
        return ListPortInfosRaw
