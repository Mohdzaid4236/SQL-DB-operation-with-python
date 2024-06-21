def generate_fibonacci(n):
    if n <= 0:
        return "Please enter a positive integer."
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    
    fibonacci_sequence = [0, 1]
    for i in range(2, n):
        next_term = fibonacci_sequence[i - 1] + fibonacci_sequence[i - 2]
        fibonacci_sequence.append(next_term)
    
    return fibonacci_sequence

def main():
    try:
        n = int(input("Enter the number of terms: "))
        if n <= 0:
            print("Please enter a positive integer.")
            return
    except ValueError:
        print("Please enter a valid integer.")
        return
    
    fibonacci_sequence = generate_fibonacci(n)
    print("Fibonacci sequence up to", n, "terms:")
    print(fibonacci_sequence)

if __name__ == "__main__":
    main()
