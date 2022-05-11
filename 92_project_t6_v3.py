from appJar import gui #imports the gui library from appJar

#Function to greet the user and ask for a category
cart = ""
total = 0.0
import pandas
coffee_df = pandas.read_csv("teamDB.csv")
coffee_list = list(coffee_df.Coffee)
cold_list = list(coffee_df.ColdDrinks)
food_list = list(coffee_df.Food)
acc_list = list(coffee_df.Accessories)

def greet_user(greeting, sentinel, categoryq, readyq):
    """Function to greet user"""
    canswer = ' '
    ranswer = sentinel
    print(greeting)
    while ranswer == sentinel:
        canswer = input(categoryq)
        ranswer = input(readyq)
    if canswer == "Coffee":
        coffee("Welcome to our Coffee section! Here are your choices:", coffee_list, "Which coffee would you like or enter None? ")
    elif canswer == "Cold Drinks":
        cold("Welcome to our Cold Drinks section! Here are your choices:", cold_list, "Which cold drink would you like or enter None? ")
    elif canswer == "Food":
        food("Welcome to our Food section! Here are your choices:", food_list, "Which food would you like or enter None? ")
    elif canswer == "Accessories":
        acc("Welcome to our Accessories section! Here are your choices:", acc_list, "Which accessory would you like or enter None? ")
    else:
        print("Sorry, we do not carry that category. See you next time!")

def coffee(greeting, selection, pickq):
    """Function to ask user to pick Coffee"""
    print(greeting)
    for item in selection:
        print(item)
    coffeepick = input(pickq)
    if coffeepick == "None":
        print("Goodbye")
    elif coffeepick == "Cold brew":
        closing("Cold brew", 5.25, "Enjoy your Cold brew!")
    elif coffeepick == "Macchiato":
        closing("Macchiato", 2.55, "Enjoy your Macchiato!")
    elif coffeepick == "Cappuccino":
        closing("Cappuccino", 4.25, "Enjoy your Cappuccino!")
    elif coffeepick == "Latte":
        closing("Latte", 3.35, "Enjoy your Latte!")
    else:
        closing("Americano", 3.65, "Enjoy your Americano!")

def cold(greeting, selection, pickq):
    """Function to ask user to pick Cold Drinks"""
    print(greeting)
    for item in selection:
        print(item)
    coldpick = input(pickq)
    if coldpick == "None":
        print("Goodbye")
    elif coldpick == "Strawberry Lemonade":
        closing("Strawberry Lemonade", 1.14, "Enjoy your Strawberry Lemonade!")
    elif coldpick == "Kiwi Lemonade":
        closing("Kiwi Lemonade", 2.19, "Enjoy your Kiwi Lemonade!")
    elif coldpick == "Mango Lemonade":
        closing("Mango Lemonade", 1.20, "Enjoy your Mango Lemonade!")
    elif coldpick == "Iced Tea":
        closing("Iced Tea", 3.69, "Enjoy your Iced Tea!")
    else:
        closing("Orange Juice", 1.63, "Enjoy your Orange Juice!")

def food(greeting, selection, pickq):
    """Function to ask user to pick Food"""
    print(greeting)
    for item in selection:
        print(item)
    foodpick = input(pickq)
    if foodpick == "None":
        print("Goodbye")
    elif foodpick == "Croissant":
        closing("Croissant", 2.45, "Enjoy your Croissant!")
    elif foodpick == "Bagel":
        closing("Bagel", 1.25, "Enjoy your Bagel!")
    elif foodpick == "Donut":
        closing("Donut", 0.99, "Enjoy your Donut!")
    elif foodpick == "Muffin":
        closing("Muffin", 1.69, "Enjoy your Muffin!")
    else:
        closing("Cookie", 1.95, "Enjoy your Cookie!")

def acc(greeting, selection, pickq):
    """Function to ask user to pick Accessories"""
    print(greeting)
    for item in selection:
        print(item)
    accpick = input(pickq)
    if accpick == "None":
        print("Goodbye")
    elif accpick == "Tumblers":
        closing("Tumblers", 45, "Thank you for purchasing Tumblers!")
    elif accpick == "Mugs":
        closing("Mugs", 29, "Thank you for purchasing Mugs!")
    elif accpick == "Cold cups":
        closing("Cold cups", 16, "Thank you for purchasing Cold Cups!")
    elif accpick == "Gift cards":
        closing("Gift cards", 25, "Thank you for purchasing Gift Cards!")
    else:
        closing("Shirts", 6, "Thank you for purchasing Shirts!")

def closing(pickeditem, price, goodbye):
    """Function to give user total price of purchase"""
    global cart
    cart = cart + pickeditem + ", "
    print(f"Your cart contains: {cart}")
    print(f"Your cost for the {pickeditem} is ${price}")
    global total
    total += price
    print(f"Your total is ${total:.2f}")
    more = input("Would you like to pick another item (y/n)? ")
    if more == "y":
        greet_user("Great!", "n", "What category would you like to browse (Coffee, Cold Drinks, Food, Accessories)? ", "Ready to browse (y/n)? ")
    else:
        for l in goodbye:
            print(l)

def press(btn):
    if btn == "Exit":
        app.stop()
    elif btn == "Greeting":
        greet_user("Welcome to our store", "n", "What category would you like to browse (Coffee, Cold Drinks, Food, Accessories)? ", "Ready to browse (y/n)? ")
    elif btn == "Coffee":
        coffee("Welcome to our Coffee section! Here are your choices:", coffee_list, "Which coffee would you like or enter None? ")
    elif btn == "Cold Drinks":
        cold("Welcome to our Cold Drinks section!  Here are your choices:", cold_list, "Which cold drink would you like or enter None? ")
    elif btn == "Food":
        food("Welcome to our Food section!  Here are your choices:", food_list, "Which food would you like or enter None? ")
    elif btn == "Accessories":
        acc("Welcome to our Accessories section!  Here are your choices:", acc_list, "Which accessories would you like or enter None? ")
    else:
        print('Pick a valid option')

#GUI
app=gui("Main Menu", "500x800")
app.addLabel("title", "Welcome to Team 6's Main Menu")
app.setLabelBg("title", "white")
#gif
app.addImage("decor", "c.gif")
app.setFont(30)
#buttons
app.addButton("Greeting", press)
app.addButton("Coffee", press)
app.addButton("Cold Drinks", press)
app.addButton("Food", press)
app.addButton("Accessories", press)
app.addButton("Exit", press)
app.go() #displays GUI