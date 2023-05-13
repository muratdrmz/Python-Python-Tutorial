# from car import Car

# car_1=Car('Chevy','Corvette',2021,'blue')
# car_2=Car('Ford','Mustang',2022,'red')

# print(car_1.make)
# print(car_1.model)
# print(car_1.year)
# print(car_1.color)

# car_2.drive()
# car_2.stop()

# car_1=Car('Chevy','Corvette',2021,'blue')
# car_2=Car('Ford','Mustang',2022,'red')

# # car_1.wheels=2

# Car.wheels=3

# print(car_1.wheels,car_2.wheels)

# class Animal:
#     alive=True
#     def eat(self):
#         print('this animal is eating')
#     def sleep(self):
#         print('This animal is sleeping')

# class Rabbit(Animal):
#     def run(self):
#         print('this rabbit is running')

# class Fish(Animal):
#     def swim(self):
#         print('this fish is swimming')

# class Hawk(Animal):
#     def fly(self):
#         print('this hawk can fly')

# rabbit=Rabbit()
# fish=Fish()
# hawk=Hawk()

# print(rabbit.alive)
# fish.eat()
# hawk.sleep()

# rabbit.run()
# fish.swim()
# hawk.fly()


# MULTI LEVEL INHERITENCE ==================

# class Organism:
#     alive=True

# class Animal(Organism):
#     def eat(self):
#         print('This animal eats')

# class Dog(Animal):
#     def bark(self):
#         print('this dog barks')

# dog=Dog()
# print(dog.alive)
# dog.eat()
# dog.bark()

# MULTIPLE INHERITENCE =================================================

# class Prey:
#     def flee(self):
#         print('this flees')

# class Predator:
#     def hunt(self):
#         print('this hunts')

# class Rabbit(Prey):
#     pass

# class Hawk(Predator):
#     pass

# class Fish(Prey,Predator):
#     pass

# rabbit=Rabbit()
# hawk=Hawk()
# fish=Fish()

# rabbit.flee()
# hawk.hunt()
# fish.hunt()
# fish.flee()


#METHOD OVERRIDING  =====================================================

# class Animal:
#     def eat(self):
#         print('eating')

# class Rabbit(Animal):
#     def eat(self):
#         print('carrot eat')

# rabbit=Rabbit()
# rabbit.eat()

# METHOD CHAINING =====================================================

# class Car:
#     def turn_on(self):
#         print('You start the engine')
#         return self

#     def drive(self):
#         print('You drive the car')
#         return self

#     def brake(self):
#         print('step on the brakes')
#         return self
    
#     def turn_off(self):
#         print('off the engine')
#         return self

# car=Car()

# car.turn_on()
# car.drive()

# car.turn_on()\
# .drive()\
# .brake()\
# .turn_off()

# SUPER FUNCTION =======================================================
   # gives access to the methods of a parent class returns a temporary object of a parent class

# class Rectangle:
#     def __init__(self,length,width):
#         self.length=length
#         self.width=width

# class Square(Rectangle):
#     def __init__(self,length,width):
#         super().__init__(length,width)

#     def area(self):
#         return self.length*self.width

# class Cube(Rectangle):
    
#     def __init__(self,length,width,height):
#         super().__init__(length,width)
#         self.height=height

#     def volume(self):
#         return self.length*self.width*self.height

# square=Square(3,3)
# cube=Cube(3,3,3)

# print(square.area())
# print(cube.volume())


# ABSTRACT CLASSES =====================================================
#prevents creating an object of that class and compels user to override abstract methods in a child class. Abstarct class contain abstract methods. Abstract method has a decleration but des not have an implementation

# from abc import ABC, abstractclassmethod

# class Vehicle(ABC):
#     @abstractclassmethod    
#     def go(self):
#         pass
    
#     @abstractclassmethod 
#     def stop(self):
#         pass
    
# class Car(Vehicle):
#     def go(self):
#         print('you drive the car')

#     def stop(self):
#         print(' car stop')

# class Motorcycle(Vehicle):
#     def go(self):
#         print('you ride the motorcycle')

#     def stop(self):
#         print(' motor stop')
    
    
# # vehicle=Vehicle()
# car=Car()
# motorcycle=Motorcycle()

# # vehicle.go()
# car.go()
# motorcycle.go()

# car.stop()
# motorcycle.stop()


# PASS OBJECTS AS ARGUMENTS =============================================

# class Car:    
#     color=None
# class Motorcycle:
#     color=None

# def change_color(vehicle,color):
#     vehicle.color=color

# car_1=Car()
# car_2=Car()
# car_3=Car()

# bike_1=Motorcycle()
# bike_2=Motorcycle()
# bike_3=Motorcycle()

# change_color(bike_1,'red')
# change_color(bike_2,'white')
# change_color(bike_3,'blue')

