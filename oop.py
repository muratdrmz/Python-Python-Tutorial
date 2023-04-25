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
