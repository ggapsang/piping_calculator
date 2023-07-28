import pandas as pd
import re

### Material Classes ###
class Material:
    def __init__(self, material_data, size, sch='std', rating=None, joint_type='bw', degree=90, long_or_short='lr'):
        self.material_data = material_data
        self.size = float(size)
        self.sch = sch
        self.rating = rating
        self.joint_type = joint_type

    def get_outdia(self):
        raise NotImplementedError

    def get_india(self):
        raise NotImplementedError

    def get_thick(self):
        raise NotImplementedError
    
    def get_span(self) :
        pass

class Pipe(Material):
    def __init__(self, size, sch):
        super().__init__(None, size, sch)


class Elbow(Material):
    def __init__(self, material_data, size, sch='std', rating=None, joint_type='bw', degree=90, long_or_short='lr'):
        super().__init__(material_data, size, sch, rating, joint_type)
        self.name = 'elbow'
        self.degree = degree
        self.long_or_short = long_or_short

    def get_span(self) :
        name = self.name
        material_data = self.material_data
        size = float(self.size)
        joint_type = self.joint_type
        degree = self.degree
        long_or_short = self.long_or_short
        span = search_value_in_df(material_data, result_col='span', name=name, size=size, joint_type=joint_type, degree=degree, long_or_short=long_or_short)
        return span   


class Tee(Material):
    def __init__(self, material_data, size, subsize, sch='std', rating=None, joint_type='bw'):
        super().__init__(material_data, size, sch, rating, joint_type)
        self.name = 'tee'
        self.subsize = subsize


class Reducer(Material):
    def __init__(self, material_data, size, subsize, sch='std', rating=None, joint_type='bw'):
        super().__init__(material_data, size, sch, rating, joint_type)
        self.name = 'reducer'
        self.subsize = subsize


class Cap(Material):
    def __init__(self, material_data, size, sch='std', rating=None, joint_type='bw'):
        super().__init__(material_data, size, sch, rating, joint_type)
        self.name = 'cap'


class Flange(Material):
    def __init__(self, size, sch, flange_type, rating):
        super().__init__(None, size, sch, rating)
        self.flange_type = flange_type


class Valve(Material):
    def __init__(self, size, sch, valve_type, joint_type):
        super().__init__(None, size, sch, None, joint_type)
        self.valve_type = valve_type


class Coupling(Material):
    def __init__(self, size):
        super().__init__(None, size)

### Caculate class ###
class Calculate :
    
    values_to_calculate : tuple

    def __init__(self, tuple_for_sum, result) :
        self.tuple_for_sum = tuple_for_sum
        self.result = result
    
    def add(self) :
        tuple_for_sum = self.tuple_for_sum
        result = self.result
        sum_of_tuple = sum(tuple_for_sum)
        result = result + sum_of_tuple

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


## Functions to process command##
def search_value_in_df(material_data, result_col, **conditions) :
    condition_list = []

    for col, value in conditions.items() :
        condition = material_data[col] == value
        condition_list.append(condition)

    combined_condition = condition_list[0]
    for condition in condition_list[1:] :
        combined_condition &= condition

    filtered_data = material_data[combined_condition]

    if not filtered_data.empty : 
        return filtered_data.iloc[0][result_col]

    return 0

# input 값을 comma 기준으로 텍스트 나누어 튜플로 받는다. 단 "()"안의 값들은 분리되지 않음#
def input_values() :
    # comma 기준으로 텍스트 나누어 튜플로 받는다. 단 "()"안의 값들은 분리되지 않음#
    def split_text(text):
        pattern = r"\S*\([^)]*\)|\S+"
        matches = re.findall(pattern, text)
        return tuple(matches)
    input_values = input()
    input_values = split_text(input_values)
    return input_values

# 연산을 시작하기 전에 기존 result 값을 previous result 변수에 저장한다. cancel 명령어를 사용하기 위한 기본, 연산 시작 전에 필수로 넣는다 # 
def back_up_result(result) :
    previous_result = result
    return previous_result

# result 값을 0으로 초기화한다. previous result 값은 보존한다.
def all_clear(result) :
    result = 0
    print("계산값 초기화")
    return result

# 문자열에서 "()"안에 있는 텍스트를 comma를 기준으로 나누어 튜플로 받는다.
def get_values_in_parentheses(text):
    pattern = r"\(([^)]+)\)"
    matches = re.findall(pattern, text)
    
    return tuple(tuple(match.split(', ')) for match in matches)[0]

# while문에서 add, divide 등 command이후에 곱 연산을 하고 싶을 경우 사용한다. *를 기준으로 문자열을 나누고, 이 중 실수들을 모아 곱한 값을 반환한다
def check_the_asterisk(text) :
    product_result = 1
    if not text.find("*") == -1 :
        split_by_asterisk = text.split("*")
        for split_value in split_by_asterisk :
            try : 
                product_result = product_result * float(split_value)
            except :
                continue
        return product_result
    else :
        return product_result

