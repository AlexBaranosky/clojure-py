from ifn import IFn
from cljexceptions import AbstractMethodCall, ArityException
from ipersistentset import IPersistentSet
import rt as RT

class APersistentSet(IPersistentSet, IFn):
    def __init__(self, impl):
        self.impl = impl
    def __getitem__(self, item):
        return self.impl[item]

    def __contains__(self, item):
        return item in self.impl

    def __len__(self):
        return len(self.impl)

    def seq(self):
        return RT.keys(self.impl)

    def __call__(self, *args):
        if len(args) != 1:
            raise ArityException()
        return self.impl[args[0]]

    def __eq__(self, other):
        if self is other:
            return True
        if not RT.fulfillsHashSet(other):
            return False

        for s in self:
            if s not in other or other[s] != self[s]:
                return False
        return True

    def __hash__(self):
        if self._hash == -1:
            hsh = 0
            s = self.seq()
            while s is not None:
                e = s.first()
                hsh += hash(e)
                s = s.next()
            self._hash = hsh
        return self._hash





