def get_drinks(prompt):
    print("*************", 
      "Type 1 for Monster energy", 
      "Type 2 for coffee", 
      "Type 3 for espresso", 
      "*************", sep="\n")
    
    total_caffeine = 0
    name = ''
    while True:
        try:
            value = int(input(prompt))
        except ValueError:
            print("That is not a drink.  Please try again.")
            continue
        if value == 1:
            total_caffeine += 160
            name = 'Monster'
        elif value == 2:
            total_caffeine += 95
            name = 'coffee'
        elif value == 3:
            total_caffeine += 64
            name = 'espresso'
        return total_caffeine, name

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
    if amt > 0:
        total_mg = drink[0] * amt
        message = " which is" if amt == 1 else "s which is a total of"
        print(f"You've drank {amt} {drink[1]}{message} {total_mg}mg's of caffeine.")

    if total_mg < fda_total:
        print("You're under the daily recommended intake of caffeine. Great job!")
    else:
        print("You're over the daily recommended intake of caffeine.  Please consider drinking less caffeine.")

if __name__ == "__main__":
    drink = get_drinks("What drink(s) have you consumed so far? ")
    amt = get_amount("How many of those drinks have you had? ")
    main()

