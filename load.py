class Load:
    """
    Represents load in the circuit

    Attributes:
        name: name of the load
        bus1: connected bus
        p: active power consumption
        q: reactive power consumption
    """
    def __init__(self, name, bus1, p, q=0, nom_volt = 100):
        if not isinstance(name,str):
            raise TypeError('We need `name` to be str')
        if not isinstance(p,(float,int)):
            raise TypeError('We need `p` to be float or int')
        if not isinstance(q,(float,int)):
            raise TypeError('We need `q` to be float or int')
        self.name = name
        self.bus1 = bus1
        self.p = p
        self.q = q
        self.g = None
        self.calc_g(nom_volt)

    def calc_g(self, nom_volt):
        '''
        return the conductance `g` of the load
        '''
        if self.bus1.get_bus_v()== None:
            self.g =  self.p/nom_volt**2
        else:
            bus_v = self.bus1.get_bus_v()
            bus_i = self.p/bus_v
            self.g = (bus_i/bus_v)

