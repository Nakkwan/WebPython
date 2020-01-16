class MyInteger:

    def __init__(self, givenValue = 0):
        if(type(givenValue) == int):
            self.initValue = givenValue
            self.currrentValue = givenValue
        elif((type(givenValue) == str) or (type(givenValue) == float)):
            self.initValue = int(givenValue)
            self.currrentValue = int(givenValue)
        elif(type(givenValue) == MyInteger):
            self.initValue = givenValue.currrentValue
            self.currrentValue = givenValue.currrentValue
        else:
            self.initValue = 0
            self.currrentValue = 0
        self.history = []

    def __eq__(self, givenValue):
        if(type(givenValue) == int):
            return self.currrentValue == givenValue
        elif((type(givenValue) == str) or (type(givenValue) == float)):
            return self.currrentValue == int(givenValue)
        elif(type(givenValue) == MyInteger):
            return self.currrentValue == givenValue.currrentValue
        else:
            return False

    def pressAdd(self, givenValue):
        self.history.append(self.currrentValue)    
        if(type(givenValue) == int):
            self.currrentValue += givenValue
        elif((type(givenValue) == str) or (type(givenValue) == float)):
            self.currrentValue += int(givenValue)
        elif(type(givenValue) == MyInteger):
            self.currrentValue += givenValue.currrentValue
        return self.currrentValue

    def pressSub(self, givenValue):
        self.history.append(self.currrentValue) 
        if(type(givenValue) == int):
            self.currrentValue -= givenValue
        elif((type(givenValue) == str) or (type(givenValue) == float)):
            self.currrentValue -= int(givenValue)
        elif(type(givenValue) == MyInteger):
            self.currrentValue -= givenValue.currrentValue   
        return self.currrentValue

    def getCurrentVariable(self, mode = "dec"):
        if(mode == "dec"):
            return self.currrentValue
        elif(mode == "hex"):
            return hex(self.currrentValue)
        elif(mode == "oct"):
            return oct(self.currrentValue)
        elif(mode == "bin"):
            return bin(self.currrentValue)
        else:
            return self.currrentValue

    def resetCurrentVariable(self):
        self.currrentValue = self.initValue # or 0
        self.history = []
        return self.currrentValue

    def rollbackCurrentVariable(self):
        if(self.history.__len__() > 0):
            self.currrentValue = self.history.pop()
        return self.currrentValue

