#!/usr/bin/env python3
# import ipdb
def main():
   balance = 50
   while balance > 0:
       coin = int(input("please insert a coin : "))
       if coin == 5 or coin == 10 or coin ==25 or coin == 50:
           balance = balance - coin
           print(f"{balance} is your new balance")
       else:
           print("insert a valid coin")
           break
   change_owed = abs(balance)
   print(f"Change Owned :{change_owed}")

main()
