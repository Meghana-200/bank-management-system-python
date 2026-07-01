accounts = {}

def create_account():
    acc = input("Enter Account Number: ")

    if acc in accounts:
        print("Account already exists!")
        return

    name = input("Enter Customer Name: ")
    balance = float(input("Enter Initial Deposit: "))

    accounts[acc] = {
        "name": name,
        "balance": balance
    }

    print("Account Created Successfully!")

def deposit():
    acc = input("Enter Account Number: ")

    if acc in accounts:
        amount = float(input("Enter Amount: "))
        accounts[acc]["balance"] += amount
        print("Deposit Successful!")
    else:
        print("Account Not Found!")

def withdraw():
    acc = input("Enter Account Number: ")

    if acc in accounts:
        amount = float(input("Enter Amount: "))

        if amount <= accounts[acc]["balance"]:
            accounts[acc]["balance"] -= amount
            print("Withdrawal Successful!")
        else:
            print("Insufficient Balance!")
    else:
        print("Account Not Found!")

def transfer():
    from_acc = input("From Account: ")
    to_acc = input("To Account: ")

    if from_acc in accounts and to_acc in accounts:
        amount = float(input("Enter Amount: "))

        if amount <= accounts[from_acc]["balance"]:
            accounts[from_acc]["balance"] -= amount
            accounts[to_acc]["balance"] += amount
            print("Transfer Successful!")
        else:
            print("Insufficient Balance!")
    else:
        print("Invalid Account Number!")

def check_balance():
    acc = input("Enter Account Number: ")

    if acc in accounts:
        print("\nAccount Number :", acc)
        print("Name           :", accounts[acc]["name"])
        print("Balance        :", accounts[acc]["balance"])
    else:
        print("Account Not Found!")

def view_accounts():
    if not accounts:
        print("No Accounts Found!")
        return

    print("\n------ ALL ACCOUNTS ------")

    for acc, details in accounts.items():
        print("---------------------------")
        print("Account :", acc)
        print("Name    :", details["name"])
        print("Balance :", details["balance"])

def search_account():
    acc = input("Enter Account Number: ")

    if acc in accounts:
        print("\nAccount Found")
        print("Name    :", accounts[acc]["name"])
        print("Balance :", accounts[acc]["balance"])
    else:
        print("Account Not Found!")

def delete_account():
    acc = input("Enter Account Number: ")

    if acc in accounts:
        del accounts[acc]
        print("Account Deleted Successfully!")
    else:
        print("Account Not Found!")

while True:

    print("\n========== BANK MANAGEMENT SYSTEM ==========")
    print("1. Create Account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Transfer Money")
    print("5. Check Balance")
    print("6. View All Accounts")
    print("7. Search Account")
    print("8. Delete Account")
    print("9. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        create_account()

    elif choice == "2":
        deposit()

    elif choice == "3":
        withdraw()

    elif choice == "4":
        transfer()

    elif choice == "5":
        check_balance()

    elif choice == "6":
        view_accounts()

    elif choice == "7":
        search_account()

    elif choice == "8":
        delete_account()

    elif choice == "9":
        print("Thank You!")
        break

    else:
        print("Invalid Choice!")