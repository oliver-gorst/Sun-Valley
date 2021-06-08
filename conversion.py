def meters_from(feet):
    """Convert feet to meters."""
    try:
        meters = float(feet) / 3.28
        meters = round(meters, 2)  # Round to three decimal places
        return str(meters)
    except ValueError:
        return "invalid input"

if __name__ == "__main__":
    feet = input("Enter Height in Feet: ")
    print("The height in meters is:", meters_from(feet))
