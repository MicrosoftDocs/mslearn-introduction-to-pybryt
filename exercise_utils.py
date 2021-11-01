import pybryt
from copy import deepcopy


class ValueWrapper:
    
    def __init__(self, annot):
        self.annot = annot
        
    def __eq__(self, other):
        return isinstance(other, type(self)) and \
            type(self.annot) == type(other.annot) and \
            (not isinstance(self.annot, pybryt.Value) or \
             self.annot.check_values_equal(self.annot.initial_value, other.annot.initial_value))


class value_invariant(pybryt.invariants.invariant):
    @staticmethod
    def run(values):
        ret = []
        for v in values:
            if isinstance(v, pybryt.Annotation):
                v = ValueWrapper(v)
            ret.append(v)
        return ret


def values_equal(v1, v2):
    if not isinstance(v2, type(v1)):
        return False
    return v1.check_values_equal(v1.initial_value, v2.initial_value)


class fiberator:
    def __init__(self):
        self.i, self.j = 0, 1
        self.n = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.n += 1
        if self.n == 1:
            return self.i
        if self.n > 2:
            self.i, self.j = self.j, self.i + self.j
        return self.j
