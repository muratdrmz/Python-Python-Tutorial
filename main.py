# STUDY CODES ================================

# first_name='Murat'
# last_name='Durmaz'
# full_name=first_name +' '+ last_name

# print('hello'+ ' '+full_name)

# age=21
# age=age+1
# age+=1
# print(age)
# print(type(age))
# #print('your age is:' +str(age))

# height=250.5
# print('your height is:'+str(height) +'cm')
# print(type(height))

# human=False
# print(human)
# print(type(human))

# human=True
# print('are you a human:'+str(human))

# name='Bro Code'
#print(len(name))
#print(name.find('C'))
#print(name.capitalize())
#print(name.upper())
# print(name.lower())
# print(name.isdigit())
# print(name.isalpha())
# print(name.count('o'))
# print(name.replace('o','x'))
# print(name*3)

# x=1 #int
# y=2.0 #float
# z='3' #str

# y=int(y)
# y=str(y)
# # z=int(z)
# z=float(z)
# print(x)
# print(y)
# print(z)

# name=input('What is your name?:')
# age=int(input('how old are you?:'))
# height=float(input('how tall are you?:'))

# age=age+5

# print(name +' is '+ str(age) + ' years old' + str(height) +'tall')
# # print('hello'+ " "+name)

# import math


# pi=3.15
# x=1
# y=2
# z=3

# print(round(pi))
# print(pow(pi,2))
# print(math.sqrt(4))
# print(math.floor(pi))
# math.ceil
# math.floor
# abs
# print(max(x,y,z))
# print(min(x,y,z))

# SLICING indexing[] or slice() [start:stop:step] ================================

# name= 'Bro Code'

# first_name=name[2:5]
# last_name=name[4:6]
# funky_name=name[0:8:2]
# reversed_name=name[::-1]

# # print(first_name)
# # print(last_name)
# # print(funky_name)
# print(reversed_name)

# website='http://google.com'

# print(website[slice(7,-4)])

# if statements

# age=int(input('how old are you?:'))

# if age >=18:
#     print('you are an adult!')
# elif age==100:
#     print('you are a century old')
# elif age<0:
#     print('you havent een born yet')
# else:
#     print('you are a child')


# Logical operators   and or  not ================================

# temp=int(input('what is the temperature outside?:'))

# if not(temp>=0 and temp<=30):
#     print('t is good')
#     print('go out')    
# # elif temp<0 or temp>30:
# #     print('temp bad')
# #     print('stay')

# WHILE LOOP ================================
# name=""
# name=None

# while not name:
#     name=input('enter your name')

# # while len(name)==0:
# #     name=input('enter your name')

# print('hello '+name)


# FOR LOOP ================================

# for i in range(10):
#     print(i+1)

# for i in range(5,10+1,2):
#     print(i)

# for i in 'Bro Code Actually':
#     print(i)
# import time
# for seconds in range(10,0,-1):
#     print(seconds)
#     time.sleep(1)
# print('happy new year')

# NESTED LOOPS ================================

# rows=int(input('how many rows?:'))
# columns=int(input('how many columns?:'))
# symbol=input('enter a symbol to use:')

# for i in range(rows):
#     for j in range(columns):
#         print(symbol,end='')
#     print()

# loop control statements change a loops execution from its normal sequence

# break termínate the loop entirely
# continue skips to the next iteration of the Loop
# pass does nothing 

# while True:
#     name=input('enter your name')
#     if name!='':
#         break

# phone_number='123-456-7890'
# for i in phone_number:
#     if i=='-':
#         continue
#     print(i,end='')

# for i in range(1,21):
#     if i==13:
#         pass
#     else:
#         print(i,end='')


# LIST => ================================
# Store multiple items in a single variabl

# food=['pizza','hamburger','hotdog','spagetti','pudding']
# food[0]='sushi'
# print(food[0])

# for x in food:
#     print(x , end='')

# print(food)
# food.append('ice')
# print(food)
# food.remove('hotdog')
# print(food)
# food.pop()
# print(food)
# food.insert(0,'cake')
# print(food)
# food.sort()
# print(food)
# food.clear()
# print(food)


# 2D LISTS list of lists  ================================

# drinks=['coffee','soda','tea']
# dinner=['pizza','hamburger','hotdog']
# dessert=['cake','ice cream']

# food=[drinks,dinner,dessert]
# print(food[0][0])

# TUPLE ================================
# group data together 

# student=('bro',21,21,21,'male')
# # print(student.count(21))
# # print(student.index('male'))

# for x in student:
#     print(x)

# if 'bro' in student:
#     print('bro is here')

# SET ================================

# utensils={'fork','spoon','knife','knife'}
# dishes={'bowl','plate','cup','knife'}

# utensils.add('napkin')
# utensils.remove('fork')
# utensils.clear()
# utensils.update(dishes)
# dinner_table=utensils.union(dishes)

# for x in utensils:
#     print(x,end=' ')

# for x in dinner_table:
#     print(x,end=' ')

# differ=utensils.difference(dishes)
# differ=utensils.intersection(dishes)

# print(differ)


# DICTIONARY ================================

# capitals={
#     'USA':'Washington DC',
#     'India':'New Delhi',
#     'China':'Beijing',
#     'Russia':'Moscow'}
# for key,value in capitals.items():
#     print(key,value)

# capitals.update({'Germany':'Berlin'})
# capitals.update({'USA':'Las Vegas'})

# # print(capitals['Russia'])
# # print(capitals.get('Germany'))
# # print(capitals.keys())
# # print(capitals.values())
# # print(capitals.items())

