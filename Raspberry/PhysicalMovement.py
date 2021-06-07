class MovementAxis:
    currentCount = 0
    minStopCount = False
    maxStopCount = False

    def UpdateAxisData(self,newCount,newMin,newMax):
        if not newCount < 0:
            self.CurrentCount = newCount
        else:
            print(f'value {newCount} is too low')
            return
        self.minStopCount = newMin
        self.maxStopCount = newMax