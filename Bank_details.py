from random import choice
from os import remove
session_counter = 0

def getValInt(n): # Ensures that the user enters an integer
    try:
        return int(n)
    except ValueError:
        return None

def getValFloat(n): # Ensures that the user enters a float
    try:
        return round(float(n), 2)
    except ValueError:
        return None

def get_username_password(): ##Gets the staff username & password
    print()
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    return username, password

def staff_txt(): ## Creates file for storing staff details
    try:
        customer = open("customer.txt", "x")
    except:
        pass
    staff = open("staff.txt", 'w+')
    staff.write("Username: omtolulope,Password: tolumosope89,Email: tolulope@accessbank.com,Fullname: Oluwaseun M. Tolulope\n")
    staff.write("Username: k_oyovota,Password: thebestw@y2lv,Email: kevin.oyovota@accessbank.com,Fullname: Kevin E. Oyovota\n")
    staff.close()
    return

def chk_usrnm_psswrd(usrnm, psswrd): ##checks if the username and password are correct
    staff = open("staff.txt", 'r')
    if staff.mode == 'r':
        staff_details = staff.readlines()

    for staff_member in staff_details:
        item  = staff_member.split(',')
        if (f'Username: {usrnm}', f'Password: {psswrd}') == (item[0], item[1]): #compares the username and password to the ones in staff.txt
            staff.close()
            return True, item[0]
    return False, None


def new_account(usr_name): ## creates a new account
    global session_counter
    customer = open("customer.txt", 'a+')
    acc_name = input("\nPlease enter the account name: ")
    open_balance = input("Enter the opening balance: ")
    while True:
        open_balance = getValFloat(open_balance)
        if open_balance == None:
            open_balance = input("Please enter a valid amount: ")
        else:
            break
    acc_type = input("Enter the acount type: ")
    email = input("Enter the customer's email: ")

    acc_number = ''
    for i in range(10):
        acc_number += choice("0123456789")
    customer.write("Account Number: " + acc_number + ',' + "Account Name: " + acc_name + ',' + "Opening Balance: " + str(open_balance) + ' Naira' + ',' + "Account Type: " + acc_type + ',' + "Email: " + email + '\n')
    customer.close()
    print("The account number for the new customer is " + acc_number)

    if session_counter > 0:
        session = open("session.txt", "a+")
    else:
        session = open("session.txt", "w+")
    session.write(usr_name + ',' + "Account Number: " + acc_number + ',' + "Account Name: " + acc_name + ',' + "Opening Balance: " + str(open_balance) + ' Naira' + ',' + "Account Type: " + acc_type + ',' + "Email: " + email + '\n')
    session.close()
    session_counter += 1

    return staff_ops(usr_name)

def acc_details(user_name): ## Search for and display an account
    acc_no = input("\nPlease enter the account number: ")
    customer = open("customer.txt", "r")
    cust_details = customer.readlines()
    for cust in cust_details:
        if f"Account Number: {acc_no}" in cust:
            account = cust.split(',')
            print()
            for item in account:
                datum = item.split(': ')
                datum[0] += ':'
                print(datum[0].ljust(17, ' '), end='')
                print(datum[1])   
            break
    else:
        print("Account not found.")

    return staff_ops(user_name)

def staff_ops(usr_name): ##staff operation
    global session_counter
    prompt = input("\n1. Create new bank account.\n2. Check account details.\n3. Log out.\nEnter an option (1, 2 or 3): ")
    while True:
        prompt = getValInt(prompt)
        if prompt == None or prompt not in [1, 2, 3]:
            prompt = input("Please enter 1, 2 or 3: ")
        else:
            break
    if prompt == 1:
        new_account(usr_name)
    elif prompt == 2:
        acc_details(usr_name)
    else:
        print("End of session.\n\n")
        session_counter = 0
        try:
            remove("session.txt")
        except:
            pass
        main()

def main():
    print("1. Staff Login\n2. Close App")
    prompt = input("Enter an option (1 or 2): ")

    while True:
        prompt = getValInt(prompt)
        if prompt == None or prompt not in [1, 2]:
            prompt = input("Please enter 1 or 2: ")
        else:
            break

    if prompt == 1:
        while True:
            usrnm, psswrd = get_username_password()
            validated, usr_name = chk_usrnm_psswrd(usrnm, psswrd)
            if validated:
                break
            else:
                print('Username or password invalid. Try again.\n')
                continue

        staff_ops(usr_name)
    else:
        print("Program termiinated.")
        return


if __name__ == '__main__':
    staff_txt()
    main()