# print(bike_1.color)
# print(bike_2.color)
# print(bike_3.color)

# change_color(car_1,'red')
# change_color(car_2,'white')
# change_color(car_3,'blue')

# print(car_1.color)
# print(car_2.color)
# print(car_3.color)


# DUCK TYPING  ==========================================================
#class of an object is less important than the methods = class type is not checked if minimum methods/attributes are present

# class Duck:
#     def walk(self):
#         print('duck is walking')

#     def talk(self):
#         print('Duck is qwacking')

# class Chicken:
#     def walk(self):
#         print('chicken is walking')

#     def talk(self):
#         print('chicken is clucking')

# class Person():
#     def catch(self,duck):
#         duck.walk()
#         duck.talk()
#         print('caught the critter')   

# duck=Duck()
# chicken=Chicken()
# person=Person()

# person.catch(chicken)


# WALRUS OPERATOR :===================================================
  #assigns values to variables as part of a larger expression
# happy=True

# print(happy)

# print(happy=True)  # bu calismaz
# print(happy:=True)

# foods=list()
# while True:
#     food=input('What do you like?: ')
#     if food=='quit':
#         break
#     foods.append(food)
#     print(foods)

# foods=list()
# while food:=input('what do you like?:') !='quit':
#     foods.append(food)


# ASSINGING A FUNCTION TO A VARIABLE ============================

# def hello():
#     print('Hello')

# print(hello)
# hi=hello

# print(hi)

# hello()
# hi()

# say=print
# say('this wors')


# HIGER ORDER FUNCTIONS  =========================================
   #function that accepts a function as an argument or returns a function
    #in python functions are also treated as objects

# def loud(text):
#     return text.upper()

# def quiet(text):
#     return text.lower()

#   #these functions accept strings as an ARGUMENT. accept functions as an ARGUMENT

# def hello(func):
#     text=func('Hello')
#     print(text)

# hello(quiet)

# def divisor(download):
#     def dividend(y):
#         return y/download
#     return dividend

# divide=divisor(2)
# print(divide(10))


# LAMBDA FUNCTIONS ======================================================

#accepts any number of arguments one expression

# lambda parameters:expression

# def double(download):
#     return download*2

# print(double(5))

# double=lambda download:download*2
# print(double(5))

# multiply=lambda download,y:download*y
# add=lambda download,y,z:download+y+z
# print(add(4,5,6))
# print(multiply(2,4))

# full_name=lambda first_name,last_name:first_name+' '+last_name
# print(full_name('MURAT','DURMAZ'))

# age_check=lambda age:True if age>=18 else False
# print(age_check(182))


# SORT ============== 
#method  used with lists   function used iterables
# [BUNA LIST DIYORLAR]    (BUNA TUPLE)

# students=['Squidward','Sandy','Patrick','Spongebob','Mr. Krabs']

# students.sort(reverse=True)

# for i in students:
#     print(i)

# students=('Squidward','Sandy','Patrick','Spongebob','Mr. Krabs')

# sorted_students=sorted(students,reverse=True)

# for i in sorted_students:
#     print(i)

# students=[('Squidward', 'F',60),
#           ('Sandy','A',33),
#           ('Patrick', 'D',36),
#           ('Spongebob','B',20),
#           ('Mr. Krabs', 'C', 78)]

# students.sort()
# for i in students:
#     print(i)

# grade=lambda grade:grade[2]
# students.sort(key=grade,reverse=True)
# for i in students:
#     print(i)


# students=(('Squidward', 'F',60),
#           ('Sandy','A',33),
#           ('Patrick', 'D',36),
#           ('Spongebob','B',20),
#           ('Mr. Krabs', 'C', 78))

# age=lambda ages:ages[2]
# sorted_students=sorted(students,key=age)
# for i in sorted_students:
#     print(i)


# MAP ===========================================
# map() applies a function to each item in an iterable(list tuple...)
# map(function,iterable)

# store=[('shirt',20.00),
#        ('pants',25.00),
#        ('jacket',50.00),
#        ('socks',10.00)]

# to_euros=lambda data:(data[0],data[1]*0.82)
# to_dollars=lambda data:(data[0],data[1]/0.82)

# store_dollars=list(map(to_dollars,store))

# store_euros=list(map(to_euros,store))

# for i in store_euros:
#     print(i)

# for i in store_dollars:
#     print(i)


#FILTER function ===============================================
#filter() creates a collection of elements from an iterable for which a function returns

#filter(function,iterable)

# friends=[('Rachel',19),
#          ('Monica',18),
#          ('Phoebe',17),
#          ('Joey',16),
#          ('Chandler',21),
#          ('Ross',20)]

# age= lambda data:data[1]>=18

# drinking_buds=list(filter(age,friends))
# print(drinking_buds)

# for i in drinking_buds:
#     print(i)


