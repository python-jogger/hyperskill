class CoffeeMachine:
    def __init__(self):
        self.counter = True
        self.actual_amount_water = 400
        self.actual_amount_milk = 540
        self.actual_amount_beans = 120
        self.actual_amount_cups = 9
        self.actual_amount_money = 550
        self.espresso_water = 250
        self.espresso_beans = 16
        self.espresso_cups = 1
        self.espresso_cost = 4
        self.latte_water = 350
        self.latte_milk = 75
        self.latte_beans = 20
        self.latte_cups = 1
        self.latte_cost = 7
        self.cappuccino_water = 200
        self.cappuccino_milk = 100
        self.cappuccino_beans = 12
        self.cappuccino_cups = 1
        self.cappuccino_cost = 6

    def drink_coffee(self):
        drink_var = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu: ")

        if drink_var == "1":
            return self.buy_espresso()
        elif drink_var == "2":
            return self.buy_latte()
        elif drink_var == "3":
            return self.buy_cappuccino()
        else:
            return self.func_choice()

    def buy_espresso(self):
        if self.actual_amount_water < self.espresso_water:
            print('Sorry, not enough water!')
            return self.func_choice()
        if self.actual_amount_beans < self.espresso_beans:
            print('Sorry, not enough beans!')
            return self.func_choice()
        if self.actual_amount_cups < self.espresso_cups:
            print('Sorry, not enough cups!')
            return self.func_choice()
        else:
            print('I have enough resources, making you a coffee!')
            self.actual_amount_water -= self.espresso_water
            self.actual_amount_beans -= self.espresso_beans
            self.actual_amount_cups -= self.espresso_cups
            self.actual_amount_money += self.espresso_cost
            print()
            return self.func_choice()

    def buy_latte(self):
        if self.actual_amount_water < self.latte_water:
            print('Sorry, not enough water!')
            return self.func_choice()
        if self.actual_amount_milk < self.latte_milk:
            print('Sorry, not enough milk!')
            return self.func_choice()
        if self.actual_amount_beans < self.latte_beans:
            print('Sorry, not enough beans!')
            return self.func_choice()
        if self.actual_amount_cups < self.latte_cups:
            print('Sorry, not enough cups!')
            return self.func_choice()
        else:
            print('I have enough resources, making you a coffee!')
            self.actual_amount_water -= self.latte_water
            self.actual_amount_milk -= self.latte_milk
            self.actual_amount_beans -= self.latte_beans
            self.actual_amount_cups -= self.latte_cups
            self.actual_amount_money += self.latte_cost
            print()
            return self.func_choice()

    def buy_cappuccino(self):
        if self.actual_amount_water < self.cappuccino_water:
            print('Sorry, not enough water!')
            return self.func_choice()
        if self.actual_amount_milk < self.cappuccino_milk:
            return self.func_choice()
        if self.actual_amount_beans < self.cappuccino_beans:
            print('Sorry, not enough beans!')
            return self.func_choice()
        if self.actual_amount_cups < self.cappuccino_cups:
            print('Sorry, not enough cups!')
            return self.func_choice()
        else:
            print('I have enough resources, making you a coffee!')
            self.actual_amount_water -= self.cappuccino_water
            self.actual_amount_water -= self.cappuccino_milk
            self.actual_amount_beans -= self.cappuccino_beans
            self.actual_amount_cups -= self.cappuccino_cups
            self.actual_amount_money += self.cappuccino_cost
            print()
            return self.func_choice()

    def return_func(self):
        return self.func_choice()

    def func_rem(self):
        print("The coffee machine has: ")
        print(self.actual_amount_water, "of water")
        print(self.actual_amount_milk, "of milk")
        print(self.actual_amount_beans, "of coffee beans")
        print(self.actual_amount_cups, "of disposable cups")
        print(self.actual_amount_money, "of money")
        print()
        return self.func_choice()

    def func_fill(self):
        new_water = int(input("Write how many ml of water do you want to add: "))
        new_milk = int(input("Write how many ml of milk do you want to add: "))
        new_beans = int(input("Write how many grams of coffee beans do you want to add: "))
        new_cups = int(input("Write how many disposable cups of coffee do you want to add: "))

        self.actual_amount_water += new_water
        self.actual_amount_milk += new_milk
        self.actual_amount_beans += new_beans
        self.actual_amount_cups += new_cups
        print()
        return self.func_choice()

    def func_take(self):
        print("I gave you ${}".format(self.actual_amount_money))
        self.actual_amount_money *= 0
        print()
        return self.func_choice()

    def func_choice(self):
        action_var = input("Write action (buy, fill, take, remaining, exit): ")
        for i in action_var:
            if action_var == "exit":
                break
            elif action_var == "buy":
                return self.drink_coffee()
            elif action_var == "fill":
                return self.func_fill()
            elif action_var == "take":
                return self.func_take()
            elif action_var == "remaining":
                return self.func_rem()
            else:
                return self.func_choice()


cm1 = CoffeeMachine()
cm1.func_choice()





