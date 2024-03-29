class Würfel:
    def __init__(self, id, value, thrownPast, keep, valid, thrown):
        self.id = id
        self.value = value
        self.thrownPast = thrownPast
        self.keep = keep
        self.valid = valid
        self.thrown = thrown
        
    def setKeep(self):
        self.keep = 1
        
    def setThrown(self):
        self.thrown = 1
    
    def getValid(self):
        return self.valid
    
    def setValidity(self, valueCount):
        currValueAsString = str(self.value)
        if self.value not in (1,5):
            if valueCount[currValueAsString] >= 3:
                self.valid = 1
            else:
                self.valid = 0
        else:
            if valueCount[currValueAsString] >= 1:
                self.valid = 1
            else:
                self.valid = 0