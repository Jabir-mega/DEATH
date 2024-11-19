
# # A variable ia container for a value. Behaves as the value itself 


# # Main data types 
# """1. dtrings
#     2. interger
#     3. floating pointnumber 
#     4. Booleans
# """
# # string-> (" ")
 
# # name = "Bro"
# # last_name = "code"
# # full_name = name + last_name # combibning different variable 
# # print("Hello" + full_name)
# # print(type(name))
# # # print(" Hello" + name)

# # interger-> number 
# age = 18
# age += 1
# print(age)
# print(type(age))
# print("your age is : " + str(age))
# print(type(age))

# # floats
# height = 280.5
# print(type(height)) 
# # booleans 
# human = False

# name = "Bro code"

# print(name.find("B"))
# print(name.isdigit()) # checks to see if the string is number or not : prints false or true
# print(name.replace("o", "a"))
# print(name.capitalize())
# print(name.upper())


# # # user input 

# # name = input("What is your name? : ")

# # print("Hello " + name)

# # age = int(input("how old are you? : "))
# # print (f"Your are  {age} years old" )
# # import math
# # pi = 3.14

# # # print(round(pi))
# # # print(math.ceil(pi)) #round up -> 4
# # # print(math.floor(pi)) # rounds down -> 3

# # # slicing  = is the way of extracting an element from  a string
# # #           You can either use  [] or slice()
# # # #               [start:stop;step]

# # # name = "Jabir Ali"

# # # first_name = name[0:5]
# # # last_name = name[6:]

# # # print(name)
# # # print(first_name)
# # # print(last_name)
# # # funky_name = name[0:10:2]
# # # print(funky_name)
# # # reverse_name = name[::-1]
# # # print(reverse_name)

# # # # slice()-> works the same as [] different is they use comma instead of colons 

# # # website = "http://google.com"

# # # slice = slice(7,-4)
# # # print(website[slice])

# # # if statement = a block of code which will execute if its condition is true 

# # # age = int(input("How old are you: "))

# # # if age >= 18:
# # #     print("You are an adult") 
# # # else:
# # #     print("You are not an adult")
    
# # #  while loops -> a statement that will execute its block of code, as long as its true its condition remains true 

# # # infinite loop 
# # # while 1 == 1:
# # #     print("Help")

# # # for loop -> a statement that will excute its block of code a limited amout of time 


# # for i in range(10):
# #     print(i + 1  )
    
    
# # import time   

# # for i in range(10, 0, -1):
# #     print(i)
# #     time.sleep(1)
# # print("wake up!!!")  
    
# # rows = int(input("How many rows? : "))
# # column = int(input("How many colomn? : "))
# # symbol = input("input the symbol? : ")

# # for i in range(rows):
# #     for j in range(column):
# #         print(symbol, end="")
# #     print()
    
    
# # looop control statement 
# #     break = terminate a programm
# #     continue = skips to the next iteration  
# #     pass = does nothing it isa place holder

# # # 2D list = a list of lists
# # drinks = ["coffe", "sodda", "tea"]
# # dinner = ["pizza", "hamburger", "hotdog"]
# # dessert  =["ice cream", "cake"]

# # food = [drinks, dinner, dessert]

# # print(food)

# # # tuples ->  
# # utensils = {"knife", "plate", "cup"}
# # dishes = {"spoon", "fork", "bowl"}
 
# # dinner_table = utensils.union(dishes)
# # print(dinner_table)


# # function -> a block of code which is executed only when it id called

# def hello(first_name, last_name):
#     print("Hello!" +first_name + last_name) 
    
        
# hello("bro" , "code")
# # hello("dude")
# # hello("man")

# # return -> used to return the result from a function since they keep it in memory 

# # *args -> a parameter that will pckall arguments into atuple so that a function will accept multiple arguments(positionsal arguments)
# #           args is just a place holder and the asterisks is th eimportant thing 
# # i.e
# def add(*args):
#     sum = 0
#     for i in args:
#         sum = sum + i
#     return sum


# print(add(1, 2, 3))

# **kwargs[KEYWORDARGUMENTS]  -> parameter that will pack arguments intoa dictionary  useful so that a function can accept a varying amount of keyword arguments

# def hello(**kwargs):
#     # print(f"hello {kwargs["first"]} {kwargs["last"]}")
#     print("hello", end=" ")
#     for key,value in kwargs.items():
#         print(value,end=" ")    
    
# hello(first = "Bro", last="code", middle="GYM")


# # string format -> format()

# animal = "cow"
# item = "moon"

# print(f"The {animal} jumped over the {item}")
# print("The {} jumped over the {}".format(animal,item))  

# number = 3.12159

# print("The number pi is {:.2f} ".format(number)) # f ->stands for floating point number 

# import random

# x = random.randint(1,6)
# y = random.random()

# mylist = ["rock", "paper", "scissors"]
# z = random.choice(mylist)


# card = [1,2,3,4,5,6,7,8,9,"J","Q","A","K"]

# random.shuffle(card)
# print(card)
# print(z)
# print(x)

# exception 
# you can put the code that may raise error within a try: i,].e
# try:
    ######
    #####
# except Exception:
    # print("Something went wrong")
    
# hence instead of raising error the above kine will be printed 

# import os

# path = "C:\\Users\\Administrator\\OneDrive\\Desktop\\text.txt"
# path = "C:\\Users\\Administrator\\OneDrive\\Desktop"

# if os.path.exists(path):
#     print("Location exists")
#     if os.path.isfile(path):
#         print("that is a file")
# else:
#     print("Location does not exists")
# 
# 
# oppenning a file
# try:     
#     with open("C:\\Users\\Administrator\\OneDrive\\Desktop\\DEATH\\test.txt") as file:
#         print(file.read())
# except FileNotFoundError:
#     print("that file was not found")
    
# print(file.closed)

# writting a file
# text = "yooooooo\n this is some text\n have a good one"
# with open("text.txt", "w") as file:
#     file.write(text)
 

import random
choices = ["rock", "paper", "scissors"]
computer = random.choice(choices)
player = None

def game():
    import random
    choices = ["rock", "paper", "scissors"]
    computer = random.choice(choices)
    player = None.lower()
    
    while player not in choices:
            player = input("rock, paper, or scissors?: ")
    if player  == computer:
            print("computer: ", computer)
            print("player: ", player) 
            print("Tie")
    elif player == "rock":
            if computer == "paper":
                print("computer: ", computer)
                print("player: ", player) 
                print("You loose")
            elif computer == "scissors":
                print("computer: ", computer)
                print("player: ", player) 
                print("You win")
    elif player == "paper":
            if computer == "rock":
                print("computer: ", computer)
                print("player: ", player) 
                print("You win")
            elif computer == "scissors":
                print("computer: ", computer)
                print("player: ", player) 
                print("You loose")
    elif player == "scissors":
            if computer == "rock":
                print("computer: ", computer)
                print("player: ", player) 
                print("You loose")
            elif computer == "paper":
                print("computer: ", computer)
                print("player: ", player) 
                print("You win")
    else:
        print("Retry pls")       
    

menu = "please choose from the following:\nA-To start game\nB-TO quit game \n:"


selection = input(menu).uppercase()
while selection != "B":
    if selection == "A":
       game()
    else:
        print("retry again!!",end=" " )
    selection = input(menu)