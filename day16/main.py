from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

game_over = False
prog_menu = Menu()
prog_coffee_maker = CoffeeMaker()
prog_money_machine = MoneyMachine()
while(not game_over):
    user_input = input("What would you like? Options: 'espresso' 'latte' 'cappuccino': ")
    if(user_input == 'report'):
        prog_coffee_maker.report()
        prog_money_machine.report()
    if(user_input == 'espresso'):
        if(prog_coffee_maker.is_resource_sufficient(prog_menu.find_drink(user_input))):
            if(prog_money_machine.make_payment(prog_menu.find_drink("espresso").cost)):
                prog_coffee_maker.make_coffee(prog_menu.find_drink("espresso"))
    if(user_input == 'latte'):
        if(prog_coffee_maker.is_resource_sufficient(prog_menu.find_drink(user_input))):
            if(prog_money_machine.make_payment(prog_menu.find_drink("latte").cost)):
                prog_coffee_maker.make_coffee(prog_menu.find_drink("latte"))
    if(user_input == 'cappuccino'):
        if(prog_coffee_maker.is_resource_sufficient(prog_menu.find_drink(user_input))):
            if(prog_money_machine.make_payment(prog_menu.find_drink("cappuccino").cost)):
                prog_coffee_maker.make_coffee(prog_menu.find_drink("cappuccino"))
    if(user_input == 'off'):
        game_over = True


#A easier way this could have been done
'''
espresso = MenuItem("espresso", 50, 0, 18, 1.5)
latte = MenuItem("latte", 200, 150, 24, 2.5)
cappuccino = MenuItem("cappuccino", 250, 100, 24, 3.0)
    else:
        coffee_choice = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(espresso) and money_machine.make_payment(espresso.cost):
            coffee_maker.make_coffee(coffee_choice)
'''