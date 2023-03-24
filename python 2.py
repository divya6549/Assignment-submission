#!/usr/bin/env python
# coding: utf-8

# In[14]:


print("hello world")


# In[15]:


print("hello"+"bob")


# In[16]:


x=int(input())
y=int(input())

print("summation of two numbers",x+y)


# In[ ]:


# strings are a set of character that are an array of bytes representing unique code characters.


# In[ ]:


# python variable start with an alphabatic characters and \ or connected by underscore.


# In[ ]:


# variables when printed are not in codes.


# In[ ]:


# we can add variable as long as we add string to string and no.to no.


# In[ ]:


# string and integer cannot be add.


# In[ ]:


# default datatype of your input variable is a string until and unless it is typecasted.


# In[ ]:


# Typecasting-In typecasting,the compiler automatically changes one data type to another one depending on what we want program
to do.# for eg. we assign a float variable with an integer value, the compiler will ultimately convert this int value into float 
value.


# In[ ]:


#= , space
#= + no space


# In[ ]:


# Argument- an argument is a value that passed into the function as its input when we call its function.
# it is a value given for a parameter when calling a function.
# Parameter- is a variable which we used in the function defination.


# In[17]:


x=4
y=5
z=x+y
print(z)


# In[18]:


x= float (input("enter first number: "))
y= float (input("enter second number: "))
#z= x+y
#z= x*y
#z= x/y
#z= x-y
print("summation is:",x+y)
print("multiplication is:",x*y)
print("division is:",x/y)
print("subtraction is:",x-y)


# # Boolean Strings Methods

# In[19]:


x= "hel100_303"
x.isalpha()
# above extension checks wether given value is alphabet or not.


# In[20]:


x= "hel100_303"
x.isalnum()
# checks value is alphanumeric or not. 
# reason for false is underscore b\w no.


# In[21]:


y= "Hello world, how have you been?"
y.istitle()
# each string seperated by space has uppercase letter.


# In[22]:


x= "42515"
x.isdigit()
# returns true if all the character are digits otherwise false.


# In[23]:


y.islower()
# checks the value whether it is in lower case or not.


# In[24]:


y.isupper()
# checks the value whether it is in upper case or not.


# In[25]:


a= "morrow,chrollo"
a.startswith("m")
# this method returns whether value assigned or entered starts with that particular value.


# # String Formatting Method

# In[26]:


x= "kuch bhi likh do"
x.capitalize()
# it capitalize first character of a string.


# In[27]:


x.upper()


# In[28]:


x.lower()


# In[29]:


x.swapcase()
# all characters of a string are made to switch from upper to lower and lower to upper.


# In[30]:


x.title()
# makes the first letter of each word in capital.


# In[31]:


x="itsme05"
x.isalpha()


# In[32]:


x.isalnum()


# In[33]:


y="hello03"
y.isalnum()


# In[34]:


x="hey,its me"
x.istitle()


# In[35]:


y="Hey,Its Me"
y.istitle()


# In[36]:


y.islower()


# In[37]:


y.isupper()


# In[38]:


y.startswith("h")


# In[39]:


a="today is a good day"
a.capitalize()


# In[40]:


a.lower()


# In[41]:


a.upper()


# In[42]:


a.swapcase()


# In[43]:


a.title()


# In[44]:


z="23451"
z.isdigit()


# In[45]:


b="_23451"
b.isdigit()


# In[46]:


7%7
# %-gives remainder


# In[47]:


6//7
# //-gives quotient


# In[48]:


4*2
# single star represents multiplication.
4**2
# double star represents power.


# In[49]:


x=(3+2*4/2**4)
# parantheses
# exponential or power
# multiplication,division and remainder
# add and sub
# left to right


# In[50]:


a=int(input("Enter a number"))


# In[51]:


a//10


# In[52]:


a%10


# In[53]:


a[-1]


# In[54]:


x=a//10
y=x%10
print(y)


# In[55]:


x=a//10
y=a%10
a=x
print(y)


# In[56]:


x=a//10 
y=a%10
a=x
print(y,"###",a)


# In[57]:


x=a//10
y=a%10
print(a)


# In[58]:


a=input()
length=len(a)

a=int(a)
sum=0
for i in range(length):
    x=a//10
    y=a%10
    a=x
    sum+=y
    print("final",sum)


# In[59]:


153%10


# In[60]:


153//10


# In[61]:


15//10


# In[62]:


15%10


# In[63]:


# equality operator
2==2


# In[64]:


# unequality operator
2!=2 


# In[65]:


3<=4 


