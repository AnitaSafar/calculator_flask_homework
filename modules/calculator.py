class Calculator:

    def __init__(self, first_number, second_number, sum):
        self.first_number = first_number
        self.second_number = second_number
        self.sum = sum

    def add_numbers(self, num1, num2):
        return int(num1) + int(num2)

    def subtract_number(self, num1, num2):
        return int(num1) - int(num2)
        
    def multiply_number(self, num1, num2):
        return num1 * num2

    def divide_number(self, num1, num2):
        return num1 / num2