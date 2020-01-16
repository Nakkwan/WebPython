class MyInteger:

    def __init__(self, givenValue = 0):
        if(type(givenValue) == int):
            self.initValue = givenValue
            self.currrentValue = givenValue
        elif((type(givenValue) == str) or (type(givenValue) == float)):
            if(type(int(givenValue)) == int):
                self.initValue = int(givenValue)
                self.currrentValue = int(givenValue)
        elif(type(givenValue) == MyInteger):
            self.initValue = givenValue.currrentValue
            self.currrentValue = givenValue.currrentValue
        elif(type(givenValue) == list):
            sum = 0
            for i in givenValue:
                if(type(i) == str):
                    if(i.isnumeric()):
                        sum += MyInteger(i).currrentValue
                else:
                    sum += MyInteger(i).currrentValue
            self.currrentValue = sum
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

    def __ge__(self, givenValue):
        if(type(givenValue) == int):
            return self.currrentValue >= givenValue
        elif((type(givenValue) == str) or (type(givenValue) == float)):
            return self.currrentValue >= int(givenValue)
        elif(type(givenValue) == MyInteger):
            return self.currrentValue >= givenValue.currrentValue
        else:
            return False

    def __le__(self, givenValue):
        if(type(givenValue) == int):
            return self.currrentValue <= givenValue
        elif((type(givenValue) == str) or (type(givenValue) == float)):
            return self.currrentValue <= int(givenValue)
        elif(type(givenValue) == MyInteger):
            return self.currrentValue <= givenValue.currrentValue
        else:
            return False

    def __add__(self, value):
        if(type(value) == int):
            self.currrentValue += value
        elif(type(value) == MyInteger):
            self.currrentValue += value.currrentValue
        return MyInteger(self.currrentValue)

    def __radd__(self, value):
        if(type(value) == int):
            self.currrentValue += value
        elif(type(value) == MyInteger):
            self.currrentValue += value.currrentValue
        return MyInteger(self.currrentValue)
    


    def __str__(self):
        rep = str(self.currrentValue)
        return rep

    def pressAdd(self, givenValue):
        self.history.append(self.currrentValue)    
        if(type(givenValue) == int):
            self.currrentValue += givenValue
        elif((type(givenValue) == str) or (type(givenValue) == float)):
            self.currrentValue += int(givenValue)
        elif(type(givenValue) == MyInteger):
            self.currrentValue += givenValue.currrentValue
        return MyInteger(self.currrentValue)

    def pressSub(self, givenValue):
        self.history.append(self.currrentValue) 
        if(type(givenValue) == int):
            self.currrentValue -= givenValue
        elif((type(givenValue) == str) or (type(givenValue) == float)):
            self.currrentValue -= int(givenValue)
        elif(type(givenValue) == MyInteger):
            self.currrentValue -= givenValue.currrentValue   
        return MyInteger(self.currrentValue)

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

list1 = [1, 2, 3, "4", "5", MyInteger(6), MyInteger(7), 8, 9, 10]
list2 = [1, 2, 3, "4", "5", MyInteger(6), MyInteger(7), "alpha", 8, 9, "beta", 10]


num0 = MyInteger(30) + 10
num0.pressAdd(10)
num1 = (MyInteger(30) + 10).pressAdd(10)
num1.pressSub(100)
num2 = (10 + MyInteger(30)).pressAdd(10)
num2.pressSub(100)
num3 = MyInteger(20)
num4 = MyInteger(list1)
num5 = MyInteger(list2)

print(num0, type(num0))
print(num1, type(num1))
print(num2, type(num2))
print(num2 + num3, type(num2 +num3))
print(num2 <= num3)
print(num2 >= num3)
print(num2 <= 3)
print(num2 >= 3)
print(num2 + 2, type(num2 + 2))
print(2 + num3, type(2 + num3))
print(num4, type(num4))
print(num5, type(num5))