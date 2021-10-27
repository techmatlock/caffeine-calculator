print("*************")
print("Type 1 for Monster energy")
print("Type 2 for coffee")
print("Type 3 for espresso")
print("*************")

def get_drinks(prompt, drink_name=''):
    
    total_caffeine = 0
    while True:
        try:
            value = int(input(prompt))
        except ValueError:
            print("That is not a drink.  Please try again.")
            continue
        if value == 1:
            total_caffeine += 160
            drink_name = 'Monster'
        if value == 2:
            total_caffeine += 95
            drink_name = 'coffee'
        if value == 3:
            total_caffeine += 64
            drink_name = 'espresso'
        return total_caffeine, drink_name

def get_amount(prompt):
    while True:
        try:
            amt_drinks = int(input(prompt))
        except ValueError:
            print("That is not a valid input.  PLease try again")
            continue
        return amt_drinks

def main():
    fda_total = 400 # Recommended FDA daily intake of caffeine in milligrams (mg)
    if drink[0] * amt < fda_total:
        print("You're under the daily recommended intake of caffeine. Great job!")
    else:
        print("You're over the daily recommended intake of caffeine.  Please consider drinking less caffeine")

drink = get_drinks("What drink(s) have you consumed so far? ")
amt = get_amount("How many of those drinks have you had? ")
main()





