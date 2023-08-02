import pandas as pd
import re
import math

## test for git commit in code space
### Material Classes ###
class Material:
    default_values = {
        'sch' : 'std',
        'rating' : None,
        'joint' : 'bw',
        'degree' : 90,
        'radius' : 'lr',
        'flange_type' : 'wn',
        'valve_type' : None,
    }

    def __init__(self, material_data, size, sch=None, rating=None, joint=None, degree=None, radius=None, flange_type=None, valve_type=None):
        self.material_data = material_data
        self.size = float(size)
        self.sch = sch if sch else Material.default_values['sch']
        self.rating = rating if rating else Material.default_values['rating']
        self.joint = joint if joint else Material.default_values['joint']
        self.rating = rating if rating else Material.default_values['rating']
        self.degree = degree if degree else Material.default_values['degree']
        self.radius = radius if radius else Material.default_values['radius']
        self.flange_type = flange_type if flange_type else Material.default_values['flange_type']
        self.valve_type = valve_type if valve_type else Material.default_values['valve_type']

    def get_outdia(self):
        name = 'pipe'
        material_data = self.material_data
        size = float(self.size)
        outdia = search_value_in_df(material_data, result_col= 'outdia', name=name, size=size)
        return float(outdia)

    def get_india(self):
        name = 'pipe'
        material_data = self.material_data
        size = float(self.size)
        sch = self.sch
        india = search_value_in_df(material_data, result_col= 'india', name=name, size=size, sch=sch)
        return float(india)

    def get_thick(self) :
        name = 'pipe'
        material_data = self.material_data
        size = float(self.size)
        sch = self.sch
        thick = search_value_in_df(material_data, result_col='thick', name=name, size=size, sch=sch)
        return float(thick)
    
    def get_sch(self) :
        name = 'pipe'
        material_data = self.material_data
        size = float(self.size)
        thick = float(self.get_thick)
        sch = search_value_in_df(material_data, result_col='sch', name=name, size=size, thick=thick)
        return sch
    
    def get_span(self) :
        pass
    
    @classmethod
    def set_value(cls, attribute, value):
        if attribute in cls.default_values:
            if attribute in cls.default_values :
                cls.default_values[attribute] = value
            else:
                print(f'{attribute}는 유효한 속성값이 아닙니다 다음의 리스트를 참조하세요: {list(cls.default_values.keys())}')

class Pipe(Material):
    def __init__(self, material_data, size, sch=None):
        super().__init__(material_data, size, sch)
        self.name = 'pipe'

class Elbow(Material):
    def __init__(self, material_data, size, sch=None, rating=None, joint=None, degree=None, radius=None):
        super().__init__(material_data, size, sch, rating, joint, degree, radius)
        self.name = 'elbow'

    def get_span(self) :
        name = self.name
        material_data = self.material_data
        size = float(self.size)
        joint = self.joint
        degree = self.degree
        radius = self.radius
        rating = self.rating

        if degree == 45 or degree == 90 :
            span = search_value_in_df(material_data, result_col='span', name=name, size=size, joint=joint, degree=degree, radius=radius, rating=rating)
            return span
        else :
            radian_degree = math.radians(degree)
            if radius == 'sr' :
                span = 1.0 * 25.4 * math.tan(radian_degree/2)
                return span
            else :
                span = 1.5 * 25.4 * math.tan(radian_degree/2)
                return span
        
class Tee(Material):
    def __init__(self, material_data, size, subsize, sch=None, rating=None, joint=None):
        super().__init__(material_data, size, sch, rating, joint)
        self.name = 'tee'
        self.subsize = subsize

    def get_span(self) :
        name = self.name
        material_data = self.material_data
        size = float(self.size)
        subsize = float(self.subsize)
        joint = self.joint
        rating = self.rating

        span = search_value_in_df(material_data, result_col='span', name=name, size=size, joint=joint, subsize=subsize, rating=rating)
        return span
    
    def get_span_half(self) :
        name = self.name
        material_data = self.material_data
        size = float(self.size)
        subsize = float(self.subsize)
        joint = self.joint
        rating = self.rating

        span = search_value_in_df(material_data, result_col='span', name=name, size=size, joint=joint, subsize=subsize, rating=rating)
        return (span/2)
    
    def get_short_span(self) :
        name = self.name
        material_data = self.material_data
        size = float(self.size)
        subsize = float(self.subsize)
        joint = self.joint
        rating = self.rating

        span = search_value_in_df(material_data, result_col='short_span', name=name, size=size, joint=joint, subsize=subsize, rating=rating)
        return span

