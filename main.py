# 5A
import math as m

def check_num(str): 
    while True:
        num = input(str)
        if num.lower() == 'end':
            return False

        try:
            val = int(num)
            print("✅ Verification passed, system recieved: ", val)
            return val
        except ValueError:
            try:
                val = float(num)
                print("✅ Verification passed, system recieved: ", val)
                return val
            except ValueError:
                print("❌Invlaid entry. Please enter a number")

def many():
    expenses = []
    count = 0
    print('Type end at any time to stop entering expenses')
    while True:
            val = check_num('Expense: ' + str(count)  + '. Please enter your next expense: ')
            if val == False:
                return calc(expenses)
            else:
                expenses.append(val)
                count += 1

def set_amount(num):
    count = 0
    expenses = []

    while num > count:
        val = check_num('Expense: ' + str(count) + '/' + str(num) + ' Please enter your next expense: ')
        expenses.append(val)
        count += 1
    
    calc(expenses)

def calc(list):
    rate = check_num("How much do you make an hour? (Exclude $)")
    print('Your hourly rate is: $', rate, 'and your total expenses are: $', sum(list))
    return print('You need to work:', m.ceil(sum(list) / rate), 'hours to cover your expenses.')

def main():
    response = check_num('Please enter 0 to enter any number of expenses, or 1 to enter a set number of expenses ')
    while True:
        if response == 0:
            return many()
        elif response == 1:
            num = check_num('How many expenses? ')
            return set_amount(num)
        else:
            print("❌Invlaid entry. Please enter either 0 or 1")
            response = check_num('Please enter 0 to enter any number of expenses, or 1 to enter a set number of expenses ')
main()
