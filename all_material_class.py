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
