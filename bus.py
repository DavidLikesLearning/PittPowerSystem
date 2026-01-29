class Bus:
    """
    Represents a bus (node) in the circuit.

    Attributes:
        name (str): The name of the bus
        v (float): The voltage at the bus
        g (float): The conductance at the bus
    """
    def __init__(self, name, v):
        if ~isinstance(v,(int,float, None)):
            raise TypeError('We need `v` to be float')
        if ~isinstance(name,str):
            raise TypeError('We need `name` to be str')
        self.name = name
        self.v = v
    def set_bus_v(self,v):
        '''
        assigns a voltage `v` to the bus
        '''
        if ~isinstance(v,float):
            raise TypeError('We need `v` to be float')
        self.v = v
    def get_bus_v(self):
        return self.v