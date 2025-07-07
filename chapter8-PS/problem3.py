# WAP in python to connvert Fahrenheit to Celsius using a function
print("\nFahrenheit to Celsius temperature conversion:")
print("---------------------------------------------")
def fahrenheit_to_celsius(temp):
    celsius = 5*(temp-32)/9
    return celsius

fahrenheit = float(input("Enter the temperature value in Fahrenheit scale:"))
temp_conversion = fahrenheit_to_celsius(fahrenheit)
print(f"Temperature in Celsius scale is: {round(temp_conversion, 2)}°C")