# In[66]:


3>=4 


# In[67]:


# AND
# true and true= true
# true and false= false
# false and false= false
# false and true= false


# In[68]:


((4>5)and(5>4)or(7>2))


# In[69]:


not((5>=5)and(6>3))or((4<2)and(7<6))


# In[70]:


x= float(input())
#x= 42

# evenly divides by 2
# remainderis 0


if x%2==0:
    print("voila,number is even")
else:
    print("Eh, its odd ")


# In[71]:


x=int(input())
y=int(input())
  

if x>y:
    print(x, "is larger number")
    
    
else:
    print(y, "is larger number")


# In[ ]:


Q. write a code to generate a grading system
subjects- maths,science,hindi,english
1. marks greater than 90 in both maths and science then assign "technical" grade
2. marks greater than 85 in either eng or hindi then assign "linguist" grade
3. ''     ''      ''  90          science or maths and marks greater than equal to 85 in either eng or hindi,assign 'smart'grade.
4.                    95 in either maths or science,assign 'prodigy' grade.
5.                    90 in all then assign, 'savant' grade.


# In[72]:


m=int(input("enter maths marks"))
s=int(input("enter science marks"))
h=int(input("enter hindi marks"))
e=int(input("enter english marks"))

if(m>90 and s>90):
  print("grade=technical")
    
elif(e>85 or h>85):
    print("grade=linguist")
    
elif((s>90 or m>90)) and ((e>=85 or h>=85)):
    print("grade=smart")
    
elif(m>95 or s>95):
    print("grade=prodigy")
    
elif(m>90 and s>90 and h>90 and e>90):
    print("garde=savant")
    
else:
    print("grade=fail")
    


# In[ ]:


# code first run the first statement and if it is true it will skip the rest of the statements.
# it checks the condition in order.
# it will only check if it is true.


# In[ ]:


# identation- to make code more readable.


# In[ ]:


# recursion- call a function within function.


# In[ ]:


#break statement ends the current code line and jump out of the block.
# continue- it will skip and continue.


# # functions

# In[4]:


def lyrics():
    
    print("-----")
    print("-----")
    print("@@@@@")


# In[5]:


lyrics()


# In[6]:


def maximum(x,y):
    if x>y:
        return x
    else:
        return y


# In[7]:


maximum(42,42)


# In[7]:


def greet(lang):
    if lang == 'esp':
        return "Hola"
    elif lang == 'eng':
        return "Hey"
    elif lang == 'fr':
        return "Bonjour"
    else:
        return "Hi"


# In[6]:


x = greet("fr") + "marion"


# In[8]:


def sum_of_digits(x):
    sum=0 
    while(x>0):
        sum = sum + x%10
        x = x//10
    return sum
    
    sum_of_digits(1729)


# In[21]:


x=int(input("enter a number"))
def order(x):
    n=0
    
    while x != 0:
        n=n+1
        x=x//10
        
        return n
    
print(order(x))
    
   


# In[47]:


