
unit = input("Is this tempurature in Celsius, Fahrenheit, Kelvin (C/F/K):").lower()
temp = float(input("Enter the temperature: "))

if unit == "c":
    ntemp = round((9 * temp) / 5 + 32, 2)
    print(f"The temperature in Fahrenheit is: {ntemp}°F")
    ntemp = round(temp + 273.15 , 2)
    print(f"The temperature in Kelvin is: {ntemp}°K")
elif unit == "f":
    ntemp = round((temp - 32) * 5 / 9, 2)
    print(f"The temperature in Celsius is: {ntemp}°C")
    ntemp = round((temp - 32) * 5/9 + 273.15, 2)
    print(f"The temperature in Kelvin is: {ntemp}°K")
elif unit == "k":
    ntemp = round(temp - 273.15 , 2)
    print(f"The temperature in Celsius is: {ntemp}°C")
    ntemp = round((temp - 273.15) * 9/5 + 32, 2)
    print(f"The temperature in Fahrenheit is: {ntemp}°F")
else:
    print(f"{unit} is an invalid unit of measurement")