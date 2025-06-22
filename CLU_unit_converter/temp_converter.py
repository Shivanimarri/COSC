import argparse

def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

def main():
    parser = argparse.ArgumentParser(
        description="Convert temperatures between Celsius and Fahrenheit"
    )
    
    parser.add_argument(
        "temperature", type=float, help="Temperature value to convert"
    )
    
    parser.add_argument(
        "--to", choices=["C", "F"], required=True,
        help="Convert to: 'C' for Celsius, 'F' for Fahrenheit"
    )
    
    args = parser.parse_args()
    
    temp = args.temperature
    target = args.to

    if target == "F":
        result = celsius_to_fahrenheit(temp)
        print(f"{temp}°C = {result:.2f}°F")
    else:
        result = fahrenheit_to_celsius(temp)
        print(f"{temp}°F = {result:.2f}°C")

if __name__ == "__main__":
    main()
