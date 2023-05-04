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

# def divisor(x):
#     def dividend(y):
#         return y/x
#     return dividend

# divide=divisor(2)
# print(divide(10))


# LAMBDA FUNCTIONS ======================================================

#accepts any number of arguments one expression

# lambda parameters:expression

# def double(x):
#     return x*2

# print(double(5))

# double=lambda x:x*2
# print(double(5))

# multiply=lambda x,y:x*y
# add=lambda x,y,z:x+y+z
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

# # fun=lambda x,y:x+y
# # word=functools.reduce(fun,letters)

# # print(word)

# factorial=[5,4,3,2,1]

# fac=lambda x,y:x*y

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
# # passed_students=list(filter(lambda x:x >=60, students))
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
# x=threading.Thread(target=eat_breakfast,args=())
# x.start()

# y=threading.Thread(target=drink_coffee,args=())
# y.start()

# z=threading.Thread(target=study,args=())
# z.start()

# x.join()
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

# x=threading.Thread(target=timer, daemon=True)
# x.start()


# answer=input('Do you wish to exit?',)


# MULTIPROCESSING ================================================
   #running tasks in prallel on diffferent cpu cores, bypasses GIL / mulitprocessing better for cpu bound tasks heavy cpu usage. multithreading better for bound tasks waiting around

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
# # label.place(x=100,y=100)
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

