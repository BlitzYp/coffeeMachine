from data import menu, resources
from time import sleep
from os import system

if __name__ == "__main__":
    machine_money = 0
    while True:
        try:
            system("clear")
            report = "\n".join([f"{i}: {y}" for i, y in resources.items()]) + f"\nmoney: {machine_money}$"  
            print("-----PRICES------\n{}".format("\n".join(("{}: {}$".format(i, menu[i]["cost"]) for i in menu.keys()))))
            print(f"-----REPORT-----\n{report}")
            player_choice = input("Enter choice: (espressor/latte/cappuccino): ")
            quarters, dimes, nickles, pennies = float(input("Enter quarters: ")) * 0.25, float(input("Enter dimes: ")) * 0.10, float(input("Enter nickels: ")) * 0.05, float(input("Enter pennies: "))
            player_cash = sum((quarters, dimes, nickles, pennies))
            if sum(menu[player_choice]["ingredients"].values()) > sum(resources.values()):
                print("Not enough ingredients....")
                sleep(1)
                continue
            if player_cash < menu[player_choice]["cost"]:
                print("Not enough tokens, money refunded...")
                sleep(1)
                continue
            machine_money += menu[player_choice]["cost"]
            for k in resources.keys(): 
                resources[k] -= menu[player_choice]["ingredients"][k]
            print("Change given: {}$".format(round(player_cash - menu[player_choice]["cost"], 2)))
            print(f"Here is your {player_choice}. Enjoy the consumption of this particular beverage!")
            sleep(3)
        except KeyError:
            print("Sorry, but we don't have that beverage at the moment")
            sleep(1)
            continue