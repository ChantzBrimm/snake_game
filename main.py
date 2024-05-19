import subprocess
import sys

print("Welcome to my Snake Game")


def controller_snake():
    while True:
        print("="*15+"Controller Snake"+"="*15)
        print("0. Exit")
        print("1. Easy snake")
        print("2. Medium snake")
        print("3. Hard snake")
        choice = input("What is your choice: ")

        if choice == '0':
            main()
        elif choice == "1":
            subprocess.run(["python3", "/Users/chantz/Documents/GitHub/snake_game/easy_snake.py"])
        elif choice == '2':
            subprocess.run(['python3', '/Users/chantz/Documents/GitHub/snake_game/medium_snake.py'])
        elif choice == '3':
            subprocess.run(['python3', "/Users/chantz/Documents/GitHub/snake_game/hard_snake.py"])
        else:
            print("Invalid choice. please try again")


def main():
    while True:
        print("="*15+"Snake Game"+"="*15)
        print("0. Quit")
        print("1. Snake using controller")
        choice = input("What is your choice: ")

        if choice == '0':
            sys.exit()
        elif choice == '1':
            controller_snake()
        else:
            print("Invalid choice. please try again")


if __name__ == '__main__':
    main()
