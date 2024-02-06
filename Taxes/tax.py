class Tax:
    def main(): 
        #Gets user inputs for income, state rate, and pre tax deductions.
        money = input("What is your monthly (gross/before pretax deductions) income?\n")
        state_percent = input("What is your states income tax percent?\n")
        pretax = input("What is your monthly deductions total(401k, life insurance, dental insurance, etc.)\n")
        #Input validation
        while(True):
            if not(money.isnumeric()):
                money = input("Invalid income. Please input a number and nothing else (Example: 100000) \n")
            if not(pretax.isnumeric()):
                pretax = input("Invalid pretax total. Please input a number and nothing else (Example: 100000) \n")
            if not(state_percent.isnumeric()) and isinstance(state_percent, float) == False or 0.50 > float(state_percent) > 100.00 :
                state_percent = input("Invalid state tax. Please input a plain number between 1-100. (Example: 69) \n")
            else:
                break
        #Variables for numbers and math
        gross = int(money)
        net = int(money) - int(pretax)
        if net > 13500:
            fed = Tax.income_tax(net - 13500)
        else:
            fed = 0
        state = Tax.state_tax(net , float(state_percent))
        medi = Tax.medicare(gross)
        social_sec = Tax.social_security(gross)
    
        #Final calculations
        total_taxes = (fed + state) + (medi + social_sec)
        net = net - total_taxes

        #Prints your tax info
        print(f"Calculations done!\n Federal:{fed:.2f}\n State:{state:.2f}\n Medicare:{medi:.2f}\n Social Security:{social_sec:.2f}\nFor the month you will pay {total_taxes:.2f} in taxes and deductions. Your net pay(before after tax deductions) is {net:.2f}.")

    #Calculates federal tax
    def income_tax(money):
        #Gets federal tax numbers
        tax = 0
        tax_bracket_nums = {
            "b1": 11000,
            "b2": 44725,
            "b3": 95375,
            "b4": 182100,
            "b5": 231250,
            "b6": 578125
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
        if(money < 11000):
                tax = money * 0.10
        else:
            for x in tax_bracket_percents:
                percent = int(tax_bracket_percents[x])
                taxable = int(tax_bracket_nums[x])
                if x == 6:
                    tax = tax + (money * (percent / 100))
                    break
                if(money > taxable):
                    tax = tax + (taxable * (percent / 100))
                    money = money - taxable
                elif(money < taxable):
                    tax = tax + (money * (percent / 100))
                    break
        return int(tax)
    #Calculates state tax
    def state_tax(money, state_percent):
        return money * (state_percent / 100)
    
    #Calculates medicare
    def medicare(money):
        return money * (1.45 / 100)
    
    #Calculates social security
    def social_security(money):
        return money * (6.2 / 100)
    
if __name__ == "__main__":
    Tax.main()
