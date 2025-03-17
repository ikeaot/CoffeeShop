import random as rd
import time as t

day = 2
attempts = 1

# INVENTORY
if day == 2:
    coffeebean = 25
    water = 10
    milk = 15
    coins = 5

# MIMI'S DELAYED MESSAGES
def msg(string):
    print(string)
    t.sleep(2.5)

def tutorial():
    # NEEDED VARIABLE
    global coffeebean
    global water
    global milk
    global coins

    msg("(😃) Mimi: Welcome to Mimi's Tutorial!")
    msg("(😆) Mimi: Here you can try make a drink yourself!")
    msg("(😁) Mimi: Let's Start! \n")

    # START THE LOOPED TUTORIAL
    while True:
        td = ["Timeless Mimipresso", "Hawkkt Americawrr", "Magical Milky Mimi"]
        td_auto = rd.choice(td)


        # ORDER TRIAL
        msg(f"(🥸) Mimi: I want a {td_auto}!")
        msg(f"(😉) Mimi: If Mimi's Customer says this, you should take it!")
        print("Hint: Type (Y) \n")
        t.sleep(1)

        ans_t = input("(Y/N): ").lower()

        # ORDER TRIAL
        if ans_t == 'y':
            if td_auto == "Timeless Mimipresso":
                msg(f"(😋) Mimi: Now, to make a {td_auto}, you need to add..")
                msg("(😆) Mimi: 3 grams of Coffee Beans")
                msg("(😄) Mimi: With no water")
                msg("(😉) Mimi: And no milk!")
                msg("(😁) Mimi: Try it!")
            elif td_auto == "Hawkkt Americawrr":
                msg(f"(😋) Mimi: Now, to make a {td_auto}, you need to add..")
                msg("(😆) Mimi: 2 grams of Coffee Beans")
                msg("(😄) Mimi: With an Oz of water")
                msg("(😉) Mimi: And no milk!")
                msg("(😁) Mimi: Try it!")
            else:
                msg(f"(😋) Mimi: Now, to make a {td_auto}, you need to add..")
                msg("(😆) Mimi: a gram of Coffee Beans")
                msg("(😄) Mimi: With no water")
                msg("(😉) Mimi: And 2 Oz of milk!")
                msg("(😁) Mimi: Try it!")
            
            while True:
                try:
                    p = int(input("Coffee Bean(s): "))
                    q = int(input("Water: "))
                    r = int(input("Milk: "))
                except ValueError:
                    msg("(🫢) Mimi: Mimi Forgot to Mention That You Need Valid Numbers!")
                    msg("(😰) Mimi: Mimi Really Need To Leave a Note")
                    continue
        
                if td_auto == "Timeless Mimipresso" and p == 3 and q == 0 and r == 0:
                    msg("(😆) Mimi: You're a Natural!")
                    break
                elif td_auto == "Hawkkt Americawrr" and p == 2 and q == 1 and r == 0:
                    msg("(😋) Mimi: That's The Spirit!")
                    break
                elif td_auto == "Magical Milky Mimi" and p == 1 and q == 0 and r == 2:
                    msg("(😃) Mimi: You're Getting a Hang of It!")
                    break
                else:
                    msg("(🤨) Mimi: That's not quite right.. Try Again!")
                    continue
        elif ans_t == 'n':
            msg("(😐) Mimi: That's Not How You Respond to Mimi's Customer..")
        else:
            msg("(🤔) Mimi: Huh? It's not on Mimi's Dicitonary..")

        # CONPLETION
        msg("(😆) Mimi: You've completed your order!")
        
        
        while True:
            msg("(😉) Mimi: Do you want to try again?")
            t.sleep(1)
            ans_t2 = input("(Y/N): ").lower()

            if ans_t2 == 'y':
                msg("(🥸) Mimi: Okay! Mimi's Ready!")
                break
            elif ans_t2 == 'n':
                msg("(😄) Mimi: Okay!")
                return
            else:
                msg("(😖) Mimi: Mimi Really Doens't Understand!")

