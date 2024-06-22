def main():
    # Gets user inputs for income, state rate, and pre-tax deductions.
    money = input("What is your monthly (gross/before pretax deductions) income?\n")
    state_percent = input("What is your states income tax percent?\n")
    pretax = input("What is your monthly deductions total(401k, life insurance, dental insurance, etc.)\n")
    # Input validation
    while True:
        if not (money.isnumeric()):
            money = input("Invalid income. Please input a number and nothing else (Example: 100000) \n")
        if not (pretax.isnumeric()):
            pretax = input("Invalid pretax total. Please input a number and nothing else (Example: 100000) \n")
        if not (state_percent.isnumeric()) and isinstance(state_percent, float) is False or 0.50 > float(
                state_percent) > 100.00:
            state_percent = input("Invalid state tax. Please input a plain number between 1-100. (Example: 69) \n")
        else:
            break
    # Variables for numbers and math
    gross = int(money)
    net = int(money) - int(pretax)
    if net > 13500:
        fed = income_tax(net - 13500)
    else:
        fed = 0
    state = state_tax(net, float(state_percent))
    medi = medicare(gross)
    social_sec = social_security(gross)

    # Final calculations
    total_taxes = (fed + state) + (medi + social_sec)
    net = net - total_taxes

    # Prints your tax info
    print("Calculations done!"
          + f"\n Federal:{fed:.2f}"
          + f"\n State:{state:.2f}"
          + f"\n Medicare:{medi:.2f}"
          + f"\n Social Security:{social_sec:.2f}"
          + f"\nFor the month you will pay {total_taxes:.2f} in taxes and deductions."
          + f"\nYour net pay(before after tax deductions) is {net:.2f}.")


# Calculates federal tax
def income_tax(money):
    tax = 0
    # Gets federal tax numbers for different brackets
    tax_bracket_nums = {
        "b1": 11000,
        "b2": 44725,
        "b3": 95375,
        "b4": 182100,
        "b5": 231250,
        "b6": 578125,
        "b7": 100000000
    }
    tax_bracket_percents = {
        "b1": 10,
        "b2": 12,
        "b3": 22,
        "b4": 24,
        "b5": 32,
        "b6": 35,
        "b7": 37
    }
    if money < 11000:
        tax = money * 0.10
    else:
        for x in tax_bracket_percents:
            # Gets the current loop of the tax numbers
            percent = int(tax_bracket_percents[x])
            taxable = int(tax_bracket_nums[x])
            # If it is on the last index of the two value dictionaries, It just give a flat tax rate.
            if x == 6:
                tax = tax + (money * (percent / 100))
                break
            # If you arent making massive amounts of money, it will loop until money is greater
            # than taxable. At this point it calculates tax by taking taxable and taking out the 
            # correct percent. If it is less than taxable, it takes a percent from your total.
            if money > taxable:
                tax = tax + (taxable * (percent / 100))
                money = money - taxable
            elif money < taxable:
                tax = tax + (money * (percent / 100))
                break
    return int(tax)


# Calculates state tax
def state_tax(money, state_percent):
    return money * (state_percent / 100)


# Calculates medicare
def medicare(money):
    return money * (1.45 / 100)


# Calculates social security
def social_security(money):
    return money * (6.2 / 100)


if __name__ == "__main__":
    main()
