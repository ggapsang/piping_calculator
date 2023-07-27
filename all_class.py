class Pipe :
    size : float    
    sch : str    
    def __init__(self, size, sch) :
        self.size = size
        self.sch = sch
    
    def get_outdia(self) :
        size = self.size
        
    def get_india(self) :
        size = self.size
        sch = self.sch
        
    def get_thick(self) :
        size = self.size
        sch = self.sch
        
class Elbow :
    size : float    
    sch : str
    joint_type : str
    degree : float
    long_or_short : str
    
    def __init__(self, size, sch, joint_type, degree, long_or_short) :
        self.size = size
        self.sch = sch
        self.joint_type = joint_type
        self.degree = degree
        self.long_or_short = long_or_short
    
    def get_outdia(self) :
        size = self.size
        
    def get_india(self) :
        size = self.size
        sch = self.sch
        
    def get_thick(self) :
        size = self.size
        sch = self.sch

    def get_span(self) :
        size = self.size
        sch = self.sch
        joint_type = self.joint_type
        degree = self.degree
        long_or_short = self.long_or_short
  
class Tee :
    size : float    
    subsize : float
    sch : str
    joint_type : str
    
    def __init__(self, size, sch, joint_type, subsize) :
        self.size = size
        self.sch = sch
        self.joint_type = joint_type
        self.subsize = subsize

    def get_outdia(self) :
        size = self.size
        
    def get_india(self) :
        size = self.size
        sch = self.sch
        
    def get_thick(self) :
        size = self.size
        sch = self.sch
    
    def get_span(self) :
        size = self.size
        subsize = self.subsize
        joint_type = self.joint_type
        if subsize > size :
            size, subsize = subsize, size
        else :
            pass

    def get_short_span(self) :
        size = self.size
        subsize = self.subsize
        joint_type = self.joint_type
        
class Reducer :
    size : float    
    sch : str
    joint_type : str
    subsize : float
    def __init__(self, size, sch, joint_type, subsize) :
        self.size = size
        self.sch = sch
        self.joint_type = joint_type
        self.subsize = subsize
    
    def get_outdia(self) :
        size = self.size
        
    def get_india(self) :
        size = self.size
        sch = self.sch
        
    def get_thick(self) :
        size = self.size
        sch = self.sch
        
    def get_span(self) :
        size = self.size
        subsize = self.subsize
        joint_type = self.joint_type
        if subsize > size :
            size, subsize = subsize, size
        else :
            pass

class Cap :    
    size : float    
    sch : str
    joint_type : str
    def __init__(self, size, sch, joint_type) :
        self.size = size
        self.sch = sch
        self.joint_type = joint_type
    
    def get_outdia(self) :
        size = self.size
        
    def get_india(self) :
        size = self.size
        sch = self.sch
        
    def get_thick(self) :
        size = self.size
        sch = self.sch

    def get_span(self) :
        size = self.size
        joint_type = self.joint_type

class Flange :
    size : float    
    sch : str    
    joint_type : str
    flange_type : str
    flange_rating : str
    def __init__(self, size, sch, flange_type, flange_rating) :
        self.size = size
        self.sch = sch
        self.flang_type = flange_type
        self.flang_rating = flange_rating

    def get_outdia(self) :
        size = self.size
        
    def get_india(self) :
        size = self.size
        sch = self.sch
        
    def get_thick(self) :
        size = self.size
        sch = self.sch
        
    def get_span(self) :
        size = self.size
        sch = self.sch
        flange_type = self.flange_type
        flange_rating = self.flange_rating
        
class Valve :
    size : float    
    sch : str
    joint_type : str
    valve_types : str
    valve_rating : str
    def __init__(self, size, sch, valve_type, joint_type) :
        self.size = size
        self.sch = sch
        self.valve_type = valve_type
        self.joint_type = joint_type
    
    def get_outdia(self) :
        size = self.size
        
    def get_india(self) :
        size = self.size
        sch = self.sch
        
    def get_thick(self) :
        size = self.size
        sch = self.sch

    def get_span(self) :
        size = self.size
        sch = self.sch
        valve_type = self.valve_type
        joint_type = self.joint_type

class Coupling :
    size : float
    def __init__(self) :
        self.size = str

    def get_span(self) :
        size = self.size
