balance=int(input("Enter Balance"))
withdraw=int(input("Enter Withdrawal Amount"))
c=0
if withdraw<balance:
    c=c+1
if withdraw%100==0:
    c=c+1
if withdraw>0:
    c=c+1
if c==3:
    print("WITHDRAWAL SUCCESSFUL")
    print("AMOUNT:",withdraw)
    balance=balance-withdraw
    print("BALANCE:",balance)
else:
    print("WITHDRAWAL CANCELLED")
    
