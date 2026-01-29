class Vsource:
    def __init__(self, name, bus1,v):
        if ~isinstance(name,str):
            raise TypeError('We need `name` to be str')
        if ~isinstance(bus1,float):
            raise TypeError('We need `p` to be float')
        if ~isinstance(v,float):
            raise TypeError('We need `v` to be float')
        self.name = name
        self.bus1 = bus1
        self.v = v
