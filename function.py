#  # def f1():
#   s = "I Love Navgurukul"
#    def f2():
#     print(s)
#    f2()

# f1()

# def num ( ):
# 	i=1
# 	while i<=10:
# 		if i%2!=0:
# 			print(i,'odd')
# 	 	i=i+1



# num()
# def num ( ):
# 	i=1
# 	while i<=10:
# 		if i%2==0:
# 			print(i,'even')
# 		i=i+1
# num()



# def num():
# 	num1 = 56
# 	num2 = 12
# 	print(num1+num2)
#num()
# def num(a,b=20):
# 	print(a+b)


# num(2)
# def isEven():
#  if(12%2==0):
#   print("Even Number")
#  else:
#   print("Old Number")
# isEven()


# 	def raw_a():
# 	numbers = [3, 5, 7def sum():
#     age=int(input("enter a number"))
#     if  age>=18:
#         print("eligibal for voting")
#     else:
#         print("not eligibal for voting")
# sum(), 34, 2, 89, 2, 5]


# 	i=0
# 	min=numbers[i]
# 	while i<len(numbers):
# 		if numbers[i]<min:
# 			min=numbers[i]
# 		i+=1
# 	print(min)




# raw_a()
# def reverse():
# 	a= ["Z", "A", "A", "B", "E", "M", "A", "R", "D"]
# 	i=0
# 	while i<len(a):
# 		a.reverse()
# 		i+=1
# 	print(a)
# reverse()


# def sort(a):
# 	a = [6, 8, 4, 3, 9, 56, 0, 34, 7, 15]
# 	i=0
# 	while i<len(a):
# 		j=0
# 		while j<len(a):
# 			if a[i]<a[j]:
# 				a[i],a[j]=a[j],a[i]
# 			j+=1
# 		i+=1
# 	print(a)




# sort([6, 8, 4, 3, 9, 56, 0, 34,])
# def num():
# 	numbers = [1, 2, 3, 4, 5]
# 	i=0
# 	sum=0
# 	while i<len(numbers):
# 		sum=sum+numbers[i]
# 		i+=1
# 	print(sum)



# num()
# def raw_a():
# 	numbers = [3, 5, 7, 34, 2, 89, 2, 5]
# 	i=0
# 	sum=0
# 	while i<len(numbers):
# 		sum=sum+numbers[i]
# 		i=i+1
# 	print(sum)
# raw_a()
# def number( ):
# 	i=0
# 	while i<100:
# 		print("I love you A")
# 		i+=1



# number()
# def sum():
#     age=int(input("enter a number"))
#     if  age>=18:
#         print("eligibal for voting")
#     else:
#         print("not eligibal for voting")
# sum()


# a=int(input("enter a number"))
# b=int(input("enter a number"))
# c=input("enter a oprater")
# if c=="+":
#     print(a+b)
# elif c=="-":
#     print(a-b)
# elif c=="%":
#     print(a%b)
# elif c=="*":
#     print(a*b)
# elif c=="**":
#     print(a**b)


# def add(n,n2):
# 	return n+n2
# def sub(n,n2):
# 	return n-n2
# def divi(n,n2):
# 	return n//n2
# def mod(n,n2):
# 	return n%n2
# def call():
# 	print(add(2,5))
# 	print(sub(10,5))
# 	print(mod(2,4))
# 	print(divi(5,8))
# call()


# def call():
# 	num=int(input("enter a number"))
# 	sum=0
# 	i=1
# 	while i<num:
# 		if num%i==0:
# 			sum=sum+i
# 		i+=1
# 	if num==sum:
# 		print('perfect no',num)
# 	else:
# 		print('not perfect',num)
	
# call()



# def fun():
# 	a=0
# 	i=0
# 	sum=0
# 	while i<3:
# 		n=int(input("enter a number"))
# 		sum=sum+n
# 		a=a+n
# 		i=i+1
# 	print('sum',sum)
# 	print('avg',a/3)
# fun()









