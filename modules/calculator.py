from controllers.controller import add_numbers


class Calculator:

    def __init__(self, first_number, second_number, sum):
        self.first_number = first_number
        self.second_number = second_number
        self.sum = sum

    def add_numbers(self, num1, num2):
        return num1 + num2

    def subtract_numbers(self, num1, num2):
        return num1 - num2
        
    def multiply_numbers(self, num1, num2):
        return num1 * num2

    def divide_numbers(self, num1, num2):
        return num1 / num2