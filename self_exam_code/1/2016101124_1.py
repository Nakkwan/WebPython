# ANSWER : START
class myFile():
    def __init__(self, fileName = '', fileMode = ''):
        self.fileName = fileName
        self.fileMode = fileMode
        self.fileContents = []
        self.fileList = []
        self.fileHeader = []
        if (fileMode == 'r'):
            self.fileOpen = open(fileName, fileMode)
            self.fileHeader = self.fileOpen.readline()
            for filestr in self.fileOpen:
                self.fileContents.append(filestr.strip('\n').split(','))
            self.fileContents.sort()
            self.fileList.append(self.fileHeader)
            self.fileList.extend(self.fileContents)

        elif (fileMode == 'w'):
            self.fileOpen = open(fileName, fileMode)
        else:
            print("Error: syntax error")

    def getStatus(self):
        if(self.fileOpen):
            return True
        else:
            print("Error: file is not opened")
            return False
        

    def getBody(self):
        if(self.fileOpen):
            return self.fileContents
        else:
            print("Error: file is not opened")
            return False
        

    def setContentHead(self, givenfileHeader):
        if(givenfileHeader != []):
            self.fileHeader = givenfileHeader
        elif(givenfileHeader == []):
            self.fileHeader = []
        else:
            print("Error: file is empty or Input is not list")
            return False

    def setContentBody(self, givenfileContent):
        if(givenfileContent != []):
            self.fileContents = givenfileContent
        elif(givenfileContent == []):
            self.fileContents = []
        else:
            print("Error: file is empty or Input is not list")
            return False

    def writeFile(self):
        if(self.fileOpen):
            for head in range(len(self.fileHeader)):
                self.fileOpen.write(self.fileHeader[head])
                if(head != len(self.fileHeader) - 1):
                    self.fileOpen.write(',')
                else:
                    self.fileOpen.write('\n')
            
            for line in self.fileContents:
                for item in range(len(line)):
                    self.fileOpen.write(line[item])
                    if(item != len(line) - 1):
                        self.fileOpen.write(',')
                self.fileOpen.write('\n')
            return True
        else :
            print('Error: file is not opened')
            return False


    def closeFile(self):
        if(self.fileOpen):
            self.fileOpen.close()
            return True
        else:
            print("Error: file is not opened")
            return False

def mergeList(list1, list2):
    newlist = []
    for i in range(len(list1)):
        for j in range(len(list2)):
            if(list1[i][0] == list2[j][0]):
                new = list1[i] + list2[j][1:]
                ave = int((int(list2[j][1]) + int(list2[j][2]) + int(list2[j][3])) / 3)
                new.append(str(ave))
                newlist.append(new)
                continue
    newlist.sort()
    return newlist                


# ANSWER : END

file1 = myFile("inputdata1.csv", 'r')
file2 = myFile("inputdata2.csv", 'r')

print(file1.getStatus())
if (file1.getStatus() != False) and (file2.getStatus() != False):
    newList = mergeList(file1.getBody(), file2.getBody())

    file3 = myFile("output.csv", 'w')
    file3.setContentHead(["ID", "Name", "Course 1", "Course 2", "Course 3", "Average"])
    file3.setContentBody(newList)
    file3.writeFile()
    file3.closeFile()
else:
    print("input file error")

file1.closeFile()
file2.closeFile()