#REDUCE FUNCTION ==================================================
# reduce() applys a function to an iterable and reduce it to a single cumulative value. Performs function on first two elements and repeats process until 1 value remains

#reduce(function,iterable)

# import functools
# # letters=['H','E','L','L','O']

# # fun=lambda download,y:download+y
# # word=functools.reduce(fun,letters)

# # print(word)

# factorial=[5,4,3,2,1]

# fac=lambda download,y:download*y

# result=functools.reduce(fac,factorial)
# print(result)


# LIST COMPREHENSION ===============================================
      #creates a new list with less syntax, can mimic lambda functions
      #list=[expression for item in iterable]
      #list=[expression for item in iterable if conditional]
      #list=[expression if/else for item in iterable]

# squares=[]
# for i in range(1,11):
#     squares.append(i*i)
# print(squares)

# squares=[i*i for i in range(1,11)]

# print(squares)

# students=[100,90,80,70,60,50,40,30,0]
# # passed_students=list(filter(lambda download:download >=60, students))
# # print(passed_students)

# passed_students=[i for i in students if i>=60]
# passed_students=[i if i>=60 else 'FAILED'for i in students]
# print(passed_students)


# Dictionary comprehension =========================================
   # create dictionaries using an expression = can replace for loops and certain lambda functions
   #dictionary={key:expression for (key,value) in iterable}
   #dictionary={key:expression for (key,value) in iterable if conditional}
   #dictionary={key:(if/else) for (key,value) in iterable if conditional}
   #dictionary={key: function(value) for (key,value) in iterable if conditional}

# cities_in_F={'New york':32,'Boston':75,'Los Angeles':100,'Chicago':50}

# cities_in_C={key:round((value-32)*(5/9)) for (key,value) in cities_in_F.items()}

# print(cities_in_C)

# weather={'New york':'snowing','Boston':'sunny','Los Angeles':'sunny','Chicago':'cloudy'}

# sunny_weather={key: value for (key,value) in weather.items() if value=='sunny'}
# print(sunny_weather)

# cities={'New york':32,'Boston':75,'Los Angeles':100,'Chicago':50}
# des_cities={key:('WARM' if value>=40 else 'COLD' ) for (key,value) in cities.items()}
# print(des_cities)

# cities={'New york':32,'Boston':75,'Los Angeles':100,'Chicago':50}

# def check_temp(value):
#     if value>=70:
#         return 'HOT'
#     elif 69>=value>=40:
#         return 'WARM'
#     else:
#         return 'Cold'
    
# des_cities={key:check_temp(value) for (key,value) in cities.items()}
# print(des_cities)


#ZIP (*ITERABLES) =============================================   
   #aggregate elements from two or more iterables (list,tuples,sets...,) creates a zip object with paired elements stored in tuples for each element

# usernames=['Dude','Bro','Mister']
# passwords=('p@ssword','abc123','guest')
# login_date=['1/1/2021','1/2/2021','1/3/2021']

# users=list(zip(usernames,passwords))
# for i in users:
   #  print(i)
# users=dict(zip(usernames,passwords))

# for key,value in users.items():
#     print(key+' : '+value)

# print(type(users))

# users=zip(usernames,passwords,login_date)

# for i in users:
#     print(i)


# if __name__== '__main__'========================================
  #     main()


# if __name__=='__main__':
#     print('running directly')
# else:
#     print('indiretlyh')

# IMPORT TIME ====================================================
   
# import time
# print(time.ctime(0))  #epoch=time began reference point as seconds

# print(time.ctime(10000000000))

# print(time.time())  #return current seconds since epoch

# print(time.ctime(time.time()))

# time_object=time.localtime()
# time_object=time.gmtime()
# print(time_object)
# local_time=time.strftime('%B %d %Y %H:%M:%S',time_object)
# print(local_time)

# time_string='20 April, 2020'
# time_object=time.strptime(time_string,'%d %B, %Y')
# print(time_object)

# time_tuple=(2020,4,20,4,20,0,0,0,0)
# time_string=time.asctime(time_tuple)
# print(time_string)

# time_tuple=(2020,4,20,4,20,0,0,0,0)
# time_string=time.mktime(time_tuple)
# print(time_string)


#MULTITHREADING===================================================
   #thread=a flow of execution. like a separate order of instructions. GIL global interpreter lock allows only one thread to hold the control of the Python interpreter

   #cpu bound= program/task spends most of it's time waiting for internal events use multiprocessing
   #io bound=waiting for external events use multithreading
# import threading
# import time

# def eat_breakfast():
#     time.sleep(3)
#     print('eat breakfast')

# def drink_coffee():
#     time.sleep(4)
#     print('drank coffee')

# def study():
#     time.sleep(5)
#     print('finish studying')
    
# # 1
# download=threading.Thread(target=eat_breakfast,args=())
# download.start()

# y=threading.Thread(target=drink_coffee,args=())
# y.start()

