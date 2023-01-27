import random

# assumption - 3 x 3 slot machine, only get a line if get 3 in a row

# global constants
MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

# SLOT MACHINE
ROWS = 3
COLS = 3

# think of symbols like values in each column
# here A is modeled such that it is most valuable and hence has leant number of ocurrences

symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

def get_slot_machine_spin(rows, cols, symbols):
    # generate what symbols are going to be in each column based on frequency
    all_symbols = []

    # this will add a symbol as many times as its count in dictionary
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)

    return columns

def print_slot_machine(columns):
    # need to transpose the matrix
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row])

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


def get_bet():
    # while loop because continuously ask user for amount till valid amount is entered
    while True:
        amount = input("How much would you like to bet on each line? $")
        # check if amount is a number
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET}.")
        else:
            print("Please enter a number.")
    
    return amount    


def main():
    balance = deposit()
    lines = get_number_of_lines()

    # this loop is to check bet against balance
    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(f"You do not have enough to bet that amount, your current balance is: ${balance}")
        else:
            break

    # summarizing the bet
    print(f"You are betting ${bet} on {lines} lines. Total bet is ${total_bet}")

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)

main()
