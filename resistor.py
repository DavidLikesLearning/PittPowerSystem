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
        if not isinstance(r,(float, int)):
            raise TypeError('We need `r` to be float or int')
        if not isinstance(name,str):
            raise TypeError('We need `name` to be str')
        self.name = name
        self.r = r
        self.bus1 = bus1
        self.bus2 = bus2
        self.g = None
        self.calc_g()

    def calc_g(self):
        """
        assigns a conductance `g` to the bus, computed from `r`
        """
        self.g = 1/self.r

