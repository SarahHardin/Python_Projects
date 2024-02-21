MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0,
}


on = True
def start_order():
    order = input("What would you like? (espresso/latte/cappuccino): ")

    if order == 'report':
        get_report()
    elif order == 'espresso' or order == 'latte' or order == 'cappuccino':
        get_resources = check_resources(order)
        if get_resources:
            payment = get_money(order)
            if payment:
                make_drink(order)
    else:
        print("We do not serve that.")


def get_report():
    print(f"Water: {resources['water']}ml \n"
          f"Milk: {resources['milk']}ml \n"
          f"Coffee: {resources['coffee']}g \n"
          f"Money: ${resources['money']}")


def check_resources(type):
    if type == 'espresso':
        if resources['water'] >= MENU[type]['ingredients']['water']:
            if resources['coffee'] >= MENU[type]['ingredients']['coffee']:
                return True
            else:
                print("Sorry there is not enough coffee.")
                return False
        else:
            print("sorry there is not enough water.")
            return False
    else:
        if resources['water'] >= MENU[type]['ingredients']['water']:
            if resources['coffee'] >= MENU[type]['ingredients']['coffee']:
                if resources['milk'] >= MENU[type]['ingredients']['milk']:
                    return True
                else:
                    print("Sorry there is not enough milk.")
                    return False
            else:
                print("Sorry there is not enough coffee.")
                return False
        else:
            print("sorry there is not enough water.")
            return False
    


def get_money(type):
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))

    total = (quarters*0.25) + (dimes*0.10) + (nickles*0.05) + (pennies*0.01)
    #print(f"You paid: {total} , needed: {MENU[type]['cost']}")
    if total >= MENU[type]['cost']:
        resources['money'] += MENU[type]['cost']
        change = total - MENU[type]['cost']
        if change != 0:
            print(f"Here is ${round(change,2)} in change.")
        return True
    elif total < MENU[type]['cost']:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_drink(type):
    if type == 'espresso':
        resources['water'] -= MENU['espresso']['ingredients']['water']
        resources['coffee'] -= MENU['espresso']['ingredients']['coffee']
    else:
        resources['water'] -= MENU[type]['ingredients']['water']
        resources['coffee'] -= MENU[type]['ingredients']['coffee']
        resources['milk'] -= MENU[type]['ingredients']['milk']
    print(f"Here is you {type} Enjoy!")


if __name__ == '__main__':
    while on:
        start_order()