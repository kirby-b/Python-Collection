def main():
    temp = float(input("Enter the temperature: "))
    #Gets unit of temperature and its value. There was no reason to include kelvin, but I was bored.
    unit = input("Is this tempurature in Celsius, Fahrenheit, Kelvin (C/F/K):").lower()
    while unit not in ["celsius","c","fahrenheit","f","kelvin","k"]:
        unit = input("Please input a valid tempurature unit (Celsius, Fahrenheit, Kelvin, C, F, K:").lower()
    
def convert(unit, temp):
    if unit == "c":
        ntemp = round((9 * temp) / 5 + 32, 2)
        print(f"The temperature in Fahrenheit is: {ntemp}°F")
        ntemp = round(temp + 273.15 , 2)
        print(f"The temperature in Kelvin is: {ntemp}°K")
    #Prints what a temp in Celsius is in Kelvin and Fahrenheit
    elif unit == "f":
        ntemp = round((temp - 32) * 5 / 9, 2)
        print(f"The temperature in Celsius is: {ntemp}°C")
        ntemp = round((temp - 32) * 5/9 + 273.15, 2)
        print(f"The temperature in Kelvin is: {ntemp}°K")
        #Prints what a temp in Fahrenheit is in Celcius and kelvin
    elif unit == "k":
        ntemp = round(temp - 273.15 , 2)
        print(f"The temperature in Celsius is: {ntemp}°C")
        ntemp = round((temp - 273.15) * 9/5 + 32, 2)
        print(f"The temperature in Fahrenheit is: {ntemp}°F")
    #Prints what a temp in Kelvin is in Celsius and Fahrenheit
if __name__ == "__main__":
    main()
