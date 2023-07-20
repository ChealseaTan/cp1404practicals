def main():
    """Get user input for temperature conversion."""
    MENU = """C - Convert Celsius to Fahrenheit
    F - Convert Fahrenheit to Celsius
    Q - Quit"""
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            celsius = float(input("Celsius: "))
            fahrenheit = get_fahrenheit_from_celsius(celsius)
            print(f"Result: {fahrenheit:.2f} F")
        elif choice == "F":
            fahrenheit = float(input("Fahrenheit: "))
            celsius = get_celsius_from_fahrenheit(fahrenheit)
            print(f"Result: {celsius:.2f} C")
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")

def get_fahrenheit_from_celsius(celsius):
    """Convert Celsius to Fahrenheit."""
    fahrenheit = celsius * 9.0 / 5 + 32
    return fahrenheit
def get_celsius_from_fahrenheit(fahrenheit):
    """Convert Fahrenheit to Celsius."""
    celsius = 5 / 9 * (fahrenheit - 32)
    return celsius

main()



