from circuit import Circuit
from load import Load
from resistor import Resistor
from bus import Bus
from vsource import Vsource
from solution import Solution

def main():
    bus_a = Bus("A")
    bus_b = Bus('B')
    v_src = Vsource('source', bus_a, 100)
    res = Resistor('res', bus_a, bus_b, 5)
    load = Load('load', bus_b, 2000)
    circuit = Circuit('test',{'A':bus_a,'B': bus_b},
    {'res': res}, {'load':load}, v_src)
    solution = Solution(circuit)
    solution.do_power_flow()


if __name__ == "__main__":
    main()
