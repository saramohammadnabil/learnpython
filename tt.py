
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
# methods part two;
#union()
a = {"apple", "banana", "cherry"}
b = {"a", "b", "c"}
x = {1, 2, 3}
print(a.union(b))
print(a | b)
print(a.union(x, b))
#add() add an item to a set, if the item already exists, the add() method does not add it.
#-----
a = {1, 3, 2,4, 6}
a.add(7)
print(a)
#pop() remove and return the element at the given index (default last)
h = [1, 2, 3, 5, 7, "s", "n", "m"]
print(h.pop(5))
#new lesson#
#set{} is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
#slicing not done
mysetone = {"sara", "nana", "bb", 55}
print(mysetone)
#------items is unique الحاجه مره واحده
mysettwo = {"sara", 44, 1,"one", 44}
print(mysettwo)
#clear
a = {1, 2, 3}
a.clear()
print(a)
#union
z = {"one", "two", "three"}
a = {1, 2, 3}
print(z.union(a))
#discard
a = {1, 2, 3, 4, 5}
a.discard(6)
print(a)
#remove
q = {1, 3, 4, 5, 6}
q.remove(3)
#pop in set
c = [1, 2, 4, "true", "r"]
print(c.pop())
#update()
a = {1, 2, "d", "sara"}
h = {"a", "b", "s"}
a.update(["sara", 8 , 8])
a.update(h)
print(a)
#set methhod p2
#difference() method returns a set that contains the difference between two or more sets.
x = {1, 2, 3, 4}
z = {4, 5, 6, 7}
print(x)
print(z.difference(x)) # = print(z-x)
print(x)
print("=" *35)
z = {1, 2, 3, 4}
x = {4, 5, 6, 7}
print(x-z)
print(z-x)
print(x.difference(z))# = z-x + x-z = print(x-z)
print("=" *35)
#difference_update() method removes the items that exist in both sets.
#intersection() method returns a set that contains the similarity between two or more sets.
e = {1, 2, 4, "c", "f"}
w = {7, 8, 1 ,"c", "f"}
print(e)
print(e.intersection(w)) #the same as print(e&w) the similar items
print(w&e)
print(e)
print("=" *35)
#intersection_update() method removes the items that is not present in both sets.
e.intersection_update(w)
print(e)
print("=" *40)
#symmetric_difference() method returns a set that contains all items from both sets, except items that are present in both sets.
d = {1, 2, 3, "b", "k"}
f = {1, 3, 5, 8, "v", "c"}
print(d)
print(d.symmetric_difference(f)) #the same as print(d^f) the items that are in either set but not in both
print(f)
print(d)
print("=" *40)
#symmetric_difference_update() method removes the items that are present in both sets, and inserts the other items.
s = {1, 2, 3, "b", "k"}
t = {1, 3, 5, 8, "v", "c"}
s.symmetric_difference_update(t)
print(s)
print("=" *40)
#dictionary{}
#dictionaries are used to store data values in key:value pairs.
#dictionaries are unordered, changeable and do not allow duplicates.
#dictionariesare written with curly braces, {}, and have keys and values:
#list not allowed
#dict have any type of datatype
#dict key have to be uniqe if has two then will print the last one
userdict= {
    "name": "sara",
    "age": 17,
    "city": "sahag",
    "university": "korea university",
    "country": "egypt",
    "skills":["python", "english", "korean"],
    "gpa": 10.5
}
#len
print(len(userdict))
#print dict  item_>>>>>> []
#get(),keys(),values()
print(userdict)
print(userdict["name"])
print(userdict["skills"])
print(userdict.get("country"))
print(userdict.keys())
print(userdict.values())
#two_dimensional dictionary
progamming_langueges = {
    "the first": {
        "name": "python",
        "level":" beginner"
    },
    "the secondone": {
        "name": "java",
        "level": "intermediate"
    },
     "the third": {
         "name": "c++",
         "level": "advanced"
     }
}
#print(progamming_langueges["the secondone"]["level"])
print(progamming_langueges["the third"]["level"])
print(progamming_langueges["the secondone"]["level"])
#len
print(len(progamming_langueges))
print(len(progamming_langueges["the first"]))
print("_" *50)
#setdefault()
saradict = {
   "name": "sara"
}
print(saradict)
print(saradict.setdefault("name", "sara"))
print(saradict.setdefault("age"))
print(saradict.setdefault("age", 44))
print(saradict)
#popitem
cieradict = {
   "name": "ciera",
   "age": 18

}
print(cieradict)
print(cieradict.update({"skills": "learning"}))
#print(type(cieradict))
print(cieradict.popitem())
print(cieradict)
print(cieradict["name"])
print("______________________________________________")
#items
nanadict = {
   "name": "nana",
   "skill": "play"
}
allitems = nanadict.items()
print(nanadict)
nanadict["age"] = 14
print(allitems)
#fromkeys
a = ("age", "name", "skill")
b = ("x")
print(dict.fromkeys(a,b))
print("_" *50)
#Boolean
name  = ""
print(name.isspace())

