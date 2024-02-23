#Name: Samra Ahmed
#Email:  samraahmed3291@gmail.com
#Q :To create a calculator by python programmimg
# start from welcome to the calculator
print("Welcome to the Python Calculator!")

#defining main function

def calculator():
    
#main loop

    while True:
        print()
        print("Select an operation: \n1. Addition \n2. Subtraction \n3. Multiplication \n4. Division \n5. Exit")

#your_Choice
        print()
        your_choice = int(input("Enter your choice (1, 2, 3, 4, or 5): "))

        if your_choice == 5:
          
                print("Exiting the calculator. Goodbye!!")
                break
                
        else:

#for Operand limit

                   print()
                   print("Operand limit: 2")
            
#To create and take your input for operands
                   print()
                   num1 = float(input("Enter first number: "))
                   num2 = float(input("Enter second number: "))

#Result for Addition

        if your_choice == 1:
            addition = num1 + num2
            addition_result=round(addition_result, 3)
            print()
            print(f"addition= {addition_result}")

#for Subtraction

        elif your_choice == 2:
            subtraction_result = num1 - num2
            result=round(subtraction_result, 3)
            print()
            print(f"subtraction_result = {num1} - {num2} = {result}")

#for Multiplication

        elif your_choice == 3:
            multiplication= num1 * num2
            result=round(result, 3)
            print()
            print(f"Result = {num1} × {num2} = {result}")

#for division

        elif your_choice == 4:
            if num2 == 0:
                print("Error: Division by zero!")
            else:
                division_result = num1 / num2
                division_result=round(division_result, 3)
                print()
                print(f"Result = {num1} ÷ {num2} = {division_result}")

if __name__ == "__main__":
    calculator()