class Reducer(Material):
    def __init__(self, material_data, size, subsize, sch=None, rating=None, joint=None):
        super().__init__(material_data, size, sch, rating, joint)
        self.name = 'reducer'
        self.subsize = subsize
    
    def get_span(self) :
        name = self.name
        material_data = self.material_data
        size = float(self.size)
        subsize = float(self.subsize)
        rating = self.rating
        joint = self.joint

        span = search_value_in_df(material_data, result_col='span', name=name, size=size, joint=joint, subsize=subsize, rating=rating)
        return span

class Cap(Material):
    def __init__(self, material_data, size, sch=None, rating=None, joint=None):
        super().__init__(material_data, size, sch, rating, joint)
        self.name = 'cap'
    
    def get_span(self):
        name = self.name
        size = self.size
        joint = self.joint
        rating = self.rating

        span = search_value_in_df(material_data, result_col='span', name=name, size=size, joint=joint, rating=rating)
        return span

class Flange(Material):
    def __init__(self, material_data, size, sch=None, flange_type=None, rating=None):
        super().__init__(material_data, size, sch, rating, flange_type)
        self.name = 'flange'

    def get_span(self) :
        name = self.name
        size = self.size
        flange_type = self.flange_type
        rating = self.rating

        span = search_value_in_df(material_data, result_col='span', name=name, size=size, rating=rating, flange_type=flange_type)
        return span

class Valve(Material):
    def __init__(self, material_data, size, sch=None, valve_type=None, joint=None):
        super().__init__(material_data, size, sch, valve_type, joint)
        self.name = 'valve'
        self.joint = joint
    
    def get_span(self):
        name = self.name
        size = self.size
        valve_type = self.valve_type
        rating = self.rating

        span  = search_value_in_df(material_data, result_col='span', name=name, szie=size, valve_type=valve_type, rating=rating)
        return span

class Coupling(Material):
    def __init__(self, material_data, size=None, rating=None):
        super().__init__(size, material_data, rating)
        self.name = 'copling'

    def get_span(self):
        name = self.name
        size = self.size
        rating =self.rating

        span = search_value_in_df(material_data, result_col='span', name=name, size=size, rating=rating)
        return span
    

### Caculate class ###
class Calculate :
    
    values_to_calculate : tuple

    def __init__(self, tup_for_arithmetic, result) :
        self.tup_for_arithmetic = tup_for_arithmetic
        self.result = result
    
    def add(self) :
        tup_for_arithmetic = self.tup_for_arithmetic
        result = self.result
        sum_of_tuple = sum(tup_for_arithmetic)
        result = result + sum_of_tuple

        return result

    def subtract(self) :
        input_values = self.tup_for_arithmetic
        result = self.result
        sum_of_input_values = sum(input_values)
        result = result - sum_of_input_values

        return result

    def mutiply(self) :
        input_values = self.tup_for_arithmetic
        result = self.result
        for element in input_values :
            result = result * element
        return result
    
    def divide(self) :
        input_values = self.tup_for_arithmetic
        result = self.result
        for element in input_values :
            result = result / element
        return result

## Functions to process command##
def search_value_in_df(material_data, result_col, **conditions) :
    condition_list = []

    for col, value in conditions.items() :
        if pd.isnull(value) :
            condition = material_data[col].isnull()
        else :
            condition = material_data[col] == value
        condition_list.append(condition)

    combined_condition = condition_list[0]
    for condition in condition_list[1:] :
        combined_condition &= condition

    filtered_data = material_data[combined_condition]

    if not filtered_data.empty : 
        return filtered_data.iloc[0][result_col]
    return 0

# input 값을 스페이스 기준으로 텍스트 나누어 튜플로 받는다. 단 "()"안의 값들은 분리되지 않음#
def input_values() :
    # 스페이스 기준으로 텍스트 나누어 튜플로 받는다. 단 "()"안의 값들은 분리되지 않음#
    def split_text(text):
        pattern = r"\S*\([^)]*\)|\S+"
        matches = re.findall(pattern, text)
        return tuple(matches)
    input_values = input("입력값 : ")
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

