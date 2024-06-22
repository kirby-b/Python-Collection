def main(fed, state, medi, social_sec):

    total_taxes = (fed + state) + (medi + social_sec)

    return f"{total_taxes:.2f}"


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