# z=threading.Thread(target=study,args=())
# z.start()

# download.join()
# y.join()
# z.join()

# 2
# eat_breakfast()
# drink_coffee()
# study()


# print(threading.active_count())
# print(threading.enumerate())
# print(time.perf_counter())


# DAEMON THREAD===================================================
   #a thread that runs in the background,not important for program to run. program will not wait for daemon threads to complete before extitin non-deamon threads cannot be normally killed, stay alive until task is complete 
# import threading
# import time

# def timer():
#     print()
#     print()
#     count = 0
#     while True:
#         time.sleep(1)
#         count += 1
#         print('logged in for: ', count, 'seconds')

# download=threading.Thread(target=timer, daemon=True)
# download.start()


# answer=input('Do you wish to exit?',)


# MULTIPROCESSING ================================================
   #running GB in prallel on diffferent cpu cores, bypasses GIL / mulitprocessing better for cpu bound GB heavy cpu usage. multithreading better for bound GB waiting around

# from multiprocessing import Process, cpu_count
# import time
# print(cpu_count())

# def counter(num):
#     count=0
#     while count<num:
#         count +=1

# def main():
    
#     a=Process(target=counter, args=(500000,))
#     b=Process(target=counter, args=(500000,))
#     c=Process(target=counter, args=(500000,))
#     d=Process(target=counter, args=(500000,))
#     a.start()
#     b.start()
#     c.start()
#     d.start()
    
#     a.join()
#     b.join()
#     c.join()
#     d.join()

#     print('Finished in:', time.perf_counter(),'seconds')

# if __name__== '__main__':
#     main()


# GRAPHICAL USER INTERFACE GUI====================================

# from tkinter import *
#    # widgets= GUI elements: buttons textboxes labels images
#    #windows= serves as a container to hold or contain these widgets

# window=Tk() # instantiate an instance of a window

# window.geometry('420x420')
# window.title('Bro Code first GUI program')
# icon=PhotoImage(file='fire.png')
# window.iconphoto(True,icon)
# window.config(background='blue')

# window.mainloop()  #place window on computer screen listen for events


# LABELS =====================================================
# from tkinter import *

# window=Tk()
# window.geometry('420x420')
# window.title('Bro Code first GUI program')
# icon=PhotoImage(file='fire.png')
# window.iconphoto(True,icon)
# window.config(background='white')
# photo=PhotoImage(file='fire.png')

# label=Label(window,
#             text='hello world do you even code',
#             font=('Arial',40,'bold'),
#             fg='green',
#             bg='black',
#             relief=RAISED,
#             bd=10,
#             padx=20,
#             pady=20,
#             image=photo,
#             compound='bottom')
# label.pack()
# # label.place(download=100,y=100)
# window.mainloop()


# BUTTONS ========================================================
# from tkinter import *

# count=0
# def click():
#     global count
#     count+=1
#     print('you clicked',count,'times')
#    #  print('you clicked')

# window=Tk()

# photo=PhotoImage(file='fire.png')
# button=Button(window,
#               text='click me',
#               command=click,
#               font=('Comic Sans',30),
#               fg='#00FF00',
#               bg='black',
#               activeforeground='pink',
#               activebackground='blue',
#               state=ACTIVE,
#               image=photo,
#               compound='bottom')
# button.pack()
# window.mainloop()


# ENTRY BOX ====================================================
   #entry widget=textbox that accepts a single line of user input

# from tkinter import*

# def submit():
#     username=entry.get()
#     print('hello '+username)
#     entry.config(state=DISABLED)

# def delete():
#     entry.delete(0,END)

# def backspace():
#     entry.delete(len(entry.get())-1,END)
    

# window=Tk()

# entry=Entry(window,
#             font=('Arial',50),
#             fg='#00FF00',
#             bg='black',
#             show='*')

# entry.insert(0,'spongebob')

# entry.pack(side=LEFT)

# submit_button=Button(window,text='submit',command=submit)
# submit_button.pack(side=RIGHT)

# delete_button=Button(window,text='delete',command=delete)
# delete_button.pack(side=RIGHT)

# backspace_button=Button(window,text='backspace',command=backspace)
# backspace_button.pack(side=RIGHT)


# window.mainloop()


# CHECK BUTTONS CUSTOMISATION ======================================

# from tkinter import*

# def display():
    
#     if(download.get()==1):
#         print(' you agreed')
#     else:
#         print('dont agree')

# window=Tk()

# download=IntVar()

# photo=PhotoImage(file='fire.png')
# check_button=Checkbutton(window,
#                          text='I agree to something',
#                          variable=download,
#                          onvalue=1,
#                          offvalue=0,
#                          command=display,
#                          font=('Arial',20),
#                          fg='#00FF00',
#                          bg='black',
#                          activeforeground='#00FF00',
#                          activebackground='black',
#                          padx=25,
#                          pady=10,
#                          image=photo,
#                          compound='left')
# check_button.pack()

