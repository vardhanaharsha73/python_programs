class emp:
    def __init__(self,first,last,empid,pay):
        self.first=first
        self.last=last
        self.empid=empid
        self.pay=pay
    def apply_raise(self):
        raise1=1.04
        self.pay=self.pay*self.apply_raise
        return self.pay
class developer(emp):
    raise1=1.05
    def apply_raise(self):
        self.pay=self.pay*self.raise1
        return self.pay
class manager(emp):
    raise1=1.06
    def apply_raise(self):
        self.pay=self.pay*self.raise1
        return self.pay
d={}
while True:
    print("1.print Developer employee details:")
    print("2.print Manager employee details:")
    ch=int(input("enetr choice:"))
    if ch==1:
        first=input("enter your first name:")
        last=input("enter your last name:")
        empid=input("enetr empied:")
        pay=int(input("enter pay:"))
        emp1=developer(first,last,empid,pay)
        print("inital pay:",emp1.pay)
        print("pay after raises:",emp1.apply_raise())
        d[emp1.empid]=emp1.__dict__
        print(d,"\n")
    elif ch==2:
        first=input("enter your first name:")
        last=input("enter your last name:")
        empid=input("enetr emp-id:")
        pay=int(input("enter pay:"))
        emp1=manager(first,last,empid,pay)
        print("inital pay:",emp1.pay)
        print("pay after raises:",emp1.apply_raise())
        d[emp1.empid]=emp1.__dict__
        print(d,"\n")
    else:
        break
        print("invalid choice")