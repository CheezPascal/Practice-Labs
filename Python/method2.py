class Calculator:
    def __init__(self):
        self.result = 0

    def add(self, num):
        self.result += num

    def subtract(self, num):
        self.result -= num

    def multiply(self, num):
        self.result *= num

    def divide(self, num):
        if num != 0:
            self.result /= num
        else:
            print("Error: Division by zero is not allowed.")

# Create an instance of the Calculator class
calc = Calculator()

# Use the methods to perform calculations
calc.add(5)
calc.subtract(2)
calc.multiply(3)
calc.divide(4)

# Print the final result
print("Result:", calc.result)