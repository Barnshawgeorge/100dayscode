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