def gameplay():
    # VARIABLE
    global day
    global attempts
    global coffeebean
    global water
    global milk
    global coins
    global exit
    
    # INTRO
    if day == 1:
        msg("(😄) Mimi: Let's Get You Started Bartender!")
        msg("(🤔) Mimi: Well You Need to Remember Mimi's Recipe Though..")
        msg("(☺️) Mimi: Oh well! Surely You Can Remember It Right!? \n")
        print("Mimi's Coffee Shop Recipes:")
        print("Timeless Mimipresso (Espresso): 3x Coffee Bean(s)")
        print("Hawkkt Americawrr (Americano) : 2x Coffee Bean(s) + 1x Water(s)")
        print("Magical Milky Mimi (Latte)    : 2x Coffee Bean(s) + 2x Milk(s) \n")
        t.sleep(5)

        while True:
            ans_g = input("(Y/N): ").lower()
            
            if ans_g == 'y':
                msg("(😄) Mimi: Okay! Each order Will Have a Limit Of 30 Second(s).")
                msg("(😆) Mimi: Clear It Before The Time is Up! \n")
                break
            elif ans_g == 'n':
                msg("(🫥) Mimi: Well.. Mimi Supposed You A First-Timer.. Take your Time. \n")
                print("Mimi's Coffee Shop Recipes:")
                print("Timeless Mimipresso (Espresso): 3x Coffee Bean(s)")
                print("Hawkkt Americawrr (Americano) : 2x Coffee Bean(s) + 1x Water(s)")
                print("Magical Milky Mimi (Latte)    : 2x Coffee Bean(s) + 2x Milk(s) \n")
                t.sleep(4)
            else:
                msg("(😒) Mimi: Give Mimi A Valid Response..")
        
    else:
        msg(f"\n(😄) Mimi: Alright it's Day-{day}! Just Do It As You Did on Day-1.")
        msg("(😃) Mimi: Each order Will Have a Limit Of 30 Second(s).")

    # OPTION TO PLAY THE TUTORIAL
    msg("(🤔) Mimi: Oh yeah! Do you want Mimi To Explain?")
    
    while True:
        ans_g2 = input("(Y/N): ").lower()

        if ans_g2 == 'y':
            tutorial()
            break
        elif ans_g2 == 'n':
            msg("(😉) Mimi: Okay!")
            break
        else:
            msg("(🤧) Mimi: Mimi swears Mimi Doesn't Understand!!")

    msg("(😆) Mimi: Mimi Wishes You Good Luck!")

    # ORDERS LOOP
    rn = 5 + (1 if day > 1 and day % 2 != 0 else 0)
    round = rn

    for i in range(rn):
        drinks = ["Timeless Mimipresso", "Hawkkt Americawrr", "Magical Milky Mimi"]
        qnt = rd.randint(1, 3)
        auto_order = rd.choice(drinks)

        print("\n = INVENTORY =")
        print(f"{coffeebean}x Coffee Bean (g)")
        print(f"{water}x Water (Oz)")
        print(f"{milk}x Milk (Oz) \n")
        print(f"Remaining Order(s) Today: {round} \n")
        t.sleep(3)

        if coffeebean <= -25 or water <= -25 or milk <= -25 or coins <= -50:
            # GAME OVER
            attempts += 1
            msg("\n GAME OVER!")
            print(f"Total Attempts: {attempts} \n")
            print("= Death Menu =")
            print("1. Retry")
            print("2. Exit")
            
            while True:
                ans_d = int(input("Choose Wisely: "))
                if ans_d == 1:
                    msg("(😓) Mimi: Let's Try Again..")
                    break
                elif ans_d == 2:
                    msg("(🥺) Mimi: Okay, Byebye..")
                    exit()
                else:
                    print("Try Again.")      

        elif coffeebean <= 0 or water <= 0 or milk <= 0:
            # BUY INSUFFICIENT INGREDIENTS
            msg("(😰) Mimi: Oh No! You're Ran Out Of ingredients.")
            msg("(🤕) Mimi: Let's Buy the missing Ingredient first..")
            for i in range(2):
                if coffeebean <= 0:
                    print("Missing Ingredient: Coffee Bean")
                    t.sleep(1)
                if water <= 0:
                    print("Missing Ingredient: Water")
                    t.sleep(1)
                if milk <= 0:
                    print("Missing Ingredient: Milk")
                    t.sleep(1)
                break

            # OPTION TO THE GROCERY SHOP
            while True:
                ans_g4 = input("To Grocery Shop? (Y/N) ")

                if ans_g4 == 'y':
                    msg("(😖) Mimi: Let's Quickly buy it! \n")
                    shop()
                    break
                elif ans_g4 == 'n':
                    msg("(😕) Mimi: If you're sure..")
                    break
                else:
                    msg("(😐) Mimi: Mimi Doesn't Understand.")
                return

        # ORDERS
        msg(f"Customer: Can I order {qnt}x {auto_order}?")
        t.sleep(1)

        ans_g1 = input("(Y/N): ").lower()

        if ans_g1 == 'y':
            st = t.monotonic() # START
            dr = 30  # COUNTDOWN DURATION (30 seconds)

            while True:
                # COUNTDOWN STARTS
                current_t = t.monotonic()
                elapsed_t = current_t - st

                if elapsed_t >= dr:
                    print("Time's Up!")
                    coins -= 2  # TIMEOUT PENALTY
                    break
                
                # INPUT INGREDIENTS
                try:
                    x = int(input("Coffee Bean(s): "))
                    y = int(input("Water: "))
                    z = int(input("Milk: "))
                    coffeebean -= x
                    water -= y
                    milk -= z
                except ValueError:
                    print("Mimi Left a Message To Use Valid Numbers.")
                    x = 0 
                    y = 0
                    z = 0
                    continue

                # CHECK
                if auto_order == "Timeless Mimipresso" and x == (3 * qnt) and y == 0 and z == 0:
                    coins += (8 * qnt)
                    msg("Customer: That's My Drink! Thanks!")
                    break
                elif auto_order == "Hawkkt Americawrr" and x == (2 * qnt) and y == qnt and z == 0:
                    coins += (7 * qnt)
                    msg("Customer: This is Magnificent!")
                    break
                elif auto_order == "Magical Milky Mimi" and x == qnt and y == 0 and z == (2 * qnt):
                    coins += (10 * qnt)
                    msg("Customer: Just The Right Amount!")
                    break
                else:
                    msg("Customer: That's Not My Order!!")
                    coins -= (qnt)  # INCORRECT ORDER PENALTY
                    break

        elif ans_g1 == 'n':
            msg("Customer: You're Mean! \n")
            coins -= 1  # DECLINING PENALTY

        else:
            msg("Customer: What.. \n")
            coins -= 1  # INVALID RESPONSE PENALTY

        # ROUND ENDED
        round -= 1
        print(f"Total Coins: {coins}")
        t.sleep(3)
        continue        

    # DAY ENDED
    day += 1
    t.sleep(2)
    print("It's The End Of The Day! \n")
    print("= REMAINING INGREDIENTS =")
    print(f"{coffeebean}x Coffee Bean (g)")
    print(f"{water}x Water (Oz)")
    print(f"{milk}x Milk (Oz) \n")
    print(f"Total Coins Today: {coins}")

    # CONTINUE
    while True:
        ans_g3 = input("Continue? (Y/N): ").lower()

        if ans_g3 == 'y':
            gameplay()
            break
        elif ans_g3 == 'n':
            menu()
            break
        else:
            print("(😒) Mimi: Mimi Doesn't Understand.")

