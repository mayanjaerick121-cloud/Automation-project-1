balance = 100000
while True:
    print("\n1.Check Balance")
    print("2.Deposit")
    print("3.Withdraw")
    print("4.Exit")

    choice = input("choose: ")
    if choice == "1":
        print("balance", balance)

    elif choice == "2":
        amount = int(input("Enter Deposit:")) 
        balance += amount
        print("Deposit Successfully")

    elif choice == "3":
        amount = int(input("Enter Withdrawal:"))
        if amount > balance:
            print("Insuficient funds")
        else:
            balance -= amount
            print("Withdrawal successfuly")

    elif choice == "4":
        break
    else:
        print("Invalid Choice")