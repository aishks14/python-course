# WAP in python to convert cms to inch using function
print("\nCentimeters to Inches:")
print("----------------------")
def centimeters_to_inches(unit):
    return unit/2.54

centimeter = float(input("Enter the unit value in Centimeter scale:"))
unit_conversion = centimeters_to_inches(centimeter)
print(f"Units in Inch scale: {round(unit_conversion, 2)}\"")