def recipe():
    # SELF EXPLANATORY
    while True:
        print("Mimi's Coffee Shop Recipes:")
        print("Timeless Mimipresso (Espresso): 3x Coffee Bean(s)")
        print("Hawkkt Americawrr (Americano) : 2x Coffee Bean(s) + 1x Water(s)")
        print("Magical Milky Mimi (Latte)    : 2x Coffee Bean(s) + 2x Milk(s) \n")

        ans_r = input("Exit? (Y/N) ").lower()
        if ans_r == 'y':
            break
        elif ans_r == 'n':
            print("(😆) Mimi: Okay! Take Your Time! \n")
        else:
            print("(🤨) Mimi: What Do you Mean? \n")

    
def shop(): # CLEAR
    # VARIABLE
    global coins
    global coffeebean
    global water
    global milk

    # MENU
    while True:
        print("== Mimi's Grocery Shop ==")
        print(f"1. Coffee Bean(s)  // You Have {coffeebean} g.")
        print(f"2. Water           // You Have {water} Oz.")
        print(f"3. Milk            // You Have {milk} Oz.")
        print("4. Go Back \n")
        print(f"Total Coin(s): {coins}")

        ans_s = input("Choose Wisely (1-4): ")

        # INGREDIENT QUANTITY
        if ans_s == '1':
            qn =  int(input("How Much? "))
            pr = 2 * qn
            print(f"That'll be {pr} coin(s)! \n")
        elif ans_s == '2':
            qn =  int(input("How Much? "))
            pr = qn
            print(f"That'll be {pr} coin(s)! \n")
        elif ans_s == '3':
            qn =  int(input("How Much? "))
            pr = 3 * qn
            print(f"That'll be {pr} coin(s))! \n")
        elif ans_s == '4':
            print("Okay! See you Later Bartender! \n")
            return
        else:
            print("Mimi System Error!")
            shop()

        # PAYMENT
        while True:
            ans_s2 = input("Proceed With The Payment (Y/N): ").lower()

            if ans_s2 == 'y':
                if coins >= pr: # SUFFICIENT COINS
                    coins = coins - pr
                    if ans_s == '1':
                        coffeebean +qn
                    elif ans_s == '2':
                        water +qn
                    else:
                        milk +qn
                    print("Payment Has Succeded!")
                    print(f"Total Coins: {coins}")
                    break
                else: # INSUFFICIENT COINS
                    print("Insufficient Coins! Work a Day or Two!")
                    break
                    
            elif ans_s2 == 'n':
                print("Payment Canceled!")
                break
            
            else:
                print("Mimi System Error!")
            
            t.sleep(1)
        t.sleep(1)

    