# 사용자에게 받은 명령어를 class 생성에 입력 가능한 방식으로 바꾼다. 
def interpret(value, material_data) :

    value = value.replace(" ", "") # 공백 제거
    class_name, arg_str = value.split("(") #"("를 기준으로 앞에를 class, 뒤의 부분의 값들을 입력값으로 구분        
    product_result_front = check_the_asterisk(class_name)
    product_result_back = check_the_asterisk(arg_str)

    class_name = class_name.split("*")[-1]
    arg_str = arg_str.split("*")[0]
    arg_str = arg_str[:-1] #맨 뒤의 닫힘 괄호를 지움

    arg = arg_str.split(",") # ,를 기준으로 입력값들을 분리

    if class_name == 'tee' or class_name == 'reducer' : #subsize를 갖는 피팅들
        arg_dict = {'material_data' : material_data}
        first_size = 0
        for element_arg in arg :
            if '=' in element_arg :
                key, val = element_arg.split('=')
                if val.isnumeric():
                    arg_dict[key] = int(val) if val.isdigit() else float(val)
                else :
                    arg_dict[key] = val
            else :
                if first_size == 0 :
                    arg_dict['size'] = int(element_arg) if element_arg.isdigit() else element_arg
                    first_size = 1
                else :
                    arg_dict['subsize'] = int(element_arg) if element_arg.isdigit() else element_arg
                    first_size = 0

    else :
        arg_dict = {'material_data' : material_data}
        for element_arg in arg :
            if '=' in element_arg :
                key, val = element_arg.split('=')
                if val.isnumeric():
                    arg_dict[key] = int(val) if val.isdigit() else float(val)
                else :
                    arg_dict[key] = val
            else :
                arg_dict['size'] = int(element_arg) if element_arg.isdigit() else element_arg

    return class_name, arg_dict, product_result_front, product_result_back
    #arg.insert(0, material_data)

# interpret 함수를 통해 받은 명령어를 한번 더 해석하여 연산이 가능한 숫자 형태의 튜플을 만든다
def get_tup_for_arithmetic(input_values, material_data, classes) :
    
    lst_to_be_tuple = []
    for value in input_values :
        if contains_substring(classes, value) is True :
            span = interpret(value, material_data)
            if span[0] == 'elbow' :
                the_elbow = Elbow(**span[1])
                the_span = the_elbow.get_span()
                if the_span == 0 :
                    print("값을 찾을 수 없습니다. ", value, "값을 제외하고 계산합니다.")
                the_span = the_span * span[2] * span[3]

            elif span[0] == 'tee' :
                the_tee = Tee(**span[1])
                the_span = the_tee.get_span()
                if the_span == 0 :
                    print("값을 찾을 수 없습니다. ", value, "값을 제외하고 계산합니다.")
                the_span = the_span * span[2] * span[3]

            elif span[0] == 'reducer':
                the_reducer = Reducer(**span[1])
                the_span = the_reducer.get_span()
                if the_span == 0 :
                    print("값을 찾을 수 없습니다. ", value, "값을 제외하고 계산합니다.")
                the_span = the_span * span[2] * span[3]

            elif span[0] == 'cap' :
                the_cap = Cap(**span[1])
                the_span = the_cap.get_span()
                if the_span == 0 :
                    print("값을 찾을 수 없습니다. ", value, "값을 제외하고 계산합니다.")
                the_span = the_span * span[2] * span[3]

            elif span[0] == 'flange':
                the_flange = Flange(**span[1])
                the_span = the_flange.get_span()
                if the_span == 0 :
                    print("값을 찾을 수 없습니다. ", value, "값을 제외하고 계산합니다.")
                the_span = the_span * span[2] * span[3]

            elif span[0] == 'valve':
                the_valve = Valve(**span[1])
                the_span = the_valve.get_span()
                if the_span == 0 :
                    print("값을 찾을 수 없습니다. ", value, "값을 제외하고 계산합니다.")
                the_span = the_span * span[2] * span[3]

            elif span[0] == 'coupling' :
                the_coupling = Coupling(**span[1])
                the_span = the_coupling.get_span()
                if the_span == 0 : 
                    print("값을 찾을 수 없습니다. ", value, "값을 제외하고 계산합니다.")
                the_span = the_span * span[2] * span[3]

            else : 
                raise ValueError(f"Unknown class : {span[0]}")
            
            lst_to_be_tuple.append(the_span)

        else :
            try :
                lst_to_be_tuple.append(float(value)) 
            except :
                product_result = check_the_asterisk(value)
                lst_to_be_tuple.append(product_result)

    tup_for_arithmetic = tuple(lst_to_be_tuple)

    return tup_for_arithmetic

