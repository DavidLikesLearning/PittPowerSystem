class Bus:
    """
    Represents a bus (node) in the circuit.

    Attributes:
        name (str): The name of the bus
        v (float): The voltage at the bus
        g (float): The conductance at the bus
    """
    def __init__(self, name):
        if not isinstance(name,str):
            raise TypeError('We need `name` to be str')
        self.name = name
        self.v = None
    def set_bus_v(self,v):
        """
        assigns a voltage `v` to the bus
        """
        if not isinstance(v,(float,int)):
            raise TypeError('We need `v` to be float or int')
        self.v = v
    def get_bus_v(self):
        return self.v