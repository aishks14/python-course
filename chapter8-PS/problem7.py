# WAP in python to convert inches to cms using function
print("\nInches to Centimeters:")
print("----------------------")
def inches_to_centimeters(unit):
    return unit * 2.54

inch = float(input("Enter the unit value in Inch scale:"))
unit_conversion = inches_to_centimeters(inch)
print(f"Units in Centimeter scale: {round(unit_conversion, 2)}cm")