num=int(input("enter a 3 digit number")
  
        
  temp = num
sum = 0
        
while temp > 0:
    digit = temp % 10
    sum+= digit*digit*digit
    temp = temp // 10
    
    if sum == num:
        print('it is an armstrong number')
    else: 
        print('it is not armstrong number')


# In[37]:


#f-string method

x="harshit"
y='adil'

print(f"hello {x}, how are you {y}?")

f"something here {x} and then something here as well {y}"


# ##### print("hello", x, ", how are you", y, "?")

# In[5]:


# .format method
"string here {1} then something here {0}" .format("harshit" ,"adil")


# In[8]:


template= '{0} {1} are worth US${2}'
template.format(4.5660, "Argentine peso", 1)


# In[9]:


'{0:.2f} {1:s} are worth US${2:d}' .format(4.5660, 'Argentine Peso', 1)


# In[13]:


def fact(x):
    if(x==0):
        return 1
    else:
        return x*fact(x-1)
    
x=int(input("input a no"))
fact(x)
                    


# In[ ]:


def fibb(x):
    y=0
    z=1
    while(x>=0):
        temp=y+z
        y=z
        z=temp
print(temp) 
x += 1
fibb(5)


# In[9]:


def product_of_digit(x):
    p=1
    while(x!=0):
        p=p*(x%10)
        x=x//10
        print(p)
x=int(input("enter a no"))
product_of_digit(x)
            


# In[ ]:


# convocational time
# stored in which memory


# In[11]:


# indexing
# mutable - which can be changed
# immutable - which cannot be changed

x=[1,2,3,"hello"]
x[0]="kill"


# In[ ]:


# list have heterogenous data type
# mutable


# In[12]:


x = "hello world"
len(x)


# In[15]:


# indexing notation uses squrae bracket after the string or variable assign to string.
# it allows you grab a single character from string.
x="hello world"
x[4]


# In[20]:


# slicing- it allows u grab a substraction of multiple characters, a slice of a string.
x= "can i sit here"
# [start:stop:step/stride]
x[4:9]
x[4:13:2]


# In[21]:


y= "today i was late"
y[2:50:3]


# In[22]:


y= "today i was late"
y[-2:50:3]


# In[20]:


# give position and find no.
def total(x,z):
    if(z>x):
        print("NA")
while(z!=0):
    a=x%10
    x=x//10
    z=z-1
    print(a)
total(3246,2)


# In[22]:


# prime no.s
def prime(x):
    count=2
    while(count<x):
        y=x%count
        z=count-1
        if(x==z):
            print("yes")
        elif(y==0):
            print("no")
        else:
            count=count+1
        prime(13)


# In[1]:


n=int(input("enter a number:"))
result=n**0.5
print("square root of",n,"is:",result)


# In[2]:


import math
n=float(input("enter the number:"))
result=math.sqrt(n)
print("square root of",n,"is:",result)


# In[ ]:


# while loop is identifier
# PASS: pass is the "no-op" statement in python.It can be used in black where no action is to be taken (or as a placeholder for code)


# In[ ]:


# range: range function
syntax same as slicing


# In[3]:


range(5)


# In[4]:


list(range(0,20,2))


# In[6]:


list(range(5,0,-1))
x=0


# In[7]:


range(6)
#interacting variable


# # For Loop

# In[8]:


seq=[1,2,3,4]
for i in seq:
    print(x)


# In[ ]:


# keyword is used to test if an item is in an itrating object-membership
seq=(1,2,3,4)
8 is not in seq
is and is not are identity operator that are used to check if two variables are located on the same part of memory.they are like
list, tuple


# In[7]:


num=int(input("enter a number"))
for i in range(10,0,-1):
    print(num,"x",i,"=",num*i)


# In[13]:


# Mailing Address
# create a program that display your name and complete mailing address formatted in the manner that you would usually see it on
# the outside of an envelope. your program does not read to read any input from the user.
def personal_address():
    Name , age = "disha" , "20"
address = "kota", "India"
print("Name: {}\nAge: {}\nAddress: {}".format(Name,Age,Address))

personal_details()


# In[19]:


demo=(1,2,3)
t1=(1,4,(2,3),'John','jane')
t2=(t1[2],t1[3])
print(t2)
print((2,3)in t1)
print(1 in t2)


# In[18]:


# create list conatining elements 1,7,[4,9],('a' ,'b'),'f'
# add element 'g' to end of list
# using slicing create another list containing last two elements of list.

a=[1,7,[4,9],('a','b'),'f']
a.append('n')
print(a)
a=(a[4],a[5])
print(a)


# In[ ]:


# join all element of tuple into string #hint using string join method.


# In[11]:


def compute_lcm(x,y):
    
    if x > y :
        greater = x
    else:
        greater = y
        
    while(True):
            if ((greater % x == 0) and (greater % y == 0)):
                lcm = greater
                break
            greater += 1
    return lcm

num1 = 54
num2 = 24

print("the lcm is", compute_lcm(num1,num2))


# In[14]:


demo=[1,2,3,4,7]


# In[17]:


for i in range(len(demo)):
    print(demo[i])


# In[18]:


list = ['red','black','blue','green']
i=0
while i< len(list):
    print(list[i])
    i += 1


# In[21]:


spam_words = ["make a lot of money","buy now","subscribed this","click this","you won","discount","coupon"]

text = input("enter some text:")
contains_spam = False
   For word in spam words:
    if word in text.lower():
        conatins_spam = True
        break
        
        if conatins_spam:
            print("this text is spam")
            
            else:
                print("this text is not spam")


# In[1]:


a=int(input("enter a number:"))
x=a//10
y=a%10
a=x
print(y,"###",a)


# In[5]:


a=input()
length = len(a)

a=int(a)
sum=0
for i in range (length):
    x=a//10
    y=a%10
    a=x
    sum+=y
    print("final",sum)


# In[17]:


x=int(input("enter a number:"))
def sum_of_digits(x):
    sum=0
    while(x>0):
        sum=sum+(x%10)
        x=x//10
    return sum

x=1729
print(sum_of_digits(x))


# In[ ]:




