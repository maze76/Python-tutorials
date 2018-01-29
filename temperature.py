# chapter 5 temperature.py
# Convert Celsius and Fahrenheit temperatures using functions

def conversion_fahr(temp_celsius):
    """
    convert degrees celsius to fahrenheit according to given formula
    """

    fahrenheit = temp_celsius * (9 / 5) + 32
    fahrenheit = round(fahrenheit, 2)
    print(f"{temp_celsius} degrees celsius is equal to {fahrenheit} degrees fahrenheit.")

def conversion_celsius(temp_fahr):
    """
    convert degrees fahrenheit to celsius according to given formula
    """
    celsius = (temp_fahr - 32) * 5 / 9
    celsius = round(celsius, 2)
    print(f"{temp_fahr} degrees fahrenheit is equal to {celsius} degrees celsius.")

conversion_fahr(30)
conversion_celsius(84)
