import serial
#https://pythonhosted.org/pyserial/index.html

class ArduinoSerial:
    ArduinoCom = serial.Serial()

    def setPort(self,PortName):
        try:
            self.ArduinoCom.close()
            self.ArduinoCom = serial.Serial(PortName,57600,timeout=1,write_timeout=1)
        except Exception as ex:
             print(f'Setting port to {PortName}  failed, error: {ex}')

    def ReadArduino(self):
        if self.ArduinoCom.is_open:
            #https://stackoverflow.com/questions/16077912/python-serial-how-to-use-the-read-or-readline-function-to-read-more-than-1-char
            #https://arduino.stackexchange.com/questions/10088/what-is-the-difference-between-serial-write-and-serial-print-and-when-are-they
            return str(self.ArduinoCom.readline())  #change to readline?

    def WriteArduino(self,message):
        if self.ArduinoCom.is_open:
            message = '<'+message+'>'
            for x in range(0,len(message)):
                self.ArduinoCom.write(str.encode(message[x]))
            return True
        else:
            return False

    def CloseConnection(self):
        print(f'closing connection...')
        self.ArduinoCom.close()