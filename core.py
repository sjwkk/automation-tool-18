import sys
import random

def get_user_input(prompt):
    try:
        user_input = input(prompt)
        if not user_input.strip() or not user_input.isdigit():
            raise ValueError('Input must be a non-empty numeric string')
        return int(user_input)
    except EOFError:
        print('End of input stream. Exiting.')
        sys.exit()
    except ValueError as e:
        print(e)
        return get_user_input(prompt)


def main_loop():
    print('Welcome to the game!')
    while True:
        user_choice = get_user_input('Enter a number (1-100) to guess or 0 to exit: ')
        if user_choice == 0:
            print('Thanks for playing! Goodbye!')
            break
        elif 1 <= user_choice <= 100:
            print(f'You guessed: {user_choice}')
            random_number = random.randint(1, 100)
            if user_choice == random_number:
                print('Congratulations! You guessed it right!')
            else:
                print(f'Wrong guess! The number was {random_number}.')
        else:
            print('Invalid choice. Please try again.')

if __name__ == '__main__':
    main_loop()
