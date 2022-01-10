def atm():
    print("ATM SERVICES")
    service=int(input("WELCOME TO ATM PROGRAMME:\n press 1 for homepage\n press 2 for registeration\n press 3 for ATM:"))
    if service==1:
        atm()
    elif service==2:
        registration()
    elif service==3:
        atm_service()
    else:
        atm()
def registration():
    card1=[12345]
    pin1=[1234]
    print("register for atm services")
    print("enter the following details:")
    name=input("enter the name:")
    ph_no=input("enter the phone number:")
    address=input("enter the address:")
    print("generating debit card number.....")
    import random
    a=random.randrange(99999)
    print("your debit card number is:",a)
    import random
    b=random.randrange(9999)
    print("ATM pin generated is:",b)
    card1.append(a)
    pin1.append(b)
    print("debit card no is",card1)
    print("debit card pin is",pin1)
    print("registered successfully!!")
def atm_service():
    print("welcome for atm services")
    card=int(input("enter your debit card number:"))
    pin=int(input("enter your pin:"))
    if(card in card1 and pin in pin1):
        sel=int(input("ATM SERVICE\n 1.check_bal\n 2.cash_withdraw\n 3.deposit\n 4.quit\n please enter your choice:"))
        if(sel==1):
            check_bal()
        elif(sel==2):
            cash_withdraw()
        elif(sel==3):
            deposit()
        else:
            atm()
def check_bal():
    amt=12500
    print("current balance:",amt)
    atm()
def cash_withdraw():
    amt=12500
    print("enter the amount to be withdrawn")
    a=int(input("amount:"))
    bal=amt-a
    print("balance:",bal)
    atm()
def deposit():
    amt=12500
    print("enter the amount to be deposited")
    a=int(input("amount:"))
    bal=amt+a
    print("balance:",bal)
    atm()
atm()    

