
print("Hello World \\")

print("\"Hello Sara\"\n\" Happy Birthday\" ")
print("Hello\tWorld")
print("6574\rur")
print("diejde\r76849")
age=15
print("\"Hello Sara \\\"\n\"drd\" ")

print("\x41\x42")
print("\x53\x41\x52\x41")
print("Hello\
jfjjr\
fjuj")
print("Hllo+=0\\")
mssg="Hello"
sad="sara"
print(mssg+sad)
bgf=(mssg+sad)
print(bgf)
a="\\\"\sara \
nana\\\"\ "
b="first \
second"
print(a+"\n"+b)

MIA="SARA NANA MEDO"
print(MIA [1:5])
print(MIA[0:6])
print(MIA [0:8])
print(MIA [0:13:5])
print(MIA[0:2], MIA [5:7], MIA[10:12])
print(MIA[0:4], MIA[10:14], MIA[5:9])
print(len(MIA))



#stripprint
masseg ="   happy birthday   "
print(len(masseg))
print(masseg.strip())
print(masseg.lstrip())
print(masseg.rstrip())
print(len(masseg.rstrip()))

text="    i am sara i am 16y old   "
print(text.title())

print(text.capitalize())
print(len(text))
print(text.lstrip())
print(len(text.lstrip()))

num,sos,eee,rrr="3","4","15","188"
print(num.zfill(4))
print(eee.zfill(4))
print(sos.zfill(4))
print(rrr.zfill(4))
print("jrfjrfjr")
a,s,e,r="3","77","99","122"
print(a.zfill(5))
print(s.zfill(5))
print(e.zfill(5))
print(r.zfill(5))

#split () #rsplit()

text="Hello sara and wellcom back hear"
print(text.split())
print(text.rsplit(" ",4))
print(text.split(" ",3))

text="Hello_sara_and_wellcom_back_hear"
print(text.split("_",4))
print(text.rsplit("_",2))

#center() نعد اكتر من ال text
s="sara"
print(s.center(12))
print(s.center(12, "@"))
print(s.center(8,"j"))

#count()
text="hello sara hope u nice day sara "
print(text.count("sara"))
print(text.count("sara",0))
print(text.count("sara",11))

#swapcase()
a = "sara"
print(a.swapcase())
#------------
#index()
a = "hello sara and welcome here "
print(a.index("m"))
print(a.startswith("m" ,20 ,27 ))
print(a.find("m" , 0, 7))
print(a.index("d"))
print(a.endswith("d" ,0 ,14))
#-----------
#find()
#woks just like index but when not find => -1

#----------
#splitlines
date = "Hello#sara#welcome"
print(date.rsplit("#" , 1))
dateq = "sara\nmohammed nana"
print(dateq.splitlines())
#-----------
#expandtabs()
text = "sara\tNANA\t"
print(len(text))
print(text)
r = "sara  nana"
print(len(r))
print(text.expandtabs(4))
#----------
#is family
print("sara132".isalpha())
print("saea".isalpha())
print("nana123".isalnum())
print("baba".isalnum())
#---------
#islower (true if all letters are lowercasw) ("") 
#istitlt(true if each word stars with a capital lettrs)("")
#identifire(true if a string can be a variable in rython)("")
#isspace(true if a stringonly contains spaces)("")
#----Done----#
#new lesson
sds = 4+5j
print(type(sds))
print("real part is: {}".format(sds.real))
print("imaginary part: {}".format(sds.imag))
name = "Sara"
age = 17
motte = "love sis & bro"
print("my nsme is: {} and mt age is: {} and my motte is: {}" .format(name,age,motte))
#int
print(3)
print(float(3))
print(complex(3))
#cannot convert complex to any type
#float
print(2.4564)
print(complex(2.4564))
print(int(2.4564))
#lists method part1
#ARITHEMTIC OPERETORS
#lists[]
#str[" "]
#lists use index
#lists mutable...add,delet,edit
#lists can have diff date types

mylist = ["one" , "two" , "three" , 4 ,9 ,False]
mylist[2] = 3
mylist[5] = 0
print(mylist)
mylist[5] = "true"
print(mylist)
mylist[0:3] = []
print(mylist)
print(type(mylist[-1]))
print(mylist[0:4])
print(type(mylist[2]))
print(mylist)
mylist[0:3] = ["a" ,"d" ,"e"]
print(mylist)
mylist.append("eee")
oldlist = ["cdr" , "hnh"]
mylist.extend(oldlist)
print(mylist)
mylist.append(oldlist)
a = [2 , 4 , 5]
t = ["a" , "b" , "d"]
a.extend(t)
print(a)
ted = ["3" , "7"]
led = ["r" , "erdfjfn"]
ted.extend(led)
print(ted)
ted.append(led)
print(ted)

print(ted[4][1])
#remove() remove the first item with the specified value
x = [2, 3, 5, 6, "sara" , "fdhd" , "hahahahahaha"]
x.remove("sara")
print(x)
a = [1, 9, -4, 6, 98,]
a.sort()
print(a)
z = [9, 0, 7, 3, 5, 89, 9, 454, -34, -5]
z.sort(reverse=True)
print(z)
z.sort(reverse=False)
print(z)

#reverse()
c = [12, 3, 5, "g", "f", "ff", 100]
c.reverse()
print(c)
#part2
#-----------#
#CLEAR
x = [1, 2, 4, 6,]
x.clear()
print(x)
#copy
a = [1, 2, 3,]
b = a.copy()
print(a)#main list
print(b)#copy one
a.append(4)
print(a)
b.append(5)
print(b)
#count() return the number of times a specified value appears in the list
p = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3]
print(p.count(3))
#index() return the index of the first element with the specified value
a = [1, 2, 3, 4, 5, "sara", "nana", "mohammed"]
print(a.index("nana"))
print(type(a.index("sara")))
print(a[5])
#-------
#insert() insert an element at a given position
a= [1, 2, 3, 4, 5, "sara", "nana", "mohammed"]
a.insert(5, 6)
print(a)
a.insert(0, "hola")
print(a)
a.insert(-1, "maha")
print(a)
#-----
#pop() remove and return the element at the given index (default last)
h = [1, 2, 3, 5, 7, "s", "n", "m"]
print(h.pop(5))
    #---------#
username = input("entrer your name please: ")
password = input("entre your passowrd please: ")
age = int(input("Enter your age please: "))
print("your name is: {} and your password is: {} and your age is: {}".format(username,password,age))
#------------#

num = int(input("Enter a number: "))
result = num % 2
if result == 0:
    print("true")
else:
    print("false")
    #---------#
#new problem
num = input("enter your age:")
driver_license = input("do U have a driver license?")
if int(num) >= 22:
    if driver_license == "yes":
        print("hiered")
    else:
        print("rejected")
else:
    print("rejected")

    #--new problem
num = input("enter your age:")
driver_license = input("do U have a driver license?")
recommandition = input("do U have a recommadition")
if int(num) >= 44 and driver_license == "yes" and recommandition == "yes":
    print("hiered")
else:
    print("rejected")
    #ennnnddd#
#new problem
first_name = input("enter your first name;")
last_name = input("enter your last name;")
#print(first_name +" " + last_name)
print("your full name is: {} {}".format(first_name,last_name))
#-------endddd#
#new problem$
#half number
num = int(input("enter  number;"))
result = num / 2
#half number = num /2
print("the half of the number is: {}".format(result))
