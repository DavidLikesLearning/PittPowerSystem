class Bus:
    def __init__(self, name, v):
        if ~isinstance(v,(int,float)):
            raise TypeError('We need `v` to be float or str')
        if ~isinstance(name,str):
            raise TypeError('We need `name` to be str')
        self.name = name
        self.v = v
    def set_bus_v(self,v):
        '''
        assigns a voltage `v` to the bus
        '''
        if ~isinstance(v,(int,float)):
            raise TypeError('We need `v` to be float or str')
        self.v = v
    def get_bus_v(self):
        return self.v