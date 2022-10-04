class Product:
    def __init__(self, name: str, price: float):
        self.__name = name
        self.__price = price

    @property
    def name(self):
        return self.__name

    @property
    def price(self):
        return self.__price

    def __str__(self):
        return f"{self.__name} ({self.__price:.2f} EUR)"

class ShoppingList:
    def __init__(self):
        self.__shoppinglist = {}

    def add_product(self, name: str, price: float):
        self.__shoppinglist[name] = Product(name, price)                  

    def validate_name(self, name: str):
        if name != "":
            return True
        else:
            print(f"Error setting name: Name can't be empty. Try again!")
            return False

    def validate_price(self, price: float):
        if price >= 0:
            return True
        else:
            print(f"Error setting price: Price must be number 0 or higher. Try again!")
            return False

    def get_most_expensive(self):
        most_expensive = -1
        for name, item in self.__shoppinglist.items():
            if item.price > most_expensive:
                most_expensive = item.price
                most_expensive_item = item
        return most_expensive_item

    def get_least_expensive(self):
        least_expensive = -1
        for name, item in self.__shoppinglist.items():
            if least_expensive == -1:
                least_expensive = item.price
                least_expensive_item = item
            elif item.price < least_expensive:
                least_expensive = item.price
                least_expensive_item = item
        return least_expensive_item        

    def total_items(self):
        return len(self.__shoppinglist)

    def total_price(self):
        total = 0
        for name, item in self.__shoppinglist.items():
            total += item.price
        return total

    def print_shoppinglist(self):
        for name, item in self.__shoppinglist.items():
            temp_name = item.name
            if len(temp_name) > 10:
                temp_name = temp_name[:10]
            print(f"{temp_name:10} {item.price:>11.2f} EUR")
        print("-" * 26)
        print(f"Total: {self.total_items():<3} {self.total_price():>11.2f} EUR")

class Application:
    def __init__(self):
        self.__app = ShoppingList()

    def welcome(self):
        print()
        print("Welcome to this amazing Shopping List app by Anssi! (❁´◡`❁)")
        print("What would you like to do? Here are the commands:")
        print("1: Add item to the shopping list")
        print("2: Check the most expensive item on your shopping list")
        print("3: Check the least expensive item on your shopping list")
        print("4: Print your shopping list")
        print("0: Stop the app")

    def goodbye(self):
        print("Goodbye! Hope you had a blast.")

    def add_item(self):
        while True:
            name = input("Name: ")
            #Validate if name input is valid
            if self.__app.validate_name(name):
                break
        while True:
            #Validate if price input is valid
            try:
                price = float(input("Price: "))
                if self.__app.validate_price(price):
                    break
            except ValueError:
                print(f"ValueError when setting price: Price must be number. Try again!")     
        self.__app.add_product(name, price)

       
    def most_expensive(self):
        if self.__app.total_items() == 0:
            print("There is no items in your shopping list! :(")
        else:
            item = self.__app.get_most_expensive()
            print(f"The most expensive item: {item}")

    def least_expensive(self):
        if self.__app.total_items() == 0:
            print("There is no items in your shopping list! :(")
        else:
            item = self.__app.get_least_expensive()
            print(f"The least expensive item: {item}")

    def print_all(self):
        if self.__app.total_items() == 0:
            print("There is no items in your shopping list! :(")
        else:
            print()
            print("Here is your shopping list:")
            self.__app.print_shoppinglist()

    def invalid_command(self):
        print("Invalid command, try again!")

    def execute(self):
        self.welcome()
        while True:
            print()
            command = input("Command: ")
            if command == "0":
                self.goodbye()
                break
            elif command == "1":
                self.add_item()
            elif command == "2":
                self.most_expensive()
            elif command == "3":
                self.least_expensive()
            elif command == "4":
                self.print_all()
            else:
                self.invalid_command()


shopping = Application()
shopping.execute()


if __name__ == "__main__":
    pass