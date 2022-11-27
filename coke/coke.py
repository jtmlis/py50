#!/usr/bin/env python3
# import ipdb
def main():
    valid_coins = {
        "nickel" :float(0.05),
        "dime": float(0.10),
        "quarter":float(0.25),
    }
    balance = 0.50
    userPaid = int(input("Please insert a coin"))
    return(get_balance(userPaid,balance,valid_coins))

def get_balance(paid:float, balance: float, valid_coins: dict):
        for paid in valid_coins.values():
            balance =  balance - paid
            print(balance)
        else:
            print("please insert a valid coin")


main ()
