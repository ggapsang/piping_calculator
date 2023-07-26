class Pipe :
    size : str    
    sch : str    
    def __init__(self, size, sch) :
        self.size = size
        self.sch = sch

    def outdia(self) :
        size = self.size
        
    def india(self) :
        size = self.size
        sch = self.sch
        
    def thick(self) :
        size = self.size
        sch = self.sch
        

class Elbow :
    size : str    
    sch : str
    joint_type : str
    degree : str
    long_or_short : str
    
    def __init__(self, size, sch, joint_type, long_or_short) :
        self.size = size
        self.sch = sch
        self.joint_type = joint_type
        self.degree = degree
        self.long_or_short = long_or_short

    def outdia(self) :
        size = self.size
        
    def india(self) :
        size = self.size
        sch = self.sch
        
    def thick(self) :
        size = self.size
        sch = self.sch

    def elbow_value(self) :
        size = self.size
        sch = self.sch
        joint_type = self.joint_type
        degree = self.degree
        long_or_short = self.long_or_short
  
class EqualTee :
    size : str    
    sch : str
    joint_types : str
    
    def __init__(self, size, sch, joint_type) :
        self.size = size
        self.sch = sch
        self.joint_type = joint_type

    def outdia(self) :
        size = self.size
        
    def india(self) :
        size = self.size
        sch = self.sch
        
    def thick(self) :
        size = self.size
        sch = self.sch

    def equal_tee_value(self) :
        size = self.size
        joint_type = self.joint_type
        
        
class RedTee :
    size : str    
    sch : str 
    joint_types : str
    subsize : str
    def __init__(self, size, sch, joint_type, subsize) :
        self.size = size
        self.sch = sch
        self.joint_type = joint_type
        self.subsize = subsize

    def outdia(self) :
        size = self.size
        
    def india(self) :
        size = self.size
        sch = self.sch
        
    def thick(self) :
        size = self.size
        sch = self.sch

    def red_tee_value(size, subsize, joint_type) :
        size = self.size
        subsize = self.subsize
        joint_type = self.joint_type

class Reducer :
    size : str    
    sch : str
    joint_types : str
    subsize : str
    def __init__(self, size, sch, joint_type, subsize) :
        self.size = size
        self.sch = sch
        self.joint_type = joint_type
        self.subsize = subsize

    def outdia(self) :
        size = self.size
        
    def india(self) :
        size = self.size
        sch = self.sch
        
    def thick(self) :
        size = self.size
        sch = self.sch
        
    def reducer_value(size, subsize, joint_type) :
        size = self.size
        subsize = self.subsize
        joint_type = self.joint_type

class Cap :    
    size : str    
    sch : str
    joint_types : str
    def __init__(self, size, sch, joint_type) :
        self.size = size
        self.sch = sch
        self.joint_type = joint_type

    def outdia(self) :
        size = self.size
        
    def india(self) :
        size = self.size
        sch = self.sch
        
    def thick(self) :
        size = self.size
        sch = self.sch :

    def cap_value(self) :
        size = self.size
        joint_type = self.joint_type

class Boss :
    size : str    
    subsize : str    
    def __init__(self, size, sch) :
        self.size = size
        self.sch = sch

    def outdia(self) :
        size = self.size
        
    def india(self) :
        size = self.size
        sch = self.sch
        
    def boss_value(self) :

class Union :
    size : str
    def __init__(self, size) :
        self.size = size

    def union_value(self) :
        self.size = input

class Flange :
    size : str    
    sch : str    
    joint_types : str
    flange_type : str
    flange_rating : str
    def __init__(self, size, sch, flange_type, flange_rating) :
        self.size = size
        self.sch = sch
        self.flang_type = flang_type
        self.flang_rating = flang_rating

    def outdia(self) :
        size = self.size
        
    def india(self) :
        size = self.size
        sch = self.sch
        
    def thick(self) :
        size = self.size
        sch = self.sch
        
    def flange_value(self) :
        size = self.size
        sch = self.sch
        flange_type = self.flange_type
        flange_rating = self.flange_rating
        
class Valve :
    size : str    
    sch : str
    joint_types : str
    valve_types : str
    valve_rating : str
    def __init__(self, size, sch, valve_type, joint_type) :
        self.size = size
        self.sch = sch
        self.valve_type = valve_type
        self.joint_type = joint_type

    def outdia(self) :
        size = self.size
        
    def india(self) :
        size = self.size
        sch = self.sch
        
    def thick(self) :
        size = self.size
        sch = self.sch

    def valve_value(size, valve_type, joint_type) :
        size = self.size
        sch = self.sch
        valve_type = self.valve_type
        joint_type = self.joint_type

class Coupling :
    size : str
    def __init__(self) :
        self.size = str
        
    def coupling_valve(size) :
        size = self.size
