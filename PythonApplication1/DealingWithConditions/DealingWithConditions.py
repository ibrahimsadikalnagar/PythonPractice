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

import random
import PythonApplication1


GenerateRandam = random.randint(1,5)
Counter = 0 ;

while(GenerateRandam != 5):
    Counter += 1;
    print(f"Computer choose not 5 it choose {GenerateRandam}")
    GenerateRandam = random.randint(1,5)
print(f"Computer try {Counter} times until it reach 5 ")