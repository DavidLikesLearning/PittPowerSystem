class Vsource:
    """
    Represents a voltage source

    Attributes:
        name: Name of the source
        bus1: Connected bus
        v: Voltage of source
    """
    def __init__(self, name, bus1,v):
        if not isinstance(name,str):
            raise TypeError('We need `name` to be str')
        if not isinstance(v,(float, int)):
            raise TypeError('We need `v` to be float or int')
        self.name = name
        self.bus1 = bus1
        self.v = v
