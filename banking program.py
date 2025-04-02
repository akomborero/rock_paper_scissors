#Banking program

def Show_Balance():
 print(f"your Balance is ${Balance:.2f}")
def Deposit():
  amount = float(input("Enter amount to be deposited: "))
  if amount < 0:
    print('amount is not valid')
    return 0
  else:
    return amount

def withdraw():
 amount = float(input("Enter amount to be withdrawn:  "))
 if amount is  Balance:
   print("insuffient balance")
 elif amount < 0:
  print("enter amount greater than 0")



Balance = 0
is_running = True

while is_running:
 print("*****************")
 print("Welcome to Banking Program")
 print("*****************")
 print("1.Show_Balance")
 print("2.Deposit")   
 print("3.Withdraw")
 print("4.Exit Program")

 choice = input("Enter option of Your choice: ")

 if choice ==  '1':
    Show_Balance()
 elif choice == '2':
    Balance +=Deposit()
 elif choice == '3':
  Balance -= withdraw()
 elif choice == '4':
  is_running = False
 else:
    print("*****************")
    print("invalid option")
    print("Thank you have an nice day")