# 튜플 안에 원소들이 특정 문자열과 겹치는지 확인
def contains_substring(tup, string) :
    for s in tup :
        if string in s or s in string :
            return True
    return False
# input value()를 통해 받은 튜플은 각 원소들이 문자형이므로 실수형으로 반환한다. 이때 명령어 ****(ex elbow())**** 등과 같은 것들도 값을 해석하여 모두 계산 가능한 실수값으로 표시한다.
def get_tuple_can_sum(input_values, material_data, classes) :
    def interpret(value, material_data) :
        
        value = value.replace(" ", "") # 공백 제거
        class_name, arg_str = value.split("(") #"("를 기준으로 앞에를 class, 뒤의 부분의 값들을 입력값으로 구분        
        product_result_front = check_the_asterisk(class_name)
        product_result_back = check_the_asterisk(arg_str)

        class_name = class_name.split("*")[-1]
        arg_str = arg_str.split("*")[0]
        arg_str = arg_str[:-1] #맨 뒤의 닫힘 괄호를 지움

        arg = arg_str.split(",") # ,를 기준으로 입력값들을 분리
        arg.insert(0, material_data)

        if class_name == 'elbow' :
            the_elbow = Elbow(*arg)
            the_span = the_elbow.get_span()
            return the_span * product_result_front * product_result_back

        elif class_name == 'tee' :
            the_tee = Tee(*arg)
            the_span = the_tee.get_span()
            return the_span * product_result_front * product_result_back

        elif class_name == 'reducer':
            the_reducer = Reducer(*arg)
            the_span = the_reducer.get_span()
            return the_span * product_result_front * product_result_back

        elif class_name == 'cap' :
            the_cap = Cap(*arg)
            the_span = the_cap.get_span()
            return the_span * product_result_front * product_result_back

        elif class_name == 'flange':
            the_flange = Flange(*arg)
            the_span = the_flange.get_span()
            return the_span * product_result_front * product_result_back

        elif class_name == 'valve':
            the_valve = Valve(*arg)
            the_span = the_valve.get_span()
            return the_span * product_result_front * product_result_back
        
        elif class_name == 'coupling' :
            the_coupling = Coupling(*arg)
            the_span = the_coupling.get_span()
            return the_span * product_result_front * product_result_back
        
        else : 
            raise ValueError(f"Unknown class : {class_name}")

    lst_to_be_tuple = []
    for value in input_values :
        if contains_substring(classes, value) is True :
            span = interpret(value, material_data)
            lst_to_be_tuple.append(span)
        else :
            try :
                lst_to_be_tuple.append(float(value)) 
            except :
                product_result = check_the_asterisk(value)
                lst_to_be_tuple.append(product_result)

    tuple_for_sum = tuple(lst_to_be_tuple)

    return tuple_for_sum

### Prompt part ###
classes = ('pipe', 'elbow', 'flange', 'reducer', 'tee', 'valve', 'coupling')
material_data = pd.read_csv('material.csv')
result = 0
previous_result = result

while True :
    command = input("명령을 입력하세요 : [result = " + str(result) + "] ")

    if command == "add" :
        
        give_me = input_values()
        
        if 'back' in give_me :
            continue
        else :
            previous_result= back_up_result(result)
            tuple_for_sum = get_tuple_can_sum(give_me, material_data, classes)
            do_command = Calculate(tuple_for_sum, result)
            result = do_command.add()

    elif command == "subtract" :
        give_me =input_values()
        
        if 'back' in give_me :
            continue
        else :
            previous_result= back_up_result(result)
            tuple_for_sum = get_tuple_can_sum(give_me, material_data, classes)
            do_command = Calculate(tuple_for_sum, result)
            result = do_command.subtract()
    
    elif command == "product" :
        give_me =input_values()
        
        if 'back' in give_me :
            continue
        else :
            previous_result= back_up_result(result)
            tuple_for_sum = get_tuple_can_sum(give_me, material_data, classes)
            do_command = Calculate(tuple_for_sum, result)
            result = do_command.product()
    
    elif command == "divde" :
        give_me =input_values()

        if 'back' in give_me :
            continue
        else :
            previous_result= back_up_result(result)
            tuple_for_sum = get_tuple_can_sum(give_me, material_data, classes)
            do_command = Calculate(tuple_for_sum, result)
            result = do_command.divde()

    elif command == "clear" :
        previous_result= back_up_result(result)
        result = all_clear(result)

    elif command == "exit" :
        break

    elif command == "cancel" :
        result = previous_result




    
