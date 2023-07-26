class Pipe :
    size =
    sch = 
    joint_types = ("BW", "SW", "Screw")

    def __init__(self) :

    def outdia(size) :

    def india(size, sch) :

    def thick(size, sch) :

class Elbow :
    size =
    sch =
    joint_types = ("BW", "SW", "Screw")
    degree =
    long_or_short = ("Long", "Short")

    def __init__(self) :

    def outdia(size) :

    def india(size, sch) :

    def wall_thickness(size, sch) :

    def elbow_value(size, degree, long_or_short, joint_type)
  
class EqualTee :
    size =
    sch =
    joint_types = ("BW", "SW", "Screw")

    def __init__(self) :

    def outdia(size) :

    def india(size, sch) :

    def wall_thickness(size, sch) :

    def equal_tee_value(size, joint_type) :
        

class RedTee :
    size =
    sch =
    joint_types = ("BW", "SW", "Screw", "Flange")
    subsize =
    
    def __init__(self) : 
        
    def outdia(size) :

    def india(size, sch) :

    def wall_thickness(size, sch) :

    def red_tee_value(size, subsize, joint_type)


class Reducer :
    size =
    sch =
    joint_types = ("BW", "SW", "Screw", "Flange")
    subsize =
    
    def __init__(self) :

    def outdia(size) :

    def india(size, sch) :

    def wall_thickness(size, sch) :

    def reducer_value(size, subsize, joint_type) :

class Cap :
    size =
    sch =
    joint_types = ("BW", "SW", "Screw", "Flange")
    
    def __init__(self) :
        
    def outdia(size) :

    def india(size, sch) :

    def wall_thickness(size, sch) :

    def cap_value(size) :

class Boss :
    size =
    subsize =
    joint_types = ("BW", "SW", "Screw", "Flange")

    def __init__(self) :

    def outdia(size) :

    def india(size, sch) :

    def wall_thickness(size, sch) :

    def boss_value(size) :

class Union :
    size =
    joint_types = ("BW", "SW", "Screw", "Flange")

    def __init__(self) :

    def outdia(size) :

    def india(size, sch) :

    def union_valeu()


class Flange :
    size =
    sch =
    joint_types = ("BW", "SW", "Screw", "Flange")
    flange_type =
    flange_rating =

    def __init__(self) :
        
    def outdia(size) :

    def india(size, sch) :

    def wall_thickness(size, sch) :

    def flange_value(size, flange_rating, flange_type) :

class Valve :
    size =
    sch =
    joint_types = ("BW", "SW", "Screw", "Flange")
    valve_types =
    valve_rating = 

    def __init__(self) :
        
    def outdia(size) :

    def india(size, sch) :

    def wall_thickness(size, sch) :

    def valve_value(size, valve_type, joint_type) :

class Coupling :
    size =
    shc =
    joint_types = ("BW", "SW", "Screw", "Flange")
    
    def __init__(self) :
        
    def outdia(size) :

    def india(size, sch) :

    def wall_thickness(size, sch) :

    def coupling_type(size) :
