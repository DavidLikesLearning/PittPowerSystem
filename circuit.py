from bus import Bus
from load import Load
from resistor import Resistor


class Circuit:
    """
    Represents a circuit with buses, resistors, loads, sources.
    Computes voltage and current through the circuit.

    Attributes:

    """
    def __init__(self, name, buses, resistors,
                 loads,vsource):
        if not isinstance(name,str):
            raise TypeError('We need `name` to be str')
        if not isinstance(buses,dict):
            raise TypeError('We need `buses` to be dict')
        if not isinstance(resistors,dict):
            raise TypeError('We need `resistors` to be dict')
        if not isinstance(loads,dict):
            raise TypeError('We need `loads` to be dict')
        self.name = name
        self.buses = buses
        self.resistors = resistors
        self.loads = loads
        self.vsource = vsource
        self.i = None

    def add_bus(self, bus_name):
        """
        adds a bus to the circuit through `buses` dict
        """
        if bus_name in list(self.buses.keys()):
            raise Exception(f'{bus_name} name already exists in circuit')
        else:
            self.buses [bus_name] = Bus(bus_name,None)

    def add_resistor_element(self, r_name, r_bus1, r_bus2, r_r):
        """
        adds a resistor to the circuit through `resistors` dict
        """
        if r_name in list(self.resistors.keys()):
            raise Exception(f'{r_name} name already exists in circuit')
        else:
            self.resistors [r_name] = Resistor(r_name,r_bus1,r_bus2,r_r)

    def add_load_element(self, l_name, l_bus1, l_p,l_v):
        """
        adds a load to the circuit through `loads` dict
        """
        if l_name in list(self.loads.keys()):
            raise Exception(f'{l_name} name already exists in circuit')
        else:
            self.loads [l_name] = Load(l_name,l_bus1,l_v)


    def add_vsource_element(self, vsource):
        """
        adds a Vsource object to the circuit
        """
        self.vsource = vsource

    def set_i(self, i):
        """
        sets a current `i` in the circuit
        """
        self.i = i

    def print_nodal_voltage(self):
        """
        prints the nodal voltage of each bus in the circuit
        """
        for bus in self.buses.keys():
            print('Bus', bus,'voltage =',
                  self.buses[bus].get_bus_v(), 'V')

    def print_circuit_current(self):
        """
        prints the current of the circuit
        """
        print(f'Circuit Current: {self.i:.4f} A')

