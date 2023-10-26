import re

def operator_choice(num1, num2):
    """
    Perform the chosen arithmetic operation on two numbers.

    Parameters:
    - num1 (int): The first number.
    - num2 (int): The second number.

    Returns:
    - str: A string representing the result of the operation.
    """
    valid_operators = r'[+\-*/]'
    
    while True:
        choice = input("Enter arithmetic operator (+, -, *, /): ")
        
        if re.match(valid_operators, choice):
            break
        else:
            print("Invalid operator. Please enter a valid operator.")

    try:
        if choice == "+":
            result = addition(num1, num2)
            return f"Your sum is: {result}"
        elif choice == "-":
            result = subtraction(num1, num2)
            return f"Your difference is: {result}"
        elif choice == "/":
            if num2 == 0:
                raise ZeroDivisionError("Error: Division by zero is not allowed.")
            result = division(num1, num2)
            return f"Your quotient is: {result}"
        else:
            result = multiplication(num1, num2)
            return f"Your product is: {result}"
    except Exception as e:
        return f"An error occurred: {e}"

def addition(num_1, num_2):
    """
    Add two numbers.

    Parameters:
    - num_1 (int): The first number.
    - num_2 (int): The second number.

    Returns:
    - int: The sum of the two numbers.
    """
    return num_1 + num_2

def subtraction(num_1, num_2):
    """
    Subtract the second number from the first.

    Parameters:
    - num_1 (int): The first number.
    - num_2 (int): The second number.

    Returns:
    - int: The difference of the two numbers.
    """
    return num_1 - num_2

def multiplication(num_1, num_2):
    """
    Multiply two numbers.

    Parameters:
    - num_1 (int): The first number.
    - num_2 (int): The second number.

    Returns:
    - int: The product of the two numbers.
    """
    return num_1 * num_2

def division(num_1, num_2):
    """
    Divide the first number by the second.

    Parameters:
    - num_1 (int): The numerator.
    - num_2 (int): The denominator.

    Returns:
    - float or None: The quotient of the division, or None if division by zero.
    """
    return num_1 / num_2 if num_2 != 0 else None

def get_number_input(prompt):
    """
    Get a valid integer input from the user.

    Parameters:
    - prompt (str): The prompt to display to the user.

    Returns:
    - int: The valid integer input from the user.
    """
    while True:
        number = input(prompt)
        if number.isdigit():
            return int(number)
        else:
            print("Invalid input. Please enter a valid integer.")
            
def print_in_asterisks(word):
    """
    Print each character of a word in caps and a space in between.

    Parameters:
    - word (str): The word to print.

    Returns:
    - None
    """
    for char in word.upper(): 
        print(char, end=" ")
    print()  

def main():
    """
    Main function to execute the simple calculator program.
    """
    word_to_print ="CODSOFT SIMPLE CALCULATOR"
    print_in_asterisks(word_to_print)
 
    
    try:
        first_number = get_number_input("Enter the first number: ")
        second_number = get_number_input("Enter the second number: ")
        print(operator_choice(first_number, second_number))
    except ValueError as ve:
        print(f"Input error: {ve}")

if __name__ == "__main__":
    main()
