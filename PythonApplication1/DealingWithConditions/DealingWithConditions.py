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

from queue import Full
from tokenize import String



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


myScores = [12 ,343,55,667,444,55,23,57,12,12]
currentNum =0

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

fullName = "ibrahim"
checkIfRepeat = False
lenghtString = len(fullName)

print = fullName[1]

for i in range(0, lenghtString) :
    for j in range(1, lenghtString):
        if fullName[i] == fullName[j] :
            print(f"there is a deplucate {j}" )
        
print("Sayad")
    


