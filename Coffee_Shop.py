#Template for our coffee shop with no UI/UX
class Main():
    def __init__(self):
        self.choice = {1: "Shop",2: "Inventory",3: "Order",4: "Payment"}
        self.show_options()
        self.select_options()

    #Shows the options to navigate on the app
    def show_options(self):
        for key, value in self.choice.items():
            print(f"{key}. {value}")

    #Allows the user to select from the options
    def select_options(self):
        try:
            option = int(input("Please select an option to navigate: (Enter the corresponding number) "))
            if option == 1:
                Shop() #This runs the shop class when user input equals 1
            elif option == 2:
                Inventory()
            elif option == 3:
                Order()
            elif option == 4:
                Payment()
            else: 
                print("Coming soon!") #Prints coming soon if othe than 1, as these classes are not made yet
        except ValueError:
            print("Invalid input. Please enter a number.")
            self.select_options()

class Shop():
    def __init__(self):
        self.drinks = {1: "Water $1.00",2: "Coffee $3.50",3: "Soda $2.00",4: "Other"}
        self.show_menu()
        self.select_drink()
    
    def show_menu(self):
        for key, value in self.drinks.items():
            print(f"{key}. {value}")

    def select_drink(self):
        try:
            drink = int(input("What would you like to drink? (Enter the number): "))
            if drink == 1:
                print("Options for Water:")
                print("1. Iced Water")
                print("2. Warm Water")
            elif drink == 2:
                print("Options for Coffee:")
                print("1. Iced Coffee")
                print("2. Hot Coffee")
                print("3. List of all available Coffee")
            elif drink == 3:
                print("Options for Soda:")
                print("1. List of all available sodas")
            elif drink == 4:
                my_drink = input("Please enter your preferred drink: ")
                print(f"You selected: {my_drink}")
            else:
                print("Invalid option. Please choose a number from the menu.")
                self.select_drink() 
        except ValueError:
            print("Invalid input. Please enter a number.")
            self.select_drink()

class Inventory():
    def __init__(self):
        self.prompt1 = "This will show the inventory when we get to it!"
        self.show_prompt1()

    def show_prompt1(self):
        print(self.prompt1)

class Order():
    def __init__(self):
        self.prompt2 = "This will show the Order for the user when it is ready!"
        self.show_prompt2()

    def show_prompt2(self):
        print(self.prompt2)

class Payment():
    def __init__(self):
        self.prompt3 = "This will show the payment options when it is ready!"
        self.show_prompt3()

    def show_prompt3(self):
        print(self.prompt3)


Main()
