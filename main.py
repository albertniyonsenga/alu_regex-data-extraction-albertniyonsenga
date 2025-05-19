from colorama import init, Fore
from validator import VALIDATORS

# Demonstrate the different behavior when autoreset is True and False.
"""So better to make it True so that whenever we assign color 
it doesn't affect other which is not assigned to.
"""

init(autoreset=True)

def display_menu():

    print(Fore.MAGENTA + "\n" + "-"*50)
    print(Fore.MAGENTA + " REGULAR EXPRESSION VALIDATOR ".center(50, ' '))
    print(Fore.MAGENTA + "_"*50)
    print("\nAvailable validation options:\n")

    # Getting all validators and assign number to them so that we can call them with ease
    for i, (key, validator) in enumerate(VALIDATORS.items(), 1):
        print(Fore.YELLOW + f"{i}. {key.capitalize()}")# And make the keys capitalized at first letter

    print(Fore.YELLOW + "0. Exit")

def get_user_choice():
    while True:
        try:
            choice = int(input("\nEnter your choice (0-4): "))
            if 0 <= choice <= len(VALIDATORS):
                return choice
            print(Fore.RED + "Invalid choice. Please try again.")
        except ValueError:
            print(Fore.RED + "Please enter a valid number.")

def main():
    while True:
        display_menu()
        choice = get_user_choice()
        
        if choice == 0:
            print("\nThank you for using Our Regex Validator")
            break

        """How it works:
        1. Here will get the choice minus one to get actual index of the keys
        2. Then we call the validation function by using its index from step 1
        3. Then after we get the user input and assign it to the attribute of our function from step 2.
        """
        validator_name = list(VALIDATORS.keys())[choice-1]
        validator_fn = VALIDATORS[validator_name]
        user_input = input(f"\nEnter text to validate as {validator_name}: ").strip()
        
        result = validator_fn(user_input) # Which will return dictionary with valid, matches and description
        
        print("\n" + "-"*50)
        if result['valid']:
            print(Fore.GREEN +"Valid format detected!")
            print(f"Matched values: {', '.join(result['matches'])}")
        else:
            print(Fore.RED + "Invalid format detected!\n")
            print(Fore.MAGENTA + result['description'])
        
        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()