# material class의 공통 속성을 보여준다. "show me" 커맨드를 위한 함수
def show_me_attribute(input_values, material_data, classes, attribute) :

     for value in input_values :
        if contains_substring(classes, value) is True :
            span = interpret(value, material_data)
            if span[0] == 'elbow' :
                the_elbow = Elbow(**span[1])
                the_span = getattr(the_elbow, attribute)()
                if the_span == 0 :
                    print("값을 찾을 수 없습니다. ASTM 규격에 없는 피팅입니다")
                the_span = the_span * span[2] * span[3]
                return the_span

            elif span[0] == 'tee' :
                the_tee = Tee(**span[1])
                the_span = getattr(the_tee, attribute)()
                if the_span == 0 :
                    print("값을 찾을 수 없습니다. ASTM 규격에 없는 피팅입니다")
                the_span = the_span * span[2] * span[3]
                return the_span

            elif span[0] == 'reducer':
                the_reducer = Reducer(**span[1])
                the_span = getattr(the_reducer, attribute)()
                if the_span == 0 :
                    print("값을 찾을 수 없습니다. ASTM 규격에 없는 피팅입니다")
                the_span = the_span * span[2] * span[3]
                return the_span

            elif span[0] == 'cap' :
                the_cap = Cap(**span[1])
                the_span = getattr(the_cap, attribute)()
                if the_span == 0 :
                    print("값을 찾을 수 없습니다.", value, "값을 제외하고 계산합니다.")
                the_span = the_span * span[2] * span[3]
                return the_span

            elif span[0] == 'flange':
                the_flange = Flange(**span[1])
                the_span = getattr(the_flange, attribute)()
                if the_span == 0 :
                    print("값을 찾을 수 없습니다. ASTM 규격에 없는 피팅입니다")
                the_span = the_span * span[2] * span[3]
                return the_span

            elif span[0] == 'valve':
                the_valve = Valve(**span[1])
                the_span = getattr(the_valve, attribute)()
                if the_span == 0 :
                    print("값을 찾을 수 없습니다. ASTM 규격에 없는 피팅입니다")
                the_span = the_span * span[2] * span[3]
                return the_span

            elif span[0] == 'coupling' :
                the_coupling = Coupling(**span[1])
                the_span = getattr(the_coupling, attribute)()
                if the_span == 0 : 
                    print("값을 찾을 수 없습니다. ASTM 규격에 없는 피팅입니다")
                the_span = the_span * span[2] * span[3]
                return the_span
            
            elif span[0] == 'pipe' :
                the_pipe = Pipe(**span[1])
                the_span = getattr(the_pipe, attribute)()
                if the_span == 0 :
                    print("값을 찾을 수 없습니다. ASTM 규격에 없는 값입니다")
                the_span = the_span * span[2] * span[3]
                return the_span

            else : 
                raise ValueError(f"확인 불가능한 명령 : {span[0]}")

def show_read_me(read_me):
    with open(str(read_me), 'r', encoding='utf-8') as fp_read_me :
        for line in fp_read_me.readlines() :
            print(line.strip())

### Prompt part ###
classes = (
    'pipe', 
    'elbow',
    'tee',
    'reducer',
    'cap', 
    'flange',
    'valve',
    'coupling',
)
material_data = pd.read_csv('material.csv')
result = 0
previous_result = result
read_me = 'read me.txt'
show_read_me(read_me)


