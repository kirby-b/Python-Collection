def main(): 
    money = input("What is your monthly (gross/before pretax deductions) income?\n")
    state_percent = input("What is your states income tax percent?\n")
    pretax = input("What is your monthly deductions total(401k, life insurance, dental insurance, etc.)\n")
    while(True):
        if !(money.isnumeric()):
            money = input("Invalid income. Please input a number and nothing else (Example: 100000) \n")
        if !(pretax.isnumeric()):
            pretax = input("Invalid pretax total. Please input a number and nothing else (Example: 100000) \n")
        if !(state_percent.isnumeric()) or 1 > int(state_percent) > 100 :
            state_percent = input("Invalid state tax. Please input a plain number between 1-100. (Example: 69) \n")
        else:
            break
    gross = money
    net = money - pretax
    fed = income_tax(net)
    state = state_tax(net , state_percent)
    
def income_tax(money):

def state_tax(money, state_percent):
    return money * (state_percent/100)

def medicare(money):

def social_security(money):

if __name__ == "__main__":
    main()
