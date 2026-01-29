class Resistor:
    """
    Represents a resistor in the circuit.

    Attributes:
        name (str): The name of the resistor
        bus1 (str): The name of the first bus
        bus2 (str): The name of the second bus
        r (float): The resistance value in ohms
        g (float): The conductance value in siemens
    """
    def __init__(self, name, bus1, bus2, r):
        if ~isinstance(r,float):
            raise TypeError('We need `r` to be float')
        if ~isinstance(bus1,str):
            raise TypeError('We need `bus1` to be str')
        if ~isinstance(bus2,str):
            raise TypeError('We need `bus2` to be str')
        if ~isinstance(name,str):
            raise TypeError('We need `name` to be str')
        self.name = name
        self.r = r
        self.bus1 = bus1
        self.bus2 = bus2
        self.calc_g()
    def calc_g(self):
        '''
        assigns a conductance `g` to the bus, computed from `r`
        '''
        self.g = 1/self.r

