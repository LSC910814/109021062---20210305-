class Student:
    def __init__(self, name, nameid, nickname, height, bodyweight): 
        self.StudentName= name
        self.StudentNameId= nameid
        self.StudentNickName= nickname
        self.StudentHeight= height
        self.StudentBodyWeight=bodyweight
    def showinfo(self):
        print (self.StudentName,"\t",self.StudentNameId,"\t",self.StudentNickName,"\t",self.StudentHeight,"\t",self.StudentBodyWeight)
x1=Student("王小明","103022542","小明","170","55")
x2=Student("陳小新","108005553","新仔","190","80")
x3=Student("郭小宏","107022354","宏宏","180","70")

x1.showinfo()
x2.showinfo()
x3.showinfo()