#dock quation


 
# a=['abc', 'xyz', 'aba', '1221']
# i=0
# c=1
# while i<len(a):
# 	if a[i]==a[-1]:
# 		c+=1
# 	i=i+1
# print(c)

          
# num()




 
# def sum():
#     list1 =[8, 2, 3, 0, 7]
#     i = 0
#     sum=0    
#     while(i < len(list1)):
#        sum=sum+list1[i]
#        print(sum)
#        i=i+1

# sum()



# def sum():
#     a=[1,2,3,3,3,3,4,5]
#     l=[]
#     i=0
#     while i<len(a):
#         if a[i] not in l:
#             l.append(a[i])
#         i+=1
#     print(l)
# sum()

# bug


# a=5
# def my():
#     b=6
#     print(a+b)
# my()
# print(a,b)



# debug
# a=5
# def my():
#     global b
#     b=6
#     print(a+b)
# my()
# print(a,b)


# bug

# a=20
# def num():
#     b=2
#     p\rint(a*b)
# num()
# print(a,b)


# debug

# a=20
# def num():
#     global b
#     b=2
#     print(a*b)
# num()
# print(a,b)




# 		return 1
# 	else:
# 		return (x * factorial(x-1))
# num = 3
# print("The factorial of", num, "is", factorial(num))


#labda
# my=lambda a: a+10
# print(my(9))

# a=lambda b: b*20
# print(a(4))


#recursion
#i=4
#def my():
	#	if i==1:
		#	print("pooja rani")
	#		my()
#my()


#call one function two onother


# def sum(a,b):
# 	 return a+b
# def multy(c): 
#      return sum(3,6)*c
# print(multy(2))



# nested

# def dhani():
# 	print("pooja")
# 	def swari():
# 		print("roshni")
# 	swari()
# dhani()


# return onother function


 
# def disp():
# 	def show():
# 		return "show function"
# 	print("disp function")
# 	return show

# ris=disp()
# print(ris())


# def disp(sh):
# 	print("disp function")
# 	return sh
# def show():
# 	return "show function"

# ris=disp(show)
# print(ris())


# function call one function two onother function


# def sum(a,b):
# 	c=a+b
# 	print(c)
# def sub(a,b):
# 	c=a-b
# 	print(c)
# 	sum(7,2)
# sub(5,2)


# a=[1,2,3,4,5,6,7,8,9]
# i=1
# l=[]
# while i<len(a):
# 	if a[i]%2==0:
# 		l.append(a[i])
# 		print(l)
# 	i=i+1


	
	
# def sub():	
# 	a=[1,2,3,4,5,6,7,8,9]
# 	i=0
# 	l=[]
# 	while i<len(a):
# 		if a[i]%2==0:
# 			l.append(a[i])
# 		i=i+1
# 	print(l)
# sub()

# def sub():	
# 	a=[1,2,3,4,5,6,7,8,9]
# 	i=0
# 	l=[]
# 	while i<len(a):
# 		if a[i]%2==0:
# 			l.append(a[i])
# 		i=i+1
# 	print(l)
# sub()




# def num():
# 	i=0
# 	while i<=20:
# 		if i%2==0:
# 			print("even",i)
# 		else:
# 			print("odd",i)
# 		i+=1
# num()

# def sub():
# 	n=int(input("enter a no::"))
# 	r=n
# 	a=1
# 	c=0
# 	while a<=n:
# 		if n%a==0:
# 			c=c+1
# 		a=a+1		
# 		if c==2:
# 			print("this is praime num",r)
# 		else:
# 			print("not",r)
# sub()



# num = 1
# def func():
#     global num
#     num = num + 3
#     print(num)

# func()
# print(num)


# def test(x = 1, y = 2):
#     x = x + y
#     y += 1
#     print(x, y)

# test()



# def test(x = 1, y = 2):
#     x = x + y
#     y += 1
#     print(x, y)

# test(2, 1)



# num = 1
# def func():
#     num = 3
#     print(num)

# func()
# print(num)
# print('resturent\n biriyani\n is hot')

# def sum(a,b):
# 	return a+b
# def num(c,d):
# 	return c*d
# print(sum(2,4))
# print(num(3,6))

