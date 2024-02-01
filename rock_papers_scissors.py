import random

 

options = ["Rock", "Paper", "Scissors"]

 

user_choice = input("Choose anyone from either Rock (r), Paper(p), or Scissors(s): ")

computer_choice = random.choice(options)

 
if user_choice == "r":
    print("You chose : Rock")
elif user_choice == "s":
    print("You chose: Scissors")
elif user_choice == "p":
    print("you chose: Paper")
else :r
    print("you chose", user_choice)


print("The Computer chose: ", computer_choice)

 

if user_choice == computer_choice:

    print("Oh no, It's a tie!")

elif user_choice == "Rock" or "r" and computer_choice == "Scissors":

    print("Congratulations, You win!")

elif user_choice == "Paper" or "p" and computer_choice == "Rock":

    print("Congratulations You win!")

elif user_choice == "Scissors" or "s" and computer_choice == "Paper":

    print("Congratulations, You win!")

else:

    print("Sorry You Loose and the Computer wins!")