print(100 > 200)
print(100 == 100)
print("___________________________________________________")
#bool()
#True values;
print(bool("sara"))
print(bool(13))
print(bool([1, 2, 4, 5,]))
print(bool(12.4))
print(bool(True))
print("___________________________________________________")
#false values
print(bool(0))
print(bool(""))
print(bool([]))
print(bool({}))
print(bool(False))
print(bool(None))
print("__________________________________________________")
#not;
#explain:





print("______________________________________________")
#assigment operators:-
x = 10
z = 20
x = x-z #-10
print(x)
x -= z #-10
print(x)
#
print("_____________________________________________________-")
#comparsion operators
#[==]
#[!=]
#[>]
#[<]
#[>=]
#[<=]
print("____________________________________________")
#type conversion
#str()
x = 3
print(type(x))
print(type(str(x)))
#tuble()
print(")__________________________________________________")
z = [1, 2, 3, 4, 5]
d = {"one": 1, "two": 2, "three": 3}
s = "sara", "xsed"
f = {"sss", "dddd"}
print(tuple(z))
print(tuple(f))
print(tuple(s))
print(tuple(d))
print("______________________________________________-;")
# type conversion# String -> List
text = "Sara" "vava"
print(list(text))
# ['S', 'a', 'r', 'a']

# Tuple -> List
t = (1, 2, 3)
print(list(t))

# Set -> List
s = {1, 2, 3}
print(list(s))

# Dictionary -> List (المفاتيح فقط)
d = {"name": "Sara", "age": 17}
print(list(d))

# Dictionary Values -> List
print(list(d.values()))

# Dictionary Items -> List
print(list(d.items()))
print("________________________________________________")
# List -> Tuple
l = [1, 2, 3]
print(tuple(l))

# String -> Tuple
print(tuple("Sara"))

# Set -> Tuple
print(tuple({1, 2, 3}))

# Dictionary -> Tuple (المفاتيح)
print(tuple({"a": 1, "b": 2}))
print("________________________________________________:")
# List -> Set
l = [1, 2, 2, 3, 3]
print(set(l))
# {1, 2, 3}

# Tuple -> Set
print(set((1, 2, 3)))

# String -> Set
print(set("banana"))
# {'b', 'a', 'n'}

# Dictionary -> Set (المفاتيح)
print(set({"a": 1, "b": 2}))
print("________________________________________________:")
# List of Tuples -> Dictionary
l = [("name", "Sara"), ("age", 17)]
print(dict(l))

# Tuple of Tuples -> Dictionary
t = (("x", 10), ("y", 20))
print(dict(t))

# Set of Tuples -> Dictionary
s = {("a", 1), ("b", 2)}
print(dict(s))
#----------------------------



