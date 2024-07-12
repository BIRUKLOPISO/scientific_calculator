import math

def scientific_calculator():
    print("Welcome to the Scientific Calculator!")
    
    while True:
        print("\nSelect an operation:")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)") 
        print("5. Square Root (√)")
        print("6. Exponent (^)")
        print("7. Logarithm (log)")
        print("8. Trigonometric Functions (sin, cos, tan)")
        print("9. Exit")
        
        choice = input("Enter your choice (1-9): ")
        
        if choice == '1':
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            print(f"Result: {num1 + num2}")
        
        elif choice == '2':
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            print(f"Result: {num1 - num2}")
        
        elif choice == '3':
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            print(f"Result: {num1 * num2}")
        
        elif choice == '4':
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            print(f"Result: {num1 / num2}")
        
        elif choice == '5':
            num = float(input("Enter the number: "))
            print(f"Result: {math.sqrt(num)}")
        
        elif choice == '6':
            base = float(input("Enter the base: "))
            exponent = float(input("Enter the exponent: "))
            print(f"Result: {base ** exponent}")
        
        elif choice == '7':
            num = float(input("Enter the number: "))
            print(f"Result: {math.log(num)}")
        
        elif choice == '8':
            num = float(input("Enter the number: "))
            print(f"Sine: {math.sin(num)}")
            print(f"Cosine: {math.cos(num)}")
            print(f"Tangent: {math.tan(num)}")
        
        elif choice == '9':
            print("Exiting the calculator...")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    scientific_calculator()