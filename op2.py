from operatoe import *
obj1=op()
obj2=op()
obj1.get_element()
obj2.get_element()
while True:
    print("1.add 2.sub 3.mult")
    choice=int(input("enter the choice:"))
    if choice==1:
        obj1+obj2;
    elif choice==2:
        obj1-obj2;
    elif choice==3:
        obj1*obj2;
    else:
        break