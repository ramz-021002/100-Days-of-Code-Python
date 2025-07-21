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
}

def print_report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${resources['money']}")

def check_resources(coffee):
    for item in MENU[coffee]['ingredients']:
        if MENU[coffee]['ingredients'][item] >= resources[item]:
            print(f"Sorry there is not enough {item}")
            return False
        return True

def update_resources(coffee):
    global resources
    resources["water"] -= MENU[coffee]["ingredients"]["water"]
    resources["coffee"]  -= MENU[coffee]["ingredients"]["coffee"]
    if "milk" in MENU[coffee]["ingredients"]:
        resources["milk"] -= MENU[coffee]["ingredients"]["milk"]
    resources["money"] += MENU[coffee]["cost"]

def collect_coins(coffee):
    print("Insert the coins")
    total = int(input("How many quarters?: "))*0.25
    total += int(input("How many dimes?: "))*0.1
    total += int(input("How many nickles ?: "))*0.05
    total += int(input("How many pennies?: "))*0.01
    if total >= MENU[coffee]['cost']:
        print(f"Here is ${round(total - MENU[coffee]['cost'], 3)} in change")
        print(f"Here is your {coffee}. Enjoy!")
        update_resources(coffee)
    else:
        print("Sorry that's not enough money. Money refunded.")

def make_coffee(coffee):
    resources_available = check_resources(coffee)
    if resources_available:
        collect_coins(coffee)

def main():
    make_continue = True
    while make_continue:
        user_input = input(" What would you like? (espresso/latte/cappuccino): ").lower()
        if user_input == 'report':
            print_report()
        elif user_input == 'off':
            make_continue = False
            print("Machine is off")
        else:
            make_coffee(user_input)

resources["money"] = 0
main()