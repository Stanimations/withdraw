import sys
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

def main():
    # Print the welcome message in green
    print(Fore.GREEN + "Welcome to the program!")

    # Ask the user if they want to continue
    response = input("Do you want to continue from where you left off? ETA: 15 min (y/n): ").strip().lower()

    # Check the user's response
    if response == 'y' or response == '':
        # Print the error message
        print(Fore.RED + "Error: Please upload the .bin files generated on your PC. The current ones are damaged.")
    elif response == 'n':
        # Exit the program
        sys.exit()
    else:
        # Handle invalid input
        print(Fore.RED + "Invalid input. Please enter 'y' to continue or 'n' to exit.")

if __name__ == "__main__":
    main()
