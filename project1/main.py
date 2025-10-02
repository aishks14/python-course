# Python program to play Snake, Water, Gun game
'''
Legends:
1 - Snake
-1 - Water
0 - Gun
'''
import random
print("Welcome to Snake Water Gun Game!")
print("------------------------------")

def get_winner(user, computer):
    print("user --->>>", user)
    print("computer --->>>", computer)
    if user == 'q':
        print("Thanks for playing!")
    elif user not in chosen_option_dict:
        print("Invalid choice. Please try again.")
    else:
        if user == computer:
            return "It's a tie!"
        elif (user == 1 and computer == -1) or \
            (user == 0 and computer == 1) or \
            (user == -1 and computer == 0):
            return "You win!"
        else:
            return "Computer wins!"

choices = [-1, 0, 1, 2]
chosen_option_dict = { 
    "s": 1, 
    "w": -1, 
    "g": 0,
    "q": 2
}
output_dict = {
    1: "Snake",
    -1: "Water",
    0: "Gun",
    2: "Quit"
}
your_choice = input("Enter your choice('s', 'w', 'g' for choices and 'q' to exit): ").strip().lower()
computer_choice = random.choice([-1, 0, 1])
your_selection = chosen_option_dict[your_choice]
print(f"You chose: {output_dict[your_selection]}\nComputer chose: {output_dict[computer_choice]}")
result = get_winner(your_choice, computer_choice)
print(result)