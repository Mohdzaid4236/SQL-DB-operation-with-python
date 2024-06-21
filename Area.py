def calculate_area(length, width):
    if length == width:
        return "This is a square!"
    else:
        return length * width

def main():
    try:
        length = float(input("Enter the length: "))
        width = float(input("Enter the width: "))
    except ValueError:
        print("Please enter valid numbers for length and width.")
        return

    result = calculate_area(length, width)
    print(result)

if __name__ == "__main__":
    main()