# window.mainloop()


# RADIOBUTTONS =====================================================
   #only select one from a group

# from tkinter import*

# food=['pizza','hamburger','hotdog']

# def order():
#     if(download.get()==0):
#         print('ordered pizza')
#     elif(download.get()==1):
#         print('hamburger ordered')
#     elif(download.get()==2):
#         print('hotdog ordererd')
#     else:
#         print('what')

# window=Tk()

# pizzaImg=PhotoImage(file='fire.png')
# hamImg=PhotoImage(file='fire.png')
# hotdogImg=PhotoImage(file='fire.png')
# foodImgs=[pizzaImg,hamImg,hotdogImg]

# download=IntVar()
# for index in range (len(food)):
#     radbtn=Radiobutton(window,
#                        text=food[index],
#                        variable=download,
#                        value=index,
#                        padx=25,
#                        font=('Impact',50),
#                        image=foodImgs[index],
#                        compound='left',
#                        indicatoron=0,
#                        width=375,
#                        height=100,
#                        command=order)
#     radbtn.pack(anchor=W)

# window.mainloop()


# SLIDING SCALE =============================================
# from tkinter import*

# def submit():
#     print('temperature is: '+str(scale.get())+' degrees C')
# window=Tk()

# hotImg=PhotoImage(file='fire1.png')
# hotLabel=Label(image=hotImg)
# hotLabel.pack()
# scale=Scale(window,
#             from_=100,
#             to=0,
#             length=600,
#             orient=VERTICAL,
#             font=('Consolas',20),
#             tickinterval=10,
#             # showvalue=0,
#             resolution=5,
#             troughcolor='#69EAFF',
#             fg='#FF1C00',
#             bg='black')

# scale.set(((scale['from']-scale['to'])/2)+scale['to'])
# scale.pack()

# coldIgm=PhotoImage(file='fire1.png')
# coldLabel=Label(image=coldIgm)
# coldLabel.pack()

# btn=Button(window,
#            text='submit',
#            command=submit)
# btn.pack()
# window.mainloop()


# LISTBOX=========================================================

# def submit():
#    #  print('you have ordered: '+listbox.get(listbox.curselection()))
#    food=[]
#    for index in listbox.curselection():
#        food.insert(index,listbox.get(index))
#    print('you have ordered: ')
#    for index in food:
#        print(index)

# def add():
#     listbox.insert(listbox.size(),entryBox.get())
#     listbox.config(height=listbox.size()) 

# def delete():
#    #  listbox.delete(listbox.curselection())

#    for index in reversed (listbox.curselection()):
#       listbox.delete(index)
#    listbox.config(height=listbox.size())

# from tkinter import*

# window=Tk()

# listbox=Listbox(window,
#                 bg='#f7ffde',
#                 font=('Constantia',35),
#                 width=12,
#                 selectmode=MULTIPLE)
# listbox.pack()

# listbox.insert(1,'pizza')
# listbox.insert(2,'pasta')
# listbox.insert(3,'garlic')
# listbox.insert(4,'soup')
# listbox.insert(5,'salad')

# listbox.config(height=listbox.size())

# entryBox=Entry(window,)
# entryBox.pack()

# submitBtn=Button(window,text='submit',command=submit)
# submitBtn.pack()

# addBtn=Button(window,text='add',command=add)
# addBtn.pack()

# deleteBtn=Button(window,text='delete',command=delete)
# deleteBtn.pack()

# window.mainloop()


# MESSAGE BOX ====================================================

# from tkinter import*
# from tkinter import messagebox  #import messagebox library

# def click():
   #  messagebox.showinfo(title='This is an info message box',message='You are a person')

   # while(True):      
   #    messagebox.showwarning(title='WARNING',message='You have a VIRUS!')

   # messagebox.showwarning(title='WARNING',message='You have a VIRUS!')

   # if messagebox.askokcancel(title='ask ok can',message='Do yo'):
   #    print('you did a thing')
   # else:
   #    print('you canceled') 

   # if messagebox.askretrycancel(title='ask ok can',message='Do you wan to do retry'):
   #    print('you redo a thing')
   # else:
   #    print('you finished')

   # if messagebox.askyesno(title='ask yes or no',message='do you like cake'):
   #    print('i like cake')
   # else:
   #    print('whey not ') 

   # answer=messagebox.askquestion(title='ask question',message='do you like pie')
   # if (answer=='yes'):
   #    print('i like pie too')
   # else:
   #    print('why not like pie')

#    answer=messagebox.askyesnocancel(title='yes no cancel',message='do you like to code',icon='warning')
#    if (answer==True):
#       print('you like to code')
#    elif(answer==False):
#       print('then why are you watching this')
#    else:
#       print('you have dodged ')
# window=Tk()

