import random

chance=10
no_of_chance=0
human_point=0
computer_point=0
list=['s','w','g']

print("\n\t\t\t\t\t\t\t\t\t\t\t\t\t\tWelcome to Snake Water and Gun game\n\n")
print("\t\tPress 'S' for Snake\n\t\tPress 'W' for Water\n\t\tPress 'G' for Gun\n\n")

while(no_of_chance<chance):
    _input=input("Snake,Water,Gun:- ")
    _random=random.choice(list)

    if(_input==_random):
        print("Tie, Both 0 points to each\n")

    elif(_input=='s' and _random=='w'):
        human_point=human_point+1
        print(f"Your guess is {_input} and computer guess is {_random}\n")
        print("Human wins 1 point\n")
        print(f"Your point is {human_point} and computer point is {computer_point}\n")
    elif(_input=='s' and _random=='g'):
        computer_point = computer_point + 1
        print(f"Your guess is {_input} and computer guess is {_random}\n")
        print("Computer wins 1 point\n")
        print(f"Your point is {human_point} and computer point is {computer_point}\n")

    elif(_input=='w' and _random=='g'):
        human_point=human_point+1
        print(f"Your guess is {_input} and computer guess is {_random}\n")
        print("Human wins 1 point\n")
        print(f"Your point is {human_point} and computer point is {computer_point}\n")
    elif(_input=='w' and _random=='s'):
        computer_point = computer_point + 1
        print(f"Your guess is {_input} and computer guess is {_random}\n")
        print("Computer wins 1 point\n")
        print(f"Your point is {human_point} and computer point is {computer_point}\n")

    elif(_input=='g' and _random=='s'):
        human_point=human_point+1
        print(f"Your guess is {_input} and computer guess is {_random}\n")
        print("Human wins 1 point\n")
        print(f"Your point is {human_point} and computer point is {computer_point}\n")
    elif(_input=='g' and _random=='w'):
        computer_point = computer_point + 1
        print(f"Your guess is {_input} and computer guess is {_random}\n")
        print("Computer wins 1 point\n")
        print(f"Your point is {human_point} and computer point is {computer_point}\n")
    else:
        print("You have entered wrong input")

    no_of_chance=no_of_chance+1
    print(f"{chance-no_of_chance} is left out of {chance} chances\n\n")

print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t-----GAME OVER-----\n")

if computer_point>human_point:
    print("\n\t\t\t\t\t\t\t\t\t\t\t\t\t\tComputer wins and you loose\n")
elif human_point<computer_point:
    print("\n\t\t\t\t\t\t\t\t\t\t\t\t\t\tYou win and Computer loose\n")
else:
    print("\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tGame is draw!\n")

print(f"\n\t\t\t\t\t\t\t\t\t\t\t\tYour point is {human_point} and computer point is {computer_point}")