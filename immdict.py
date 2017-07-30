from copy import deepcopy

class ImmDict:

    def __init__(self):
        self.imm_dict = {}

    def put(self, key, values):
        new_dict = deepcopy(self.imm_dict)
        new_dict[key] = values
        empty_dict = ImmDict()
        empty_dict.imm_dict = new_dict
        return empty_dict

    def get(self, key):
        if key in self.imm_dict.keys():
            return self.imm_dict[key]
        else:
            return None

    def keys(self):
        return deepcopy(list(self.imm_dict.keys()))

    def values(self):
        return deepcopy(list(self.imm_dict.values()))

#d = ImmDict()
#print(d.imm_dict)
#print(d.keys())

#f = d.put(4,65)
#print(f.imm_dict)
#print(d.values())
#print(f.keys())
#print(f.values())