while True :
    command = input("명령을 입력하세요(도움말을 다시 보려면 help라고 치세요) : [현재값 = " + str(result) + "] ")
    
    if command.startswith("add") :
        give_me = input_values()

        if 'back' in give_me :
            continue
        else :
            previous_result= back_up_result(result)
            tup_for_arithmetic = get_tup_for_arithmetic(give_me, material_data, classes)
            do_command = Calculate(tup_for_arithmetic, result)
            result = do_command.add()

    elif command.startswith("subtract") :
        give_me =input_values()
        
        if 'back' in give_me :
            continue
        else :
            previous_result= back_up_result(result)
            tup_for_arithmetic = get_tup_for_arithmetic(give_me, material_data, classes)
            do_command = Calculate(tup_for_arithmetic, result)
            result = do_command.subtract()
    
    elif command.startswith("multi") :
        give_me =input_values()
        
        if 'back' in give_me :
            continue
        else :
            previous_result= back_up_result(result)
            tup_for_arithmetic = get_tup_for_arithmetic(give_me, material_data, classes)
            do_command = Calculate(tup_for_arithmetic, result)
            result = do_command.mutiply()
    
    elif command.startswith("divide") :
        give_me =input_values()

        if 'back' in give_me :
            continue
        else :
            previous_result= back_up_result(result)
            tup_for_arithmetic = get_tup_for_arithmetic(give_me, material_data, classes)
            do_command = Calculate(tup_for_arithmetic, result)
            result = do_command.divide()

    elif command.startswith("clear") :
        previous_result= back_up_result(result)
        result = all_clear(result)

    elif command.startswith("exit") :
        exit()

    elif command.startswith("cancel") :
        result = previous_result

    elif command.startswith('show me') :
        if 'outdia' in command :        
            while True :
                give_me = input_values()
                if 'back' in give_me :
                    break
                elif 'exit' in give_me :
                    exit()
                else :
                    do_command = show_me_attribute(give_me, material_data, classes, 'get_outdia')
                    print(do_command)
        elif 'india' in command :
            while True :
                give_me = input_values()
                if 'back' in give_me :
                    break
                elif 'exit' in give_me :
                    exit()
                else :
                    do_command = show_me_attribute(give_me, material_data, classes, 'get_india')
                    print(do_command)
        elif 'thick' in command :
            give_me = input_values()
            while True :
                give_me = input_values()
                if 'back' in give_me :
                    break
                elif 'exit' in give_me :
                    exit()
                else :
                    do_command = show_me_attribute(give_me, material_data, classes, 'get_thick')
                    print(do_command)
        elif 'sch' in command :
            while True :
                give_me = input_values()
                if 'back' in give_me :
                    break
                elif 'exit' in command :
                    exit()
                else :
                    do_command = show_me_attribute(give_me, material_data, classes, 'get_sch')
                    print(do_command)
        elif 'half span' in command :
            while True :
                give_me = input_values()
                if 'back' in give_me :
                    break
                elif 'exit' in give_me :
                    exit()
                else : 
                    do_command = show_me_attribute(give_me, material_data, classes, 'get_half_span')
                    print(do_command)        
        elif 'short span' in command :
            while True :
                give_me = input_values()
                if 'back' in give_me :
                    break
                elif 'exit' in give_me :
                    exit()
                else :
                    do_command = show_me_attribute(give_me, material_data, classes, 'get_short_span')
                    print(do_command)
        elif 'span' in command :
            while True :
                give_me = input_values()
                if 'back' in give_me :
                    break
                elif 'exit' in give_me :
                    exit()
                else :
                    do_command = show_me_attribute(give_me, material_data, classes, 'get_span')
                    print(do_command)

    elif command.startswith('set value') :
        print('현재 설정된 spec 값 : ', Material.default_values)
        while True :
            second_command = input('설정 변경(속성=값) : ')
            if second_command.startswith('back') :
                break
            else :
                attr_values = second_command.split() #" "단위로 분리하여 여러 개의 'key=value'쌍들을 추출한 리스트를 만든다
                #리스트에 있는 각각의 'key=value'형태의 원소를 '='단위로 다시 분리하여 Materail.set_default(attribute, new_value)에 대입한다.
                for attr_value in attr_values : 
                    attr_value_lst = attr_value.split('=')
                    attribute = attr_value_lst[0]
                    new_value = attr_value_lst[1]
                    if new_value.isdigit() :
                        new_value = float(new_value)
                    else :
                        pass 
                    Material.set_value(attribute, new_value)
                print('변경됨 : ', Material.default_values)

    elif command.startswith('help') :
        show_read_me(read_me)
    else :
        pass
