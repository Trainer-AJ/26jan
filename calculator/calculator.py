# calculator.py
def main():
    print("Welcome to the terminal calculator!")
    print("Type 'q' to quit.")
    
    while True:
        expression = input("Enter calculation (e.g., 2 + 2): ")
        
        if expression.lower() == 'q':
            print("Exiting calculator. Goodbye!")
            break
        
        try:
            result = eval(expression)
            print(f"Result: {result}")
        except Exception as e:
            print(f"Error: {e}")
            print("Please try again.")

if __name__ == "__main__":
    main()
