# print("Welcome to treasure\nIsland Your mission is to find the treasure")

# chioceDirection = input("Enter Direction Right or left ")
# if chioceDirection == "right":
#     chioce2 = input("Enter Swim or Wait ")
#     if chioce2 == "Wait":
#         choioce3 = input("Enter Which door Blue or Red ")
#         if choioce3 == "Blue":
#             print("You win congratulation")
#         else:
#             print("Game over")
#     else:
#         print("Game over")

# else :
#     print("Game Over")
# choice = input("Enter \'right or left' ").lower()
# if choice == "right":
#     print(f"you entered {choice}")
# else : 
#     print('You are wrong'
#            'you have to try again')

# import random
# import PythonApplication1


# GenerateRandam = random.randint(1,5)
# Counter = 0 ;

# while(GenerateRandam != 5):
#     Counter += 1;
#     print(f"Computer choose not 5 it choose {GenerateRandam}")
#     GenerateRandam = random.randint(1,5)
# print(f"Computer try {Counter} times until it reach 5 ")

# import random
# friends = random.choice(["Ibrahim" , "Sal" , "Mom" , "Yossif" , "AboNadeem"])
# # print(friends)

# Random_index = random.randint(a:0 ,b: 5)
# print(friends[Random_index])

# fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
# vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

# Dirty_food = [fruits , vegetables]
# print(Dirty_food[1][1])

# small apps for rock paper scissors 

from ast import Num
from queue import Full
from tokenize import String
from typing import Type



# print("choice sccers choice 1 , peper choice 2 , Rock choice 3")
# user_Count = 0 ; 
# Computer_Count = 0 ; 

# while user_Count != 3 or Computer_Count != 3:
#    user_choice = input("Choice S , R , P ")
#    Computer_choice = random.choice(["S" , "R" , "P"])
#    if (user_choice == "S" and Computer_choice == "P") or\
#    (user_choice == "R" and Computer_choice == "S" ) or\
#   (user_choice == "P" and Computer_choice == "R"):
#     print("User Win")
#     user_Count += 1; 
#    else :
#     print("Computer Win")
#     Computer_Count += 1

# if user_Count == 3 :
#     print ("\n\nGreate you win ")
# else:
#     print("\n\nComputer win")


# using loop starting with for loop 
# Fruits = ["Appel" , "Bananen" , "Orange" , "Grops"]
# Fruit_like =[]

# for fruit in Fruits :
#     if fruit == "Appel" or fruit == "Orange":
#         Fruit_like.append(fruit)
#     print(fruit)

# print("This is the list of all the fruits")
# print("The fruit that i like it is ")
# for Like_Fruit in Fruit_like:
#    (len(Fruits))
# print(Fruits[3 print(Like_Fruit)
# print])

# Names = ["Ibrahim" , "Sadik" , "Alnagar"]
# Reverse_Names = []
# lenght_Name = len(Names)


# for Name in Names:
#        lenght_Name -= 1
#        Reverse_Names.append(Names[lenght_Name])
       
# print(Reverse_Names)


# myScores = [12 ,343,55,667,444,55,23,57,12,12]
# currentNum =0

# def getMaxNumber(Max , currentNum):
#     if Max > currentNum:
#         currentNum = Max
#         return Max
#     return currentNum

# for Max in myScores :
#   currentNum = getMaxNumber(Max , currentNum)
 
# print(max) 

# practice about dic

# car = {"Brand" : "toyota" , "model" : "corolla" , "Year" : 2020}
# print(car)

# car["Year"] = 2024
# print(car)
# car["Colour"] = "Blue"; 
# print(car)

# num_List =[1,3,4,5,2,1]

# dic_23 = {}
# dic_23[num_List[0]] = 2;
# print(dic_23)
# name = "Ibrahim"
# Count_deplocate = 0; 
# variable_deplocate = "";
# dic_deplocate = {}


# for i in name : 
#     for j in name : 
#         if i == j :
#             variable_deplocate = i ; 
#             Count_deplocate = j;
#     dic_deplocate = {variable_deplocate , Count_deplocate}

