class person:

	def hello(self,name,age):
		print("------------------")
		if not(name):
			print("hello",age)
		elif not(age):
			print("hello",name)
		elif (not(name) and not(age)):
			print("hello")
		else:
			print("hello",name,age)

p1=person()
while True:
	print("-----------------\n 1.with name and age \n 2.with name without age \n 3.without name with age \n 4.without name and age")
	ch=int(input("enter your choice:"))
	if ch==1:
		name=input("enter name:")
		age=input("enter age:")
		p1.hello(name,age)
	elif ch==2:
		name=input("enter name:")
		p1.hello(name,' ')
	elif ch==3:
		age=input("enter age:")
		p1.hello(' ',age)
	elif ch==4:
		p1.hello(' ',' ')
	else:
		break