class student:
    def __init__(self):
        self.usn=''
        self.name=''
        self.age=''
    def getdata(self):
        self.name=input("enter a name:")
        self.usn=input("usn:")
        self.age=int(input("age:"))
class derived1(student):
    def __init__(self):
        self.s1=0
        self.s2=0
        self.s3=0
        self.s4=0
        self.s5=0
    def getmarks(self):
        super().getdata()
        self.semester=int(input("sem:"))
        self.sub1=int(input("sub1:"))
        self.sub2=int(input("sub2:"))
        self.sub3=int(input("sub3:"))
        self.sub4=int(input("sub4:"))
        self.sub5=int(input("sub5:"))
class derived2(derived1):
    def __init__(self):
        super().__init__()
    def display(self):
        self.total=(self.sub1+self.sub2+self.sub3+self.sub4+self.sub5)
        self.final=((self.total*100)/500)
        print("usn:",self.usn)
        print("total:",self.total)
        print("percentage:", self.final)
d2=derived2()
d2.getmarks()
d2.display()


