import random
user_score=0
computer_score=0
print("Welcome to game-Snake Water Gun. ")
r=int(input("Enter Number of rounds you want"))
list=["Snake","Water","Gun"]
computer_turn=random.choice(list)
round=1
while round<=r:
    user = input("Choose what do you want\n S for snake\n W for water \n G for gun")
    if user == 'S' or user == 's':
        print("You Have chosen Snake")
    elif user == 'W' or user == 'w':
        print("You have chosen Water")
    elif user == 'G' or user == 'g':
        print("You have chosen Gun")
    else:
        print("Wrong Input Please Try Again")
    if computer_turn=='Snake':
        if user=='S' or user=='s':
            print("It is a Draw Please Try Again")
            user_score=user_score+0
            computer_score=computer_score+0

        elif user=='W' or user=='w':
            print("Snake Drink the Water\n You loose😂")
            user_score = user_score + 0
            computer_score = computer_score + 1

        elif user=='G' or user=='g':
            print("Snake Found Dead \nYou win")
            user_score = user_score + 1
            computer_score = computer_score + 0
    if computer_turn=='Water':
        if user=='S' or user=='s':
            print("Snake Drink the Water\n You Win🥳")
            user_score = user_score + 1
            computer_score = computer_score + 0
        elif user=='W' or user=='w':
            print("It is a Draw Please Try Again")
            user_score = user_score + 0
            computer_score = computer_score + 0
        elif user=='G' or user=='g':
            print("Gun gone in water\n You Loose")
            user_score = user_score + 0
            computer_score = computer_score + 1
    if computer_turn=='Gun':
        if user=='S' or user=='s':
            print("Snake Found Dead \nYou loose")
            user_score = user_score + 0
            computer_score = computer_score + 1
        elif user=='W' or user=='w':
            print("Gun gone in water\n You Win🥳")
            user_score = user_score + 1
            computer_score = computer_score + 0
        elif user=='G' or user=='g':
            print("It is a Draw Please Try Again")
            user_score = user_score + 0
            computer_score = computer_score + 0
    round=round+1
print("Your Score is",user_score)
print("Computer score is",computer_score)
if user_score>computer_score:
    print("You Win")
elif user_score<computer_score:
    print("You Loose")
else:
    print("It is a tie") 