amount=50
while amount>0:
    print("Amount Due:", amount)
    coin=int(input("Insert Coin:"))
    if coin==10 or coin==25 or coin==5:
        amount=amount-coin
    else:
        amount=amount
print("Change Owed:" , amount*-1)