# factor nikalna

# def sum(user):
# 	i=1
# 	while i<=user:
# 		if user%i==0:
# 			print(i)
# 		i+=1
# sum(10)	



                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     
# def add(n,n2):
# 	l=n+n2
# 	return l
# def sub(a,a2):
#  	m=a-a2
# 	 return m
# def mult(b,b2):
# 	o=b%b2
# def divi(c,d):
# 	return o
# deturn e
# def call():
# 	i
# 	rf op=="+":
# 		print(add(num,num2))
# 	elif op=="-":
# 		print(sub(num,num2))
# 	elif op=="%":
# 		print(mult(num,num2))
# 	elif op=="/":
# 		print(divi(num,num2))
# 	else:
# 		print("nothig")
# num=int(input("enter a number"))
# num2=int(input("enter a number"))
# op=input("enter a opreater")

# call()


	

# words ="navgurukul is great"
# counter = 0
# while counter < len(words):
# 	print (words[counter])
# 	counter+=1


# a = "NavGurukul is an alternative to higher education reducing the barriers of current formal education system"
# b= a.split()

# print(b)

		



# def num(a):
# 	i=0
# 	while i<len(a):
# 		b=a.split(" ")
# 		i+=1
# 	print(b)
# num("NavGurukul is an alternative to higher education ")



# def add(n,n2):
#     l=n+n2
#     return l
# def sub(a,a2):
#     m=a-a2
#     return m
# def mult(b,b2):
#     o=b%b2
#     return o
# def divi(c,d):
# 	e=c/d
# 	return e
# def call():
# 	if op=="+":
# 		print(add(num,num2))
# 	elif op=="-":
# 		print(sub(num,num2))
# 	elif op=="%":
# 		print(mult(num,num2))
# 	elif op=="/":
# 		print(divi(num,num2))
# 	else:
# 		print("nothig")
# num=int(input("enter a number"))
# num2=int(input("enter a number"))
# op=input("enter a opreater")

# call()


# a=4
# def sum():
# 	global b
# 	b=5
# 	print(a+b)
# sum()
# print(a,b)




# nag pos


# def pos():
# 	a= [2, -7, 5, -64, -14]
# 	i=0
# 	c=0
# 	c2=0
# 	while i<len(a):
# 		if a[i]>0:
# 			c+=1
# 		else:
# 			c2+=1
# 		i+=1
# 	print('pos',c)
# 	print('nag',c2)
# pos()	
# 





# defual aregument


# def sum(a,b=5,c=5):
# 	d=a+b+c
# 	print(d)
# a=7
# b=7
# c=9
# sum(a,b,c)


# positional argument

# def num(age,name):
# 	print(age,name)
# num(12,"pooja")




# keyword argument

# def sum(a=5,b=6):
# 	print(a+b)
# sum(4,6)



# arbetrry argument 
# def num(*a):
# 	print(a)
# num(12,345,878,"pooja",76)



# arbetrry keyword argument

# def num(**d):
# 	print(d)
# num(a=3,b=3,c=3)





# nested in function


# def dhani():
# 	print("pooja")
# 	def swari():
# 		print("roshni")
# 	swari()
# dhani()

# def num(a,b):
# 	k=a+b
# 	print(k)
# def sum(c,d):
# 	e=c-d
# 	print(e)
# 	num(6,9)
# sum(6,2)



# def sum(a,b):
# 	c=a+b
# 	print(c)
# def sub(a,b):
# 	c=a-b
# 	print(c)
# 	sum(7,2)
# sub(5,2)


# nested


# def dhani():
# 	print("pooja")
# 	def sawari():
# 		print("rani")
# 	sawari()
# dhani()


# def multy():
# 	print("son")
# 	def don(a,b):
# 		print(a+b)
# 	don(3,5)
# multy()

# def multy():
# 	print("son")
# def don(a,b):
# 	print(a+b)



# def sum(a,b):
# 	 return a+b
# def multy(c): 
#      return sum(3,6)*c
# print(multy)