# button=Button(window,command=click,text='click me')
# button.pack()
# window.mainloop()


# COLOR CHOSER MODULE =======================================
# from tkinter import*
# from tkinter import colorchooser

# def click():
#     color=colorchooser.askcolor()
#    #  print(color)
#     colorHex=color[1]
#    #  print(colorHex)
#     window.config(bg=colorHex)

# window=Tk()

# window.geometry('420x420')
# button=Button(text='click me',command=click)
# button.pack()

# window.mainloop()


# TEXT WIDGET ===============================================

# from tkinter import*

# def submit():
#     input=text.get('1.0',END)
#     print(input)

# window=Tk()

# text=Text(window,
#           bg='light yellow',
#           font=('Ink Free',25),
#           height=8,
#           width=20,
#           padx=20,
#           pady=20,
#           fg='purple')
# text.pack()

# button=Button(window,text='submit',command=submit)
# button.pack()

# window.mainloop()


# OFEN AND READ FILE===========================================

# from tkinter import*
# from tkinter import filedialog

# def openFile():
#     filepath=filedialog.askopenfilename(initialdir='C:\\Users\\Dell\\Desktop\\PYTHON\\Python Tutorial\\newtext.txt',                                    title='Open file okay',                                     filetypes=(('text files','*.txt'),('all files','*.*')))

#     file=open(filepath,'r')

#     print(file.read())
#     file.close

    
# window=Tk()

# button=Button(text='Open',command=openFile)
# button.pack()


# window.mainloop()


# SAVE FILE ===============================================

# from tkinter import*
# from tkinter import filedialog

# def saveFile():
#     file=filedialog.asksaveasfile(initialdir='C:\\Users\\Dell\\Desktop\\PYTHON\\Python Tutorial\\',
#                                   defaultextension='.txt',
#                                   filetypes=[
#                                       ('Text file','.txt'),
#                                       ('HTML file','.html'),
#                                       ('All files','.*'),

#                                   ])
#     if file is None:
#         return
#     filetext=str(text.get(1.0,END))
#    #  filetext=input('enter some text')
#     file.write(filetext)
#     file.close()

# window=Tk()
# button=Button(window,text='save',command=saveFile)
# button.pack()

# text=Text(window)
# text.pack()


# window.mainloop()


# MENU BAR =================================================

# from tkinter import*


# def openFile():
#     print('file openeded')

# def saveFile():
#     print('file saved')

# def cut():
#     print('cut')

# def copy():
#     print('copied')

# def paste():
#     print('pasted')

# window=Tk()

# openImage=PhotoImage(file='fire1.png')
# saveImage=PhotoImage(file='fire1.png')
# exitImage=PhotoImage(file='fire1.png')

# menubar=Menu(window)
# window.config(menu=menubar)

# fileMenu=Menu(menubar,tearoff=0,font=('MV Boli',15))
# menubar.add_cascade(label='File',menu=fileMenu)
# fileMenu.add_command(label='Open',command=openFile,image=openImage,compound='left')
# fileMenu.add_command(label='Save',command=saveFile, image=saveImage,compound='left')
# fileMenu.add_separator()
# fileMenu.add_command(label='Exit',command=quit,image=exitImage,compound='left')

# editMenu=Menu(menubar,tearoff=0,font=('MV Boli',15))
# menubar.add_cascade(label='Edit',menu=editMenu)
# editMenu.add_command(label='Cut',command=cut)
# editMenu.add_command(label='Copy',command=copy)
# editMenu.add_command(label='Paste',command=paste)
# window.mainloop()


# FRAME ======================================================
   #a rectangular continer to group and hold widgets

# from tkinter import*

# window=Tk()

# frame=Frame(window,bg='pink',bd=5,relief=RAISED)
# # frame.pack(side=BOTTOM)
# frame.place(download=100,y=100)

# Button(frame,text='W',font=('Consolas',25),width=3).pack(side=TOP)
# Button(frame,text='A',font=('Consolas',25),width=3).pack(side=LEFT)
# Button(frame,text='S',font=('Consolas',25),width=3).pack(side=LEFT)
# Button(frame,text='D',font=('Consolas',25),width=3).pack(side=LEFT)

# window.mainloop()


# WINDOW CREATION ===============================================

# from tkinter import*

# def create_window():
#    #  new_window=Toplevel() 
#     new_window=Tk() 

#     old_window.destroy()    #close old window

# old_window=Tk()

# Button(old_window,text='create new window',command=create_window).pack()

# old_window.mainloop()


# TABS =======================================================

# from tkinter import*
# from tkinter import ttk

# window=Tk()

# notebook=ttk.Notebook(window) #manages a collection of windows displays

# tab1=Frame(notebook)
# tab2=Frame(notebook)

# notebook.add(tab1,text='Tab 1')
# notebook.add(tab2,text='Tab 2')
# notebook.pack(expand=True,fill='both')