# for key,value in capitals.items():
#     print(key,value)

# capitals.pop('China')
# for key,value in capitals.items():
#     print(key,value)

# INDEX OPERATOR [] ================================  

# name='bro Code!'

# # if(name[0].islower()):
# #     name=name.capitalize()

# first_name=name[:3].upper()
# last_name=name[4:].lower()
# last_character=name[-2]

# print(first_name, last_name, last_character)

# FUNCTION => ================================
# a block of code which is executed only when it is called invoked

# def hello(first_name,last_name,age): #prameters
#     print('hello '+ first_name+' '+last_name)
#     print('You are '+str(age)+' years old')
#     print('have a nice day')

# hello('bro','code',21) # arguments


# RETURN STATEMENT => ================================
# functions send Python values/objects back to the caller

# def multiply(num1,num2):
#     result=num1*num2
#     # print(result)
#     return result
# print(multiply(8,6))

# def multiply(number1,number2):
#     return number1*number2

# x= multiply(6,8)
# print(x)

# KEYWORD ARGUMENTS =================================

# def hello(first,middle,last):
#     print('hello '+first+" "+middle+' '+last)

# hello('code','dude','bro')

# hello(last='code',middle='Dude',first='bro')

# NESTED FUNCTIONS CALLS  ================================

# num=input('Enter a whole postitive number:')
# num=float(num)
# num=abs(num)
# num=round(num)

# print(num)
#print(round(abs(float(input('Enter a whole postitive number:')))))

# SCOPE  ================================

# name='Bro'   # global scope global variable
# def display_name():
#     name='Code'   #local scop local variable
#     print(name)
# display_name()
# print(name)

# ARGS  *  parameter that will pack all arguments into a tuple

# def add(*stuff):
#     sum=0
#     stuff=list(stuff)
#     stuff[0]=0
#     for i in stuff:
#         sum+=i
#     return sum

# # def add(*args):
# #     sum=0
# #     for i in args:
# #         sum+=i
# #     return sum

# print(add(1,2,8,4))

# KWARGS  ================================= key word arguments

# def hello(first,last):
#     print('hello '+first+' '+last)

# def hello(**kwargs):
#     # print('hello '+kwargs['first']+' '+kwargs['last'])
#     print('Hello',end=' ')
#     for key,value in kwargs.items():
#         print(value,end=' ')

# hello(title='Mr',first='bro',pl='Ml',middle='dude',last='code')

# STR.FORMAT()  method ================================

# animal='cow'
# item='moon'

# print('the ' +animal+' jumped over the '+item)
# print('The {} jumped over the {}'.format('cow','moon'))
# print('The {} jumped over the {}'.format(animal,item))
# print('The {1} jumped over the {0}'.format(animal,item)) positional arguments
# print('The {animal} jumped over the {item}'.format(animal='cow',item='moon'))  #key word arguments

# text='The {} jumped over the {}'
# print(text.format(animal,item))

# name='Bro'
# print('hello, my name is {}'.format(name))
# print('hello, my name is {:10}. Nice to meet you'.format(name))
# print('hello, my name is {:>10}. Nice to meet you'.format(name))
# print('hello, my name is {:^10}. Nice to meet you'.format(name))

# number=3.14159
# number1=31415954545
# print('the number pi is {:.2f}'.format(number))
# print('the number pi is {:,}'.format(number1))
# print('the number pi is {:b}'.format(number1))
# print('the number pi is {:o}'.format(number1))
# print('the number pi is {:X}'.format(number1))
# print('the number pi is {:E}'.format(number1))


# RANDOM  ================================

# import random

# x=random.randint(1,6)
# y=random.random()
# print(x,y)

# myList=['roc','paper','scissors']
# z=random.choice(myList)
# print(z)

# cards=[1,2,3,4,5,6,7,8,9,'3','q','k','a']
# random.shuffle(cards)
# print(cards)

# EXCEPTION ================================

# numerator=int(input('Enter a number to divide:'))
# denominator=int(input('Enter a number to divide by:'))
# result=numerator/denominator
# print(result)

# try:
#     numerator=int(input('Enter a number to divide:'))
#     denominator=int(input('Enter a number to divide by:'))
#     result=numerator/denominator
#     # print(result)
# except ZeroDivisionError as e:
#     print(e)
#     print('you cant divide by 0')
# except ValueError as e:
#     print(e)
#     print('Enter only numbers')
# except Exception as e:
#     print(e)
#     print('something went wrong')
# else:
#     print(result)
# finally:
#     print('this will execute')

# OS ================================

# import os

# path=r'C:\Users\Dell\Desktop\Text'

# if os.path.exists(path):
#     print('That location exists')
#     if os.path.isfile(path):
#         print('that is a file')
#     if os.path.isdir(path):
#         print('directory')
# else:
#     print('does not exist')

# READING A FILE ================================

# try:
#     with open('test.txt') as file:
#         print(file.read())
# except FileNotFoundError:
#     print('not found')

# WRITING FILES  ================================

# text='Yoooooooo\nThis is some text\nHave a good one\n'
# text='Changed'
# with open('newtext.txt','w') as file:
#     file.write(text)

# with open('newtext.txt','a') as file:
#     file.write(text)

# COPY FILE ========================================
#copyfile() content copy
#copy() content permission mode directory
#copy2() medadata

# import shutil

# shutil.copyfile('test.txt','copy.txt') #two arguments must be there  src and dst