#-----add() add an item to a set, if the item already exists, the add() method does not add it.
#---------#import time
print("_________________________________________________________________________________-")
#import time
#import sys
#time.sleep(2)
#lyrics = [
    #("Wake up in the morning", 0.08),
    #("Everything's alright", 0.09),
    #("At the end of the story", 0.10),
    #("You're holdin' me tight", 0.10),
    #("I don't need to worry", 0.09),
    #("am I out of my mind?", 0.10),
    #("And, oh, it's hard to see you", 0.08),
    #("", 0.07),  # سطر فاضي
    #("But I wish you were right here", 0.07),
    #("Oh, it's hard to leave you", 0.07),
    #("When I get you everywhere", 0.09),
    #("All this time I'm thinking", 0.08),
    #("I'm strong enough to sink it", 0.09),
    #("Oh, no, I don't need you", 0.08),
    #("But I miss you, come here", 0.06),
#]

#def type_writer(text, speed):
    #for letter in text:
    #    sys.stdout.write(letter)
    #    sys.stdout.flush()
    #    time.sleep(speed)
    #print()

#for line, speed in lyrics:
#    type_writer(line, speed)
#
#username = input("entrer your name please: ")
#password = input("entre your passowrd please: ")
#age = int(input("Enter your age please: "))
#print("your name is: {} and your password is: {} and your age is: {}".format(username,password,age))
#------------#

#num = int(input("Enter a number: "))
#result = num % 2
#if result == 0:
   # print("true")
#else:
    #print("false")
    #---------#
#new problem
#num = input("enter your age:")
#driver_license = input("do U have a driver license?")
#if int(num) >= 22:
    #if driver_license == "yes":
       # print("hiered")
    #else:
        #print("rejected")
#else:
    #print("rejected")

    #--new problem
#num = input("enter your age:")
#driver_license = input("do U have a driver license?")
#recommandition = input("do U have a recommadition?")
#if int(num) >= 44 and driver_license == "yes" and recommandition == "yes":
    #print("hiered")
#else:
    #print("rejected")
    #ennnnddd#
#new problem
#first_name = input("enter your first name;")
#last_name = input("enter your last name;")
#print(first_name +" " + last_name)
#print("your full name is: {} {}".format(first_name,last_name))
#-------endddd#
#new problem$
#half number
#num = int(input("enter  number;"))
#result = num / 2
#r = int(num / 2)
#half number = num /2
#print("the half of the number is: {}".format(result))
#enddd#
#new problem
#spanish_mark = int(input("enter your spanish mark;"))
#english_mark = int(input("enter your english mark;"))
#math_mark = int(input("enter your math mark;"))
#if  spanish_mark >= 80 and english_mark >= 50 and math_mark >= 70:
    #print("pass")
#else:
    #print("failed")
    #endddd#
#new problem
#num = int(input("num one:"))
#num2 = int(input("num two:"))
#num3 = int(input("num three:"))
#print("the sum of the numbers is: {}". format (int(num) + int(num2) + int(num3)))
# هنا عملت format
#enddd#
#new problem لازززم الint()
#طريقه تانيه اسهل
#num1 = int(input("num one:"))
#num2 = int(input("num two:"))
#num3 = int(input("num three:"))
#sum = num + num2 + num3
#print(sum)
#print("the sum of the numbers is: {}".format(sum))
#ennd#
#new problem#
#3 marks ava----
#mark1 = int(input("enter your first mark: "))
#mark2 = int(input("enter your second mark: "))
#mark3 = int(input("enter your third mark: "))
#averge = (mark1 + mark2 +mark3) //3
#if averge >= 50:
    #print("pass")
#else:
    #print("failed")
    #ennddd#
#new problemاول علامتين فقط مهم
#grade1 = (int(input("enter your first grade: ")))
#grade2 = (int(input("enter your second grade: ")))
#grade3 = (int(input("enter your third grade: ")))
#grade4 = (int(input("enter your fourth grade: ")))
#if grade1 >=60 and grade2 >=50:
    #print("pass")
#else:
    #print("failed")
    #endddd#
    #new problem     max of the numbers