def byebye_menu(): 
    # VARIABLE
    global attempts

    # EXIT MENU
    while True:
        print(f"Total Attempts: {attempts}")
        msg("(🥹) Mimi: Are You Sure to Leave Mimi's Coffee Shop?")
        ans_b = input("(Y/N): ").lower()
    
        if ans_b == 'n':
            msg("(☺️) Mimi: YAY! I knew you'd miss Mimi! \n")
            menu()
        elif ans_b == 'y':
            msg("(😔) Mimi: Okay, Byebye.. \n")
            break
        else:
            msg("(🤨) Mimi: Mimi Doesn't Understand! \n")

def menu():
    # VARIABLE
    global day
    global attempts
    global exit

    while True:
        # MENU APPEARANCE
        print("== Mimi's Coffee Shop ==")
        print(f"1. Play - (Day {day})")
        print("2. Mimi's Recipe(s)")
        print("3. Grocery Shop")
        print("4. Reset | Exit (.1/.2)")
        
        ans = input("Choose Wisely (1-4): ")

        # SELF EXPLANATORY
        if ans == '1':
            gameplay()
        elif ans == '2':
            recipe()
        elif ans == '3':
            shop()
        elif ans == '4':
            byebye_menu()
            break
        elif ans == '4.1':
            msg("(☺️) Mimi: YAY! I knew you'd miss Mimi! Let's Start Again! \n")
            day = 1
            attempts += 1
            menu()
        elif ans == '4.2':
            print("(🥺) Mimi: Okay, Byebye..")
            exit()
        else:
            msg("(😤) Mimi: Mimi Doesn't Understand! \n")
    
# RETURN TO MENU
if __name__ == "__main__":
    menu()