# Number = 100 

# for Number in range(1,11):
#     print(Number)


# print("Hello World")

# numbersOfTimesToUseCalc = 0 

# numbersOfTimesToUseCalc = int(input("Enter How many numbers do you want to use the calclation ")); 

# while numbersOfTimesToUseCalc != 0 :
#     num1 = int(input("Enter the first number ")); 
#     num2 = int(input("Enter the second number  ")); 

#     synbol = input("Enter what type of calculation you want ");

#     if synbol == "+" or synbol == "-" or synbol == "/" or synbol == "*":
#         if synbol == "+":
#            print(f"Result is  {num1 + num2}")
#         elif synbol == "-":
#             print(f"Result of substract is {num1 - num2}");
#         elif synbol == "/":
#             print(f"Result of divion is {num1 / num2}"); 
#         elif synbol == "*":
#             print(f"Result of multiplcation is {num1 * num2}"); 
#     else:
   
#         inputStringAllow = str(input("Do you want to enter again numbers press yes if no it will give you the reminder by privous input "))
#         if inputStringAllow == "yes":
#              print("Know we will check about the reminder of moduler ")
#              number1 = int(input("Enter the first check number"))
#              number2 = int(input("Enter the Second check number"))

#              if number1 % number2 == 0 : 
#                     print("the Result have reminder ")
#              else: 
#                     print("the Result have no reminder ")
#         elif inputStringAllow != "Yes":
#              if num1 % num2 == 0 : 
#                  print("the Result have reminder ")
#              else: 
#                     print("the Result have no reminder ")
#     numbersOfTimesToUseCalc -=  1


# print("Hello World")

# def add(x, y):
#     return x + y

# def sub(x, y):
#     return x - y

# def multi(x, y):
#     return x * y

# def divide(x, y):
#     return x / y


# operations = {
#     '+': lambda num1, num2: num1 + num2,
#     '-': lambda num1 , num2: num1 - num2,
#     '*': lambda num1 , num2 : num1 * num2,
#     '/': lambda num1 , num2 : num1 / num2,
# }

# numbersOfTimesToUseCalc = int(input("Enter how many numbers you want to use the calculation: "))

# while numbersOfTimesToUseCalc != 0:
#     num1 = int(input("Enter the first number: "))
#     num2 = int(input("Enter the second number: "))

#     symbol = input("Enter the type of calculation you want (+, -, *, /): ")

#     if symbol in operations:
#         result = operations[symbol](num1, num2)
#         print(f"Result is {result}")
#     else:
#         inputStringAllow = input("Invalid symbol! Do you want to enter numbers again? (yes/no): ").lower()

#         if inputStringAllow == "yes":
#             print("Now we will check about the remainder (modulus)")
#             number1 = int(input("Enter the first check number: "))
#             number2 = int(input("Enter the second check number: "))

#             if number1 % number2 == 0:
#                 print("The result has no remainder.")
#             else:
#                 print("The result has a remainder.")
#         else:
#             if num1 % num2 == 0:
#                 print("The result has no remainder.")
#             else:
#                 print("The result has a remainder.")

#     numbersOfTimesToUseCalc -= 1


# for number in range(1,101): 
#     if number % 3 == 0 :
#         print("Fizz")
#     elif number % 5 == 0 :
#         print("Buzz")
#     elif number % 3 == 0 and number % 5 == 0 : 
#                 print("FizzBuzz")
#     else :
#         print(number)

# n = 3

# if n % 2 == 0 and 2 <= n <= 5:
#     print("Not Weird")
# elif n % 2 == 0 and 6 <= n <= 20: 
#     print("Weird")

# elif n % 2 == 0 and n > 20:
#     print("Not Weird")
# elif n % 2 != 0 : 
#     print("Weird")


# a = int(input())
# b = int(input())
# print(a+b)
# print(a-b)
# print(a*b)
      
# a  = int(input())
# b  = int(input())
# print(int(a / b))
# print(float(a / b))

# def Is_Leap(year):
#     if (year % 4 == 0 ) and (year % 100 != 0 ) or ( year % 400 == 0):
#       return True
#     else: 
#         return False 
# year = int(input())
# print(Is_Leap(year))
  

