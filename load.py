class Load:
    def __init__(self, name, bus1, v):
        if ~isinstance(v,float):
            raise TypeError('We need `v` to be float')
        if ~isinstance(name,str):
            raise TypeError('We need `name` to be str')
        self.name = name
        self.bus1 = bus1
        self.v = v