#num1 = int(input("enter your first number: "))
#num2 = int(input("enter your second number:"))
#print(max(num1, num2))
#endddd# 
#new problem swap num
#num1 = int(input("enter your first num"))
#num2 = int(input("enter your second num"))
#num3 = int(input("enter your thired num"))
#print(num1)
#print(num2)
#print(num3)
#temp = num1
#num1 = num2
#num2 = temp
#num2 = num3
#num3 = temp

#print(num1)
#print(num2)
#another method
#num1 = int(input("enter your first num"))
#num2 = int(input("enter your second num"))
#num3 = int(input("enter your thired num"))
#print(num1, num2 ,num3)
#num1, num2, num3 = num3, num2, num1
#print(num1, num2, num3)
#neww proooobllleem
#x = int(input("enter the length"))
#y = int(input(" enter the width"))
#area = x*y
#print(f"the erea is {area}")
#enddd#
#import math
#a = int(input("enter the width "))
#d = int(input("enter the diameter"))
#area = a*math.sqrt(d*d-a*a)
#print(area)
#wdedddd
#new problem
#a = int(input("enter the length of the base"))
#h = int(input("enter the hight"))
#area = 1/2*a*h
#print(f"the area of the tringle is {area}")
#neww problem18 circle area
import math
#r = int(input("enter the radius"))
#area =math.pi*r*r
#print(f"the area of the circle is {area}")
#end
#new problem19
# = int(input("enter the diameter"))
#area = math.pi*D*D//4
#print("the area of the circle:" , area)
#end
#20
#area of the circle inscribed in a square
#A = int(input("enter the area of the square: "))
#area = A*math.pi*(A*A)//4
#print("the area of the circle:",  area)
#end
#side = int(input("enter the side of the square: "))
#square_area = side*side
#r = side//2
#area = math.pi*r*r
#print("the area of the square is:", square_area, "and the area of the circle is:", area)
#print("the area of the circle is:", area )
#print("the area of the square is:", square_area)
#end 10/10***
#new problem21
#import math
#circumferance = int(input("enter the circumferance of the circle: "))
#radius = circumferance / (2*math.pi)
#area = math.pi*radius*radius
#print("the area of the circle is:", area)
#print("the circumference of the circle is:", circumferance)
#end other way 

#circumferance = int(input("enter the circumferance of the circle: "))
#area = circumferance*circumferance/ (4*math.pi)
#print("the area of the circle is:", area)
#print("the circumference of the circle is:", circumferance)
#end 
#problem22
#area inscribed in an isosceles triangle
#a = int(input("enter the side of the triangle:"))
#b = int(input("enter the base of the triangle:"))
#pi = 3.14
#area = (pi*b*b/4)*((2*a-b)/(2*a+b))
#triangle_area = (b*math.sqrt(a*a-b*b/4))/2
#print("the area of the circle id:", area)
#print("the area of the triangle is:", triangle_area)
#enddd
#problem23
#a = int(input("enter the side of the triangle: "))
#b = int(input("enter the base of the triangle: "))

#hight = math.sqrt(a*a-b*b/4)# math.sqrt(a**2-b**2/4)
#pi = 3.14
#traingle_area = (b*hight)/2
#s = (a+a+b)/2
#radius = traingle_area/s
#circle_area = pi * radius * radius
#print("the area of the triangle is:", traingle_area)
#print("the area of the circle is:", circle_area)
#print(hight)
#print(radius)
#print(s)
#print(traingle_area)
#triangle_area = (b*math.sqrt(a*a-b*b/4))/2 if no hight
#end
#new problem24
#a = int(input("enter the first side of the tringle: "))
#b = int(input("enter the second side of THe tringle: "))
#c = int(input("enter the third side of the tringle: "))
#pi = 3.14
#p = (a+b+c)/2
#T = (a*b*c) / (4*math.sqrt(p*(p-a)*(p-b)*(p-c))) #important formula
#area = pi*T*T
#print("the area of the circle is:", area)
#end
#validate age beteeen 18 and 60
#age =int(input(" enter your age: "))
#if age >=18 and age<=55:
    #print("you are eligible to work")
