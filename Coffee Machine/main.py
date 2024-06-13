from menu import MENU, stock, profit


def money_counter(quarts, dimes, nicks, pennies):
    """This will take in number of coins each and return the total money"""
    total_money = (quarts * 0.25) + (dimes * 0.1) + (nicks * 0.05) + (pennies * 0.01)
    return round(total_money, 2)


def check_res(drink_ing_list):
    """ Returns True if the drink ingredients are available in the resources and False if not."""
    for item in drink_ing_list:
        if drink_ing_list[item] > stock[item]:
            print(f"Sorry there's not enough {item}!")
            return False
        return True


def make_coffee(drink, drink_items):
    """Returns the drink made statement and updates the ingredients in the resources."""
    for item in drink_items:
        stock[item] -= drink_items[item]

    print(f"Here is your {drink}. ☕ Enjoy!")


def calc_change(money, drink_cost):
    """ This function will take the money given and check the difference to return the change."""
    diff = round((money - drink_cost), 2)
    if drink_cost < money:
        print(f"$ {money}")
        if diff > 0:
            print(f"Here is ${diff} dollars in change.")
            return True
    else:
        print("Sorry, that's not enough money! Money refunded. ")
        return False


machine_state = "on"

while machine_state == "on":
    # TODO 1 : Prompt user
    user_input = input("What would you like? (espresso/latte/cappuccino): ").lower()
    # TEST print(user_input)
    # TODO 2 : Turn off the coffee machine
    if user_input == "off":
        machine_state = "off"
    # TODO 3 : Print Report
    elif user_input == "report":
        print(f'Water: {stock["water"]}')
        print(f'Milk: {stock["milk"]}')
        print(f'Coffee: {stock["coffee"]}')
        print(f'Money: ${profit}')
    else:
        # TODO 4 : Check resources
        sufficient_ing = check_res(MENU[user_input]["ingredients"])
        if sufficient_ing:
            # TODO 5 : Process coins
            coins_quart = int(input("Please insert coins. \nHow many quarters? "))
            coins_dimes = int(input("How many dimes? "))
            coins_nicks = int(input("How many nickels? "))
            coins_pens = int(input("How many pennies? "))

            money_given = money_counter(coins_quart, coins_dimes, coins_nicks, coins_pens)
            # TODO 6 : Check transaction successful
            if calc_change(money_given, MENU[user_input]["cost"]):
                # TODO 7 : Make Coffee
                make_coffee(user_input, MENU[user_input]["ingredients"])
                profit += MENU[user_input]["cost"]
