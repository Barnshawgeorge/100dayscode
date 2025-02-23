from art import logo, coffee_logo
from menu import MENU, resources, money
from currency import QUARTER, DIMES, NICKLES, PENNIES

machine_off = False
money_in = 0.0

def refill_resources():
    resources["water"] = 300
    resources["milk"] = 200
    resources["coffee"] = 100

def print_report():
    for key in resources:
        if(key == "water" or key == "milk"):
            print(f"{key}: {resources[key]}ml")
        if(key == "coffee"):
            print(f"{key}: {resources[key]}g")
    print(f"Money: ${float(money["value"])}")

def calc_coins():
    global money_in
    get_quarters = int(input("How many quarters?: "))
    money_in += float(get_quarters * QUARTER)
    get_dimes = int(input("How many dimes?: "))
    money_in += float(get_dimes * DIMES)
    get_nickles = int(input("How many nickles?: "))
    money_in += float(get_nickles * NICKLES)
    get_pennies = int(input("How many pennies?: "))
    money_in += float(get_pennies * PENNIES)
    
def print_espresso():
    global money_in
    print(f"Espresso costs ${MENU["espresso"]["cost"]} Please insert coins.")
    calc_coins()
    if(MENU["espresso"]["ingredients"]["water"] > resources["water"]):
        print("Sorry, not enough water in the machine.")
        return
    if(MENU["espresso"]["ingredients"]["coffee"] > resources["coffee"]):
        print("Sorry, not enough coffee in the machine.")
        return
    if(money_in < MENU["espresso"]["cost"]):
        print("Sorry thats not enough money. Money refunded")
    else:
        resources["water"] -= MENU["espresso"]["ingredients"]["water"]
        resources["coffee"] -= MENU["espresso"]["ingredients"]["coffee"]
        print(f"Purchase successful! Here is your change: ${money_in - MENU["espresso"]["cost"]:.2f}")        
        money["value"] += MENU["espresso"]["cost"]
        money_in = 0.0
        print("Enjoy your Espresso!")

def print_latte():
    global money_in
    print(f"Latte costs ${MENU["latte"]["cost"]} Please insert coins.")
    calc_coins()
    if(MENU["latte"]["ingredients"]["water"] > resources["water"]):
        print("Sorry, not enough water in the machine.")
        return
    if(MENU["latte"]["ingredients"]["milk"] > resources["milk"]):
        print("Sorry, not enough milk in the machine.")
        return
    if(MENU["latte"]["ingredients"]["coffee"] > resources["coffee"]):
        print("Sorry, not enough coffee in the machine.")
        return
    if(money_in < MENU["latte"]["cost"]):
        print("Sorry thats not enough money. Money refunded")
    else:
        resources["water"] -= MENU["latte"]["ingredients"]["water"]
        resources["milk"] -= MENU["latte"]["ingredients"]["milk"]
        resources["coffee"] -= MENU["latte"]["ingredients"]["coffee"]
        print(f"Purchase successful! Here is your change: ${money_in - MENU["latte"]["cost"]:.2f}")
        money["value"] += MENU["latte"]["cost"]
        money_in = 0.0
        print("Enjoy your Latte!")

def print_cappuccino():
    global money_in
    print(f"Cappuccino costs ${MENU["cappuccino"]["cost"]} Please insert coins.")
    calc_coins()
    if(MENU["cappuccino"]["ingredients"]["water"] > resources["water"]):
        print("Sorry, not enough water in the machine.")
        return
    if(MENU["cappuccino"]["ingredients"]["milk"] > resources["milk"]):
        print("Sorry, not enough milk in the machine.")
        return
    if(MENU["cappuccino"]["ingredients"]["coffee"] > resources["coffee"]):
        print("Sorry, not enough coffee in the machine.")
        return
    if(money_in < MENU["cappuccino"]["cost"]):
        print("Sorry thats not enough money. Money refunded")
    else:
        resources["water"] -= MENU["cappuccino"]["ingredients"]["water"]
        resources["milk"] -= MENU["cappuccino"]["ingredients"]["milk"]
        resources["coffee"] -= MENU["cappuccino"]["ingredients"]["coffee"]       
        print(f"Purchase successful! Here is your change: ${money_in - MENU["cappuccino"]["cost"]:.2f}")
        money["value"] += MENU["cappuccino"]["cost"]
        money_in = 0.0
        print("Enjoy your Cappuccino!")

while(not machine_off):
    user_input = input("What would you like? Options: 'espresso' 'latte' 'cappuccino': ")
    if(user_input == 'report'):
        print_report()
    if(user_input == 'espresso'):
        print_espresso()
    if(user_input == 'latte'):
        print_latte()
    if(user_input == 'cappuccino'):
        print_cappuccino()
    if(user_input == 'refill'):
        refill_resources()
    if(user_input == 'off'):
        machine_off = True