# Label(tab1,text='Hello this is tab1',width=50,height=25).pack()
# Label(tab2,text='Goodbye, this is tab2',width=50,height=25).pack()

# window.mainloop()


# GRID ========================================================
# from tkinter import*

# window=Tk()

# titleLabel=Label(window,text='Enter your info',font=('Arial',25)).grid(row=0,column=0,columnspan=2)

# firstNameLabel=Label(window,text='First name: ',width=20, bg='red').grid(row=1,column=0)
# firstNameEntry=Entry(window).grid(row=1,column=1)

# LastNameLabel=Label(window,text='Last name: ',bg='green').grid(row=2,column=0)
# LastNameEntry=Entry(window).grid(row=2,column=1)

# emailNameLabel=Label(window,text='email: ',bg='blue',width=30).grid(row=3,column=0)
# emailNameEntry=Entry(window).grid(row=3,column=1)

# submitButton=Button(window,text='Submit').grid(row=4,column=0,columnspan=2)

# window.mainloop()


# PROGRESS BAR ================================================

# from tkinter import*
# from tkinter.ttk import*
# import time

# def start():
#     GB=10
#     download=0
#     speed=1
#     while(download<GB):
#         time.sleep(0.05)
#         bar['value']+=(speed/GB)*100
#         download+=speed
#         percent.set(str(int((download/GB)*100))+'%')
#         text.set(str(download)+'/'+str(GB)+' GB completed')
#         window.update_idletasks()

# window=Tk()

# percent=StringVar()
# text=StringVar()

# bar=Progressbar(window,orient=HORIZONTAL,length=300)
# bar.pack(pady=10)

# percentLabel=Label(window,textvariable=percent).pack()
# taskLabel=Label(window,textvariable=text).pack()

# button=Button(window,text='download',command=start).pack()


# window.mainloop()


# KANVAS ====================================================
# from tkinter import*

# window=Tk()

# canvas=Canvas(window,height=500,width=500)
# canvas.create_line(0,0,500,500,fill='blue',width=5)
# canvas.create_line(0,500,500,0,fill='red',width=5)
# canvas.create_rectangle(50,50,250,250,fill='purple')
# canvas.create_polygon(250,0,500,500,0,500,fill='yellow',outline='black',width=5)
# canvas.create_arc(0,0,500,500,
# style=PIESLICE,start=270,extent=180,width=5)
# canvas.create_arc(0,0,500,500,fill='red',extent=180,width=10)
# canvas.create_arc(0,0,500,500,fill='white',extent=180,start=180,width=10)
# canvas.create_oval(190,190,310,310,fill='white',width=10)

# canvas.pack()

# window.mainloop()

# KEY EVENTS===============================================

# from tkinter import*

# def doSomething(event):
#    #  print('you presssed: '+event.keysym)
#    label.config(text=event.keysym)

# window=Tk()

# window.bind("<Key>",doSomething)

# label=Label(window,font=('Helvetica',100))
# label.pack()


# window.mainloop()

# MOUSE EVENTS ==============================================
# from tkinter import*

# def doSome(event):
#     print('you did a thing coordinates: '+str(event.x)+','+str(event.y))

# window=Tk()

# window.bind('<Button-1>',doSome)
# window.bind('<Button-2>',doSome)
# window.bind('<Button-3>',doSome)
# window.bind('<ButtonRelease>',doSome)
# window.bind('<Enter>',doSome)
# window.bind('<Leave>',doSome)
# window.bind('<Motion>',doSome)

# window.mainloop()


# DRAG AND DROP WIDGETS=================================

# from tkinter import*

# def drag_start(event):
#     widget=event.widget
#     widget.startX=event.x
#     widget.startY=event.y

# def drag_motion(event):
#     widget=event.widget
#     x=widget.winfo_x()-widget.startX+event.x
#     y=widget.winfo_y()-widget.startY+event.y
#     widget.place(x=x,y=y)
       

# window=Tk()

# label=Label(window,bg='red',width=10,height=5)
# label.place(x=0,y=0)

# label2=Label(window,bg='blue',width=10,height=5)
# label2.place(x=100,y=100)

# label.bind('<Button-1>',drag_start)
# label.bind('<B1-Motion>',drag_motion)

# label2.bind('<Button-1>',drag_start)
# label2.bind('<B1-Motion>',drag_motion)

# window.mainloop()


# MOVING====================================================
# from tkinter import*

# def move_up(event):
#     label.place(x=label.winfo_x(),y=label.winfo_y()-10)

# def move_down(event):
#     label.place(x=label.winfo_x(),y=label.winfo_y()+10)

# def move_left(event):
#     label.place(x=label.winfo_x()-10,y=label.winfo_y())

# def move_right(event):
#     label.place(x=label.winfo_x()+10,y=label.winfo_y())
    