#else: 
    #print("you are not eligible to work")
    #end
while True:
    age =int(input(" enter your age: "))

    if age >=18 and age<=55:
       print("you are eligible to work")
       break
    else: 
       print("you are not eligible to work")
       #end
#print num from 1 to N
#N = int(input("enter a num: "))
#x = 0
#while True:
      #x = x+1
      #print(x)
      #if x == N:
        #break
      #another way to solve
#N = int(input("enter N:   "))
#x = 0
#while x < N:
      #x = x+1
      #print(x)
#end
#new problemmmm25
#N = int(input("enter N : "))
#counter = N+1
#while True: 
 #   counter = counter - 1
 #   print(counter)

 #   if counter == 1:
  #      break
#new problem 26
#sum odd nums from 1 to N
#N = int(input("enter N : "))
#counter = 0
#total = 0
#while True:
    #counter = counter + 1
    #if counter % 2 != 0:# odd # if counter % 2 == 1
         #total = total + counter
    #if counter == N:
        #break
#print(total)#new one 27
#N = int(input("enter N2 ;"))
#counter = 0
#total = 0
#while True:  # or while counter < N
#     counter = counter +1
#     if counter % 2 == 0: # if counter % 2 != 1
#         total = total + counter 
#     if counter == N: # no  use if 684 exist
#         break  # no too
#print(total)
#new one 28
# factorial num
N = int(input("enter N ''' "))
while  N <= 0:
  N = int(input("enter again; "))
counter = 1 + N 
factorial = 1
while True:
   counter = counter - 1
   factorial = counter * factorial
   if counter == 1:
      break
print(factorial) #****
#end
#new ***** prrrrraaavvvOOOOO
N = int(input("enter N :"))
M = N**2,N**3,N**4
#print(M)
print(f"square is:{N**2}, cube is:{N**3}, power is:{N**4}")
#print(N**2)         
#print(N**3)
#print(N**4)
 #_________________________________________
#power**M
N = int(input("enter N/ "))
M = int(input("enter M;"))
p = N**M
print(p)
#another way to solve
N = int(input("enter N/ "))
M = int(input("enter M;"))
P = 1
counter = 0
while counter < M:
 P = P * N 
 counter +=1
print(P)
#end_______________________________________
#G = int(input("enter Grade : "))
#if G >90 and G <= 100:
    #print("Grade is A")
#elif G >=80 and G <= 89:
    #print("Grade is B")
#elif G >=70 and G <= 79:
    #print("Grade is C")
#elif G >=60 and G <= 69:
    #print("Grade is D")
#elif G >=50 and G <= 59:
    #print("Grade is E")
#else:
    #print("Grade is F")
    #________________________________________________
    #another problem
#X = int(input("enter X: "))
#Z = int(input("enter Z: "))
#counter = 1
#while True:
    #counter = 1
   # while counter <=Z:
      # print(f"{X}^{counter} = {X**counter}")
      # counter = counter +1
     #  if counter > Z:
     #       break
       #_______________________
#new promlem
T = int(input("enter totalsales: "))
if T > 1000000:
   print("bounse is 1% of the total sales")
elif T > 5000000 and T <=1000000:
   print("bounse is 2% of the totalsales: ")  
elif T > 100000 and T <= 500000:
    print("bounse is 3% of the totalsales: ")
elif T > 50000 and T <= 100000:
    print("bounse is 4% of the totalsales: ")
else:
    print("bounse is 0% of the totalsales: ")
#---------------------------------------------
#piggy bank calculator
P = int(input("enter the nums of pennies : "))
N = int(input("enter the nums of the nickles : "))
D = int(input("enter the nums of the Dimes : "))
D2 = int(input("enter the nums of the dollars : "))
Q = int(input("enter the nums of the Quarters : "))
total_cents = P + N * 5 + D * 10 + D2 * 100 + Q * 25
print(f"the total amount of the monney in the piggy bank is : {total_cents}    cents")
#__________________neewwwww onnneee 

 