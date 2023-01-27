# global constants
MAX_LINES = 3

def deposit():
    # while loop because continuously ask user for amount till valid amount is entered
    while True:
        amount = input("What would you like to deposit? $")
        # check if amount is a number
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please enter a number.")
    
    return amount

def get_number_of_lines():
    # while loop because continuously ask user for amount till valid amount is entered
    while True:
        lines = input("Enter the number of lines to bet on (1-" + str(MAX_LINES) + ")? ")
        # check if amount is a number
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a valid number of lines.")
        else:
            print("Please enter a number.")
    
    return lines

def main():
    balance = deposit()
    lines = get_number_of_lines()
    print(balance, lines)

main()
