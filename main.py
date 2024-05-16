import subprocess
import sys

print("Welcome to my Snake Game")

while True:
    print("1. Easy Snake")
    print("2. Medium Snake")
    print("3. Hard Snake")
    print("0. Quit")
    choice = input("What is your choice: ")

    if choice == '0':
        sys.exit()
    elif choice == '1':
        subprocess.run(['python', 'easy_snake.py'])
    elif choice == '2':
        subprocess.run(['python', 'medium_snake.py'])
    elif choice == '3':
        subprocess.run(['python', 'hard_snake.py'])
    else:
        print("Invalid choice. please try again")
