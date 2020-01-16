class MyInteger:
    def __init__(self, value = 0):
        if(type(value) == int):
            self.value = value
            self.initvalue = value

        elif(type(value) == float):
            self.value = int(value)
            self.initvalue = int(value)

        elif(type(value) == str):
            self.value = int(value)
            self.initvalue = int(value)

        elif(type(value) == MyInteger):
            self.value = value.value
            self.initvalue = value.value
        else:
            self.value = 0
            self.initvalue = 0
        
        self.vary_value = [self.initvalue]

    def __eq__(self, other):
        if(type(other) == int):
            if(self.value == other):
                return True
            else:
                return False

        elif(type(other) == float):
            if(self.value == int(other)):
                return True
            else :
                return False

        elif(type(other) == str):
            if(self.value == int(other)):
               return True
            else:
                return False
        elif(type(other) == MyInteger):
            if(self.value == other.value):
                return True
            else:
                return False
        else:
            return False
        

    def pressAdd(self, add_value):
        if(type(add_value) == int):
            add_value = add_value  

        elif(type(add_value) == float):
            add_value = int(add_value)

        elif(type(add_value) == str):
            add_value = int(add_value)

        elif(type(add_value) == MyInteger):
            add_value = add_value.value

        self.value += add_value
        self.vary_value.append(add_value)

        return self.value


    def pressSub(self, sub_value):
        if(type(sub_value) == int):
            sub_value = sub_value  

        elif(type(sub_value) == float):
            sub_value = int(sub_value)

        elif(type(sub_value) == str):
            sub_value = int(sub_value)

        elif(type(sub_value) == MyInteger):
            sub_value = sub_value.value

        self.value -= sub_value
        self.vary_value.append(-sub_value)
        return self.value

    def getCurrentVariable(self, mode = 'dec'):
        if(mode == "dec"):
            return self.value
        elif(mode == "hex"):
            return hex(self.value)
        elif(mode == "oct"):
            return oct(self.value)
        elif(mode == "bin"):
            return bin(self.value)
        else:
            return self.value

    def resetCurrentVariable(self):
        self.value = 0
        self.vary_value = [0]
        return self.value

    def rollbackCurrentVariable(self):
        if(len(self.vary_value) == 1):
            return self.vary_value[0]
        else:
            pop = self.vary_value.pop()
            self.value -= pop
            return self.value



