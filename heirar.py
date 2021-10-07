class student:
    def __init__(self,usn,name,age):
        self.usn=usn
        self.name=name
        self.age=age
    def getdata(self):
        self.name=input("enter a name:")
        self.usn=input("usn:")
        self.age=int(input("age:"))
    def display(self):
        print("usn:",self.usn)
        print("name:", self.name)
        print("age:", self.age)
class ugstudent(student):
    def __init__(self,sem,fees,stipend):
        super().__init__('','','')
        self.sem=sem
        self.fees=fees
        self.stipend=stipend
    def getdata(self):
        super().getdata()
        self.sem = int(input("enter sem"))
        self.fees = int(input("enter fees"))
        self.stipend = int(input("enter stipend"))
    def display(self):
        super().display()
        print("sem:", self.sem)
        print("fees:", self.fees)
        print("stipend:", self.stipend)
class pgstudent(student):
    def __init__(self,sem,fees,stipend):
        super().__init__('','','')
        self.sem=sem
        self.fees=fees
        self.stipend=stipend
    def getdata(self):
        super().getdata()
        self.sem = int(input("enter sem"))
        self.fees = int(input("enter fees"))
        self.stipend = int(input("enter stipend"))
    def display(self):
        super().display()
        print("sem:", self.sem)
        print("fees:", self.fees)
        print("stipend:", self.stipend)
while True:
    ch=int(input(" \n 1.UGStudents \n 2.PGstudents \n enter choice "))
    if ch==1:
        ug=ugstudent('','','')
        ug.getdata()
        ug.display()
    elif ch==2:
        pg=pgstudent('','','')
        pg.getdata()
        pg.display()
    else:
        break

