# Snake water gun

import random
lst = ['s','w','g']

chance = 5
no_of_chance = 0
comp_point = 0
user_point = 0

print("s for snake \nw for water \ng for gun \n")

while no_of_chance < chance:
    user = input('Snake,Water,Gun:')
    comp = random.choice(lst)

    if user == comp:
        print("Tie Both 0 point to each \n ")

    elif user == "s" and comp == "g":
        comp_point = comp_point + 1
        print(f"your guess {user} and computer guess is {comp} ")
        print("computer wins 1 point ")
        print(f"computer point is {comp_point} and your point is {user_point}\n  ")

    elif user == "s" and comp == "w":
        user_point = user_point + 1
        print(f"your guess {user} and computer guess is {comp} ")
        print("you wins 1 point ")
        print(f"computer point is {comp_point} and your point is {user_point}\n ")

    elif user == "w" and comp == "s":
        comp_point = comp_point + 1
        print(f"your guess {user} and computer guess is {comp} ")
        print("computer wins 1 point ")
        print(f"computer point is {comp_point} and your point is {user_point}\n ")

    elif user == "w" and comp == "g":
        user_point = user_point + 1
        print(f"your guess {user} and computer guess is {comp} ")
        print("user wins 1 point ")
        print(f"computer point is {comp_point} and your point is {user_point}\n")

    elif user == "g" and comp == "s":
        user_point = user_point + 1
        print(f"your guess {user} and computer guess is {comp} ")
        print("user wins 1 point ")
        print(f"computer point is {comp_point} and your point is {user_point}\n")


    elif user == "g" and comp == "w":
        comp_point = comp_point + 1
        print(f"your guess {user} and computer guess is {comp} ")
        print("computer wins 1 point ")
        print(f"computer point is {comp_point} and your point is {user_point}\n")

    else:
        print("you have input wrong \n")

    no_of_chance = no_of_chance + 1
    print(f"{chance - no_of_chance} is left out of {chance}\n")

print("Game over")

if comp_point==user_point:
    print("Tie")

elif comp_point > user_point:
    print("Computer wins and you loose")

else:
    print("you win and computer loose")

print(f"your point is {user_point} and computer point is {comp_point}")
