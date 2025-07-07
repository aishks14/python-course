# WAP in python to connvert Celsius to Fahrenheit using a function
print("\nCelsius to Fahrenheit temperature conversion:")
print("---------------------------------------------")
def celsius_to_fahrenheit(temp):
    fahrenheit = (temp * 9/5) + 32
    return fahrenheit

celsius = float(input("Enter the temperature value in Celsius scale:"))
temp_conversion = celsius_to_fahrenheit(celsius)
print(f"Temperature in Fahrenheit scale is: {round(temp_conversion, 2)}°F")