import random
import sys
import os

print("Hello World")

# comment

'''
Multiline comment
'''

"""
Multi line strings
"""
name = "Ben"
print(name)

# LETTER-35364__
#
# name = 15
#
# Numbers, strings, lists, tuples, dictionaries
#
# 5 data types
#
# 7 different algorithmitic operators.
#
# + - * / % (modulous shows remainder) ** (exponential multiplication) // (floor devision gets \
# rid of remainder and rotates down)

print("5 + 2 = ", 5+2)
print("5 - 2 = ", 5-2)
print("5 * 2 = ", 5*2)
print("5 / 2 = ", 5/2)
print("5 % 2 = ", 5%2)
print("5 ** 2 = ", 5**2)
print("5 // 2 = ", 5//2)

# whenever performing arithmetic understand ORDER of OPERATIONS

print("1 + 2 - 3 * 2 =", 1 + 2 - 3 * 2)
print("(1 + 2 - 3) * 2 =", 1 + 2 - 3 * 2)

# in quotes = strings
# order of operations definitely matters
# string is a string of characters numbers between double or single quotes

quote = "\" Always remember you are unique"
# quote within string

multi_line_quote = ''' just like everyone else'''
# python convention for naming variables uses _ vs *space*

new_string = quote + multi_line_quote

print("%s %s %s" % ('I like the quote', quote, multi_line_quote))

print("I don't like", end =" ")
print("newlines")
# ends newlines

print('\n' * 5)
# prints 5 newlines

# LISTS: Allows you to create list of values and manipulate them. Each one has \
# index like a "label" that starts at "0"

grocery_list = ['juice', 'tomatoes', 'potatoes', 'bananas']

# put any data type in list

print('First Item', grocery_list[0])

# prints first item in list index 1 = 0 not 1

grocery_list[0] = "Green juice"
print('First Item', grocery_list[0])

# change the value of the first item if we'd like

print(grocery_list[1:3])

# print from index 1 UP TO but NOT index 3
# a little weird but just remember it

other_events = ['wash car', 'pick up kids', 'cash check']

# lists of lists inside of a list

to_do_list = [other_events, grocery_list]
print(to_do_list)

# this prints both lists as one list

print((to_do_list[1][1]))

# how to get second item outside of to_do_list
# lists are boxes inside of boxes.

grocery_list.append('Onions')
print(to_do_list)

# appends items

grocery_list.insert(1, "Pickle")

# inserts item

grocery_list.remove("Pickle")

# removes item

grocery_list.sort()

# sort

grocery_list.reverse()

# reverse sort

del grocery_list[4]
print(to_do_list)

# deletes an item in index 4
# while making changes to grocery_list they where also
# affecting the to_do_list

to_do_list2 = other_events + grocery_list

# combines lists

print(len(to_do_list2))

# length of the lists

print(max(to_do_list2))

# max

print(min(to_do_list2))

# min

# TUPLES

# IMMUTABLE

pi_tuple = (3, 1, 4, 1, 5, 9)

# sometimes you have data you do not want to be easily
# changed

new_tuple = list(pi_tuple)

# new tuple is a list now

new_list = tuple(new_tuple)

# converts list into a tuple

len(tuple) min(tuple) max(tuple)

# DICTIONARIES

# made up of values with a unique key that each value is going to be storing
# like lists but you cannot join dicts together like you can lists with a '+'
# sign

super_villans = {'Fiddler' : 'Isaac Bowin',
                'Captain Cold' : 'Leonard Snart',
                'Weather Wizard' : 'Mark Mardon',
                'Mirror Master', : 'Sam Scudder',
                'Pied Piper' : 'Thomas Peterson'}

print(super_villans['Captain Cold'])

# find out captain cold's secret Identity

del super_villans['Fiddler']

# deletes

super_villans['Pied Piper'] = 'Hartley Rathaway'

# changes value

print(len(super_villans))

# prints length

print(super_villans.get("Pied Piper"))

# value by passing in a key using get ( use this a lot)

print(super_villans.keys())

# get list of super_villan keys by just asking for keys

print(super_villans.values())

# values
# names are just so logical easy to remember

# CONDITIONALS

# if else elif (used to form different actions
# based on different conditions) == (equal) != (not equal to) > (greater than)
# >= (greater than or equal to) < ( less than ) <= (less than or equal to)
# if statement executes code if a condition is met. White space
# is used to group blocks of code in python in multiple different ways

if age > 16:
    print('You are old enough to drive')
else:
    print('You are not old enough to drive')
if age >= 21:
    print('You are old enough to drive a tractor trailer')
elif age >= 16:
    print('You are old enough to drive a car')
else:
    print("You are not old enough to drive")

# logical operators AND OR NOT

if ((age >= 1) and (age <= 18):
    print("You get a birthday")
elif (age == 21) or (age >= 65):
    print("You get a birthday")
elif not(age == 30):
    print("You don't get a birthday")
else:
    print("You get a birthday party yeah")

# if it meets a condition ahead of other conditions then the other
# conditions are forgotten about and not going to be checked logically

# LOOPING
# used when you have to do something 5 + times for example

for x in range(0, 10):
    print(x, ' ', end="")

# ten digits because index starts at 0 a shorthand for the range function is
# range(10)

print('\n')

grocery_list = ['Juice', 'Tomatoes', 'Potatoes', 'Bananas']

for y in grocery_list:
    print(y)

for x in [2, 4, 6, 8, 10]:
    print (x)

# double up for loops to cycle through a list

num_list = [[1, 2, 3], [10, 20, 30], [100, 200, 300]]

for x in range(0, 3):
    for y in range(0, 3):
        print(num_list[x][y])

# prints those out in order

# WHILE LOOP
# used when you have no idea how many times you're going to need to loop

ranomd_num = random.randrange(0, 100)

while(random_num != 15):
    print(random_num)
    random_num = random.randrange(0, 100)

# keep going until this condition is met

i = 0

# uses while loop in more traditional matter kind of like a for loop
# iterator which value is going to change over and over again

while(i <= 20):
# what if we want to print out all of the even numbers
    if(i%2 == 0):
# good way to find an even number is using the modulous of 2
        print(i)
    elif(i == 9):
# elif i == 9 even though it says 20
# force ourselves out of the loop completely using break
        break
    else:
        i += 1
        continue
# same thing as saying i = i + 1 ( short hand )
# continue skips rest of the stuff that comes after this then jumps back into
# while loop
    i += 1

# FUNCTIONS
# allows us to reuse and rewrite more readable code

def addNumber():
    sumNum = fNum + 1Num
    return sumNum

print(addNumber(1, 4))
# def FUNCTION NAME then PARAMETERS it will receive
# define function before calling it
# return something to caller of function = return
# sumNum only exists INSIDE of the function
# sumNum is out of scope
# what goes on inside of the functions happens there and stays there unless it's
# going to be returned to us
or string = addNumber(1, 4)

# works exactly the same ways

print('What is your name')

name = sys.stdin.readline()

print('Hello', name)

# CLOSER LOOK AT STRINGS

long_string = "I'll catch you if you fall - The Floor"

print(long_string[0:4])

# index 0 up to index 4 but not index 4 prints first 4 characters

print(long_string[-5:])

# prints the last 5 characters

print(long_string[:-5])

#prints up to the last 5 characters "33"

print(long_string[:4] + " be there")

# add the first 4 characters to sentence

print("%c is my %s letter and my number %d number is %.5f" %, 'X', 'favorite', 1, .14)

# %c is a characters
# %s is a string
# %d is an integer
# %.5f is floating point number with at least 5 decimal places
# X is favorite characters
# favorite is string
# prints 5 decimal places on .14 even if you did not input them

print(long_string.capitalize())

# capatalizes first character of a string

print(long_string.find("Floor"))

# returns the index value of the start of the string
# index.find then the word = "33rd character" case sensitive has to be the exact same

print(long_string.isalpha())

# is ALL letters

print(long_string.isnum())

# is ALL number

print(len(long_string))

# length

print(long_string.replace("Floor", "Ground"))

# replaces specific word with another word

print(long_string.strip())

# strips white space

quote_list = long_string.split(" ")

# splits a string into a list. How we want those words to be seperated. Space
# works out great there

# FILE I/O

test_file = open("test.txt", "wb")

# wb writes to FILE

print(test_file.mode)

# write mode

print(test_file.name)

# if you forget the name of FILE

test_file.write(bytes("Write me to the file\n", 'UTF-8'))

# weird but is how you put bytes in python

test_file.close()

# closes FILE

test_file = open("test.txt", "r+")

# r+ is reading and writing

text_in_file = test_file.read()
print(text_in_file)

os.remove("test.txt")

# OBJECTS
# Concept of OOP is to allow us to model real world things using code
# every real world object has attributes i.e. color, height, weight
# every real world object has abilities like walk, talk, and eat
# we are going to define attributes using variables inside of things called classes
# and the abilities are just going to be functions

class Animal:
    __name = " "
    # none is for lack of a value
    __height = 0
    __weight = 0
    __sound = 0
    # 2 underscores mean that the value is private and in order to change
    # values we are going to need to use a function inside of a class and
    # do the same if we want to get those values.

    def __init__(self, name, height, weight, sound):
        self.__name = name
        self.__height = height
        self.__weight = weight
        self.__sound = sound

    # constructor. Is used to set up to initialize an object
    # demands all values are passed in here in attributes
    # we want them to be defined/changed
    # create setters/getters

    def set_name(self, )
    # self allows object to refer to itself inside of its class
    # animals don't exist outside of the class
    # I want to change the objects self
        self.__name = name

    def get_name(self):
        return self.__name
    # called incapsulation
    # this is used to get the name because name is private from two underscores
    # basically incapsulation allows us to say "Hey is the name they passed in
    # here valid" Verifying data is good

    def set_name(self, name):
        self.__name = name

    def set_height(self, height):
        self.__height = height

    def set_weight(self, weight):
        self.__weight = weight

    def set_sound(self, sound):
        self.__sound = sound
    # there we go these are the setters and getter
    # variables we defined as setters and getters

    def get_type(self):
        print("Animal")

    # example of polymorphism

    def toString(self):
        return "{} is {} cm tall and {} kilograms and say {}".format(self.__name
                                                                     self.__height
                                                                     self.__weight
                                                                     self.__sound
                                                                     )
cat = Animal('Whiskers', 33, 10, 'Meow')

print(cat.toString())

# INHERITANCE
# inheritance means that when you inherit from another class that you already get
# all of the variables and methods from the class you're inheriting from

class Dog(Animal):
    __owner = ""

    def __init(self, name, height, weight, sound, owner):
        self.__owner = owner
    # overwrite the constructor to be more specific
    # what happens if I want the name height weigh and soudn to be
    # handled by the Animal Super Class' Constructor up here
        super(Dog, self).__init__(name, heigh, weight, sound)

    def set_owner(self, owner):
        self.__owner = owner
    # allows them to set owner by passing in a value
    def get_owner(self):
        return self.__owner

    def get_type(self):
        print("Dog")
    # we are using a dog object
    # we can also write functions in our super class below by overwriting a name
    # that's already within our superclass below
    def toString(self):
        return "{} is {} cm tall and {} kilograms and say {} His owner is {}".format(self.__name
                                                                         self.__height
                                                                         self.__weight
                                                                         self.__sound
                                                                         self.__owner
                                                                         )
    def multiple_sounds(self, how_many=None):
    # method overloading means that you'll be able to perform different
    # tasks based off of the attributes that are sent in
        if how_many is None:
            print(self.get_sound())
        else:
            print(self.get_sound() * how_many)

spot = Dog("spot", 53, 27, "Ruff", "Ben")

print(spot.toString())

# POLYMORPHISM
# Sounds really complicated
# All pmphism does is it allows you to refer to objects as their super class and
# automatically have the correct functions CALLED auotmatically

class AnimalTesting:
    def get_type(self, animal):
        animal.get_type()

test_animals = AnimalTesting()

test_animals.get_type(cat)
test_animals.get_type(spot)

spot.multiple_sounds(4)
spot.multiple_sounds()
