from circuit import Circuit

class Solution:
    """
    Solves a circuit with buses, resistors, loads, sources.
    Computes voltage and current through the circuit.

    Methods:
        do_power_flow:  compute current

    """
    def __init__(self, circuit):
        self.circuit = circuit

    def do_power_flow(self):
        """
        compute voltage and current through the circuit

        assuming non looping circuit, all buses in series, single load
        """
        buses = self.circuit.buses
        resistors = self.circuit.resistors
        loads = self.circuit.loads
        vsource = self.circuit.vsource

        bus_pairs = []

        #will account for all resistors
        sum_r = 0
        for r_name in resistors:
            resistor = resistors[r_name]
            sum_r += 1/resistor.g
            bus_pairs.append([resistor.bus1.name,resistor.bus2.name])

        #will account for all load resistances
        sum_p = 0
        for l_name in loads:
            sum_p += loads[l_name].p
            sum_r += 1/loads[l_name].g

        curr = vsource.v / sum_r
        self.circuit.set_i(curr)

        #now to assign voltages

        v_bus = vsource.bus1.name
        buses[vsource.bus1.name].set_bus_v(vsource.v)

        resistor_buses = [i for i in bus_pairs if i[0] == v_bus or i[1] == v_bus][0]
        l_bus  = resistor_buses[0] if resistor_buses[1] == v_bus else resistor_buses[1]
        this_r = resistors[r_name]

        buses[l_bus].set_bus_v(vsource.v -this_r.r*curr )

        self.circuit.buses = buses
        self.circuit.resistors = resistors
        self.circuit.loads = loads

        self.circuit.print_nodal_voltage()
        self.circuit.print_circuit_current()
        return self.circuit





