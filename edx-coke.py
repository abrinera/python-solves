due=50
x=[25,10,5]
while due!=0:
    print("Amount Due:", due)
    coin=int(input("Insert Coin: "))
    if coin in x:
        due= due-coin
        if due<0 or due ==0:
            print("Change Owed:", abs(due))
            break
    else:
        pass