# def is_leap(year):
#     leap = False
    
#     if (year % 4 == 0 ) and (year % 100 != 0 ) or ( year % 400 == 0):
#      return True
#     else: 
#      return False 
    
#     return leap

# year = int(input())
# print(is_leap(year))

# n = int(input())
# result = ""
# for i in range(1, n +1):
#     result += str(i)
# print(result)

# n = int(input())  # number of scores
# scores = list(map(int, input().split()))  # read scores as a list of ints

# unique_scores = set(scores)  # remove duplicates

# unique_scores.remove(max(unique_scores))  # remove the highest score

# runner_up = max(unique_scores)  # max of remaining is runner-up

# print(runner_up)
# print(scores)

# to create list 
# x = int(input())
# y = int(input())
# z = int(input())
# n = int(input())

# result = [[i , j , k ] 
#           for i in range(x + 1)
#           for j in range(j + 1)
#           for k in range(k + 1)
#           if i + j + k != n ]
# print(result)
# n = int(input())  
# scores = list(map(int, input().split())) 

# unique_scores = set(scores) 
# unique_scores.remove(max(unique_scores)) 

# runner_up = max(unique_scores) 

# print(runner_up)
# print(scores)

# creating dictionary 
# student = {}
# student["Ibrahim"] = [85 , 343 , 444]
# student["Ismail"] = [90 , 455, 566]
# student["Ishrak"] = [94 , 33 , 335]

# TotalResult = student["Ibrahim"]

# avarage = sum(TotalResult) / len(TotalResult)

# print(f"Alice's average is: {avarage:.2f}")

# myList = []
# myList.append(3)
# myList.append(8)
# myList.insert(1,5)
# myList.remove(3)
# print(myList)
# myList.reverse()
# print(myList)

# num2 = ["1" , "2" , "3"]
# print(num2)

# print("convert the num2 to integer using map")
# convN = list(map(int , num2))
# print(convN)

# if __name__ == '__main__':
#     N = int(input())
#     my_list = []
#     for _ in range(N):
#         command = input("Enter command: ").split()
#         cmd = command[0]
#         args = command[1:]

#         if cmd == 'insert':
#             i, e = map(int, args)
#             my_list.insert(i, e)
#             print(f"Inserted {e} at position {i}: {my_list}")
#         elif cmd == 'print':
#             print(f"Current list: {my_list}")
#         elif cmd == 'remove':
#             e = int(args[0])
#             my_list.remove(e)
#             print(f"Removed first occurrence of {e}: {my_list}")
#         elif cmd == 'append':
#             e = int(args[0])
#             my_list.append(e)
#             print(f"Appended {e} to the end: {my_list}")
#         elif cmd == 'sort':
#             my_list.sort()
#             print(f"Sorted list: {my_list}")
#         elif cmd == 'pop':
#             popped = my_list.pop()
#             print(f"Popped last element {popped}: {my_list}")
#         elif cmd == 'reverse':
#             my_list.reverse()
#             print(f"Reversed list: {my_list}")

# Today i will start with tuple , set , list

# TryTuple = (1, 2)
# print(hash(TryTuple))

# if __name__ == '__main__':
#     n = int(input())
#     integer_list = map(int, input().split())
#     t = tuple(integer_list)
#     print(hash(t))

# i want to change the letter inside the string 

# word = "Hello"
# position = 0
# NewLetter = "Y"

# NewWord = NewLetter + word[position+1:]
# print(NewWord)

# check of the string contain alphabit 
# s = input()
# checkInput = s.isalnum()
# # print(checkInput)

# words = []
# for _ in range(3):
#     word = input()
#     words.append(word)
# print("-----------")

# for _ in range(len(words)):
#     print(words[_])

# to do password generator
import random

mylistString = ["ibrahim" , "Sadik " , "alnagar"]
mylistInteger = [1, 2 ,4, 5,6,7,8,9,10]


RondomChoose = random.choice(mylistString)+ str( random.choice(mylistInteger))
print(RondomChoose)