# window=Tk()
# window.geometry('500x500')

# window.bind('<w>',move_up)
# window.bind('<s>',move_down)
# window.bind('<a>',move_left)
# window.bind('<d>',move_right)

# window.bind('<Up>',move_up)
# window.bind('<Down>',move_down)
# window.bind('<Left>',move_left)
# window.bind('<Right>',move_right)

# myimage=PhotoImage(file='fire1.png')
# label=Label(window,image=myimage,bg='red')
# label.place(x=0,y=0)

# window.mainloop()


# MOVING IMAGES ===================================================

# from tkinter import*

# def move_up(event):
#     canvas.move(myimage,0,-10)

# def move_down(event):
#     canvas.move(myimage,0,10)
    
# def move_left(event):
#     canvas.move(myimage,-10,0)
    
# def move_right(event):
#     canvas.move(myimage,10,0)
    

    
# window=Tk()

# window.bind('<w>',move_up)
# window.bind('<s>',move_down)
# window.bind('<a>',move_left)
# window.bind('<d>',move_right)

# window.bind('<Up>',move_up)
# window.bind('<Down>',move_down)
# window.bind('<Left>',move_left)
# window.bind('<Right>',move_right)

# canvas=Canvas(window,width=500,height=500)
# canvas.pack()

# photo=PhotoImage(file="fire1.png")
# myimage=canvas.create_image(0,0,image=photo,anchor=NW)


# window.mainloop()


# 2D ANIMATIONS ==================================================

# from tkinter import*
# import time

# WIDTH=500
# HEIGHT=500
# xVelocity=3
# yVelocity=2


# window=Tk()

# canvas=Canvas(window,width=WIDTH,height=HEIGHT)
# canvas.pack()

# bp=PhotoImage(file='fire.png')
# backg=canvas.create_image(0,0,image=bp,anchor=NW)

# photo=PhotoImage(file='fire1.png')
# my_image=canvas.create_image(0,0,image=photo,anchor=NW)

# image_width=photo.width()
# image_height=photo.height()

# while True:
#     coordinates=canvas.coords(my_image)
#     print(coordinates)
#     if(coordinates[0]>=(WIDTH-image_width) or coordinates[0]<0):
#         xVelocity=-xVelocity

#     if(coordinates[1]>=(HEIGHT-image_height) or coordinates[1]<0):
#         yVelocity=-yVelocity

#     canvas.move(my_image,xVelocity,yVelocity)
#     window.update()
#     time.sleep(0.01)

# window.mainloop()


# ANIMATE MULTIPLE OBJECT =======================================

# from tkinter import*
# from Ball import*
# import time

# window=Tk()

# WIDTH=500
# HEIGHT=500

# canvas=Canvas(window,width=WIDTH,height=HEIGHT)
# canvas.pack()

# volley_ball=Ball(canvas,0,0,100,1,1,'white')
# tennis_ball=Ball(canvas,0,0,50,4,3,'yellow')
# basket_ball=Ball(canvas,0,0,125,8,7,'orange')

# while True:
#     volley_ball.move()
#     tennis_ball.move()
#     basket_ball.move()
#     window.update()
#     time.sleep(0.01)

# window.mainloop()


# CLOCK PROGRAMMING ===============================================
# from tkinter import*
# from time import*

# def update():
#     time_string=strftime('%I:%M:%S %p')
#     time_label.config(text=time_string)

#     day_string=strftime('%A')
#     day_label.config(text=day_string)

#     date_string=strftime('%B %d, %Y')
#     date_label.config(text=date_string)

#     window.after(1000,update)


# window=Tk()

# time_label=Label(window,font=('Arial',50),fg='#00FF00',bg='black')
# time_label.pack()

# day_label=Label(window,font=('Ink Free',25))
# day_label.pack()

# date_label=Label(window,font=('Ink Free',30))
# date_label.pack()

# update()

# window.mainloop()


# SEND AN EMAIL========================================
# import smtplib

# sender='muratdurmaz97681@gmail.com'
# receiver='mrtdrmz@windowslive.com'
# password='234567of'
# subject='Python email test'
# body='I am testing python email sending '

# message=f"""from: Murat{sender}
# To:mrrtt{receiver}
# Subject:{subject}\n
# {body}
# """

# server=smtplib.SMTP('smtp.gmail.com',587)
# server.starttls()

# try:
#    server.login(sender,password)
#    print('logged in...')
#    server.sendmail(sender,receiver,message)
#    print('Email has been sent!')

# except smtplib.SMTPAuthenticationError:
#    print('unable to sign in')


# RUN PY FILE in COMMAND===================================

# print("Hello world")

# name = input("what is your name")

# print("Hello " + name)

# cd C:User\Dell\Desktop python hello.py

#PIP MANAGER===============================================


# EXECUTABLE CONVERTION ===================================









































