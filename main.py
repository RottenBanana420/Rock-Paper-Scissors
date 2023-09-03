import random as rd
import os

options=["Rock", "Paper", "Scissor"]

score=0

continueplaying=1

while continueplaying==1:
    print("\n\nWELCOME TO A CLASSIC GAME OF ROCK, PAPER AND SCISSORS")
    try:
        user_choice=int(input("\nInput your choice:\n1. Rock\n2. Paper\n3. Scissor\n-> "))
    except:
        print("Invalid Option Entered! Please Try Again...\n")
        continue


    if user_choice==1:
        user_choice="Rock"
    elif user_choice==2:
        user_choice="Paper"
    elif user_choice==3:
        user_choice="Scissor"
    else:
        print("Invalid Value!")
        continue

    computer=options[rd.randint(0,2)]

    print("\n",user_choice+" vs "+computer)

    if user_choice=="Rock" and computer=="Scissor":
        print("User won this round!")
        score+=1
    elif user_choice=="Paper" and computer=="Rock":
        print("User won this round!")
        score+=1
    elif user_choice=="Scissor" and computer=="Paper":
        print("User won this round!")
        score+=1
    elif user_choice==computer:
        print("Its a draw...")
    else:
        print("\nComputer won this round!")

    print("\nYour Score: ",score)

    print("\nDo you want to continue?\n1. Yes\n2. No")
    try:
        continueplaying=int(input())
    except ValueError:
        print("\nPlease Select the appropriate option from the list!")
        continue

    os.system("clear")

print("Thank You for Playing!")