import pandas as pd
import all_material_class as material
import re

class Calculate :
    
    values_to_calculate : tuple

    def __init__(self, input_values, result) :
        self.input_values = input_values
        self.result = result
    
    def add(self) :
        input_values = self.input_values
        result = self.result
        sum_of_input_values = int(input_values[0])
        result = result + sum_of_input_values

        return result

    def subtract(self) :
        input_values = self.input_values
        result = self.result
        sum_of_input_values = sum(input_values)
        result = result - sum_of_input_values

        return result

    def product(self) :
        input_values = self.input_values
        result = self.result
        sum_of_input_values = sum(input_values)
        result = result * sum_of_input_values
        
        return result
    
    def divide(self) :
        input_values = self.input_values
        result = self.result
        sum_of_input_values = sum(input_values)
        result = result + sum_of_input_values

        return result


def split_text(text):
    pattern = r"\S*\([^)]*\)|\S+"
    matches = re.findall(pattern, text)
    return tuple(matches)

def input_values() :
    input_values = input()
    if input_values == "back" :
        return
    else :
        input_values = split_text(input_values)
    return input_values

def back_up_result(result) :
    previous_result = result
    return previous_result

def all_clear(result) :
    result = 0
    print("계산값 초기화")
    return result

def get_values_in_parentheses(text):
    pattern = r"\(([^)]+)\)"
    matches = re.findall(pattern, text)
    
    return tuple(tuple(match.split(', ')) for match in matches)[0]

result = 0
previous_result = result

while True :
    command = input("명령을 입력하세요 : [result = " + str(result) + "] ")

    if command == "add" :
        previous_result= back_up_result(result)
        do_command = Calculate(input_values(), result)
        result = do_command.add()

    elif command == "subtract" :
        previous_result= back_up_result(result)
        do_command = Calculate(input_values(), result)
        result = do_command.subtract()
    
    elif command == "product" :
        previous_result= back_up_result(result)
        do_command = Calculate(input_values(), result)
        result = do_command.product()
    
    elif command == "divde" :
        previous_result= back_up_result(result)
        do_command = Calculate(input_values(), result)
        result = do_command.divde()

    elif command == "clear" :
        previous_result= back_up_result(result)
        result = all_clear(result)

    elif command == "exit" :
        break

    elif command == "cancel" :
        result = previous_result




    

