
import re
from tkinter.messagebox import YES


def add(numbers):
    return sum(numbers)

def subtract(numbers):
    return numbers[0]-sum(numbers[1:])

def multiplication(numbers):
    result = 1
    for num in numbers:
        result *= num
    return result 

def division(numbers):
    result = numbers[0]
    for num in numbers[1:]:
        if num == 0:
            return "Error! Division by zero."
        result /= num
    return result



def calculator():
    while True:
        print("Select Operations:")
        print("1. Add")
        print("2. Substract")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")

        choice = input("Enter choice(1/2/3/4/5): ") 
        if choice == '5':
            print("Exit Calculator.") 
            break

        if choice in ['1','2','3','4','5']:
            numbers= input("Enter the number: ").split()
            numbers = [float(num) for num in numbers]

            if choice == '1':
                print(f"Result:{add(numbers)}")
        
            elif choice == '2':
                print(f"Result:{subtract(numbers)}")

            elif choice == '3':
                print(f"Result:{multiplication(numbers)}")
            
            elif choice == '4':
                print (f"Result:{division(numbers)}")

        else:
            print("Invalid input. Please enter a number between 1 and 5.")

        next_calculator = input("Do you want to perform another calculation ?(yes/no): ")
        if next_calculator !='yes':
            break
       
        

if __name__ == "__main__":
    calculator()    