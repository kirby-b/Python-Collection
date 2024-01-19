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
    gross = int(money)
    net = int(money) - int(pretax)
    fed = income_tax(net)
    state = state_tax(net , state_percent)
    medi = medicare(gross)
    social_sec = social_security(gross)
    
    total_taxes = (fed + state) + (medi + social_sec)
    net = net - total_taxes

    print("Calculations done!\n Federal:{fed:.2f}\n State:{state:.2f}\n Medicare:{medi:.2f}\n Social Security:{social_sec:.2f}\nFor the month you will pay {total_taxes:.2f} in taxes. Your net pay(before after tax deductions) is {net:.2f}.")

def income_tax(money: int):
    #Just have the user input the numbers need I guess

def state_tax(money: int, state_percent: int):
    return money * (state_percent/100)

def medicare(money: int):
    return money * (1.45 / 100)

def social_security(money: int):
    return money * (6.2 / 100)
    
if __name__ == "__main__":
    main()
