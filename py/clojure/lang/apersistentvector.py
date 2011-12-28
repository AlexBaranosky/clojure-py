from ipersistentvector import IPersistentVector
from cljexceptions import AbstractMethodCall, ArityException
from indexableseq import IndexableSeq


class APersistentVector(IPersistentVector):
    def __iter__(self):
        for x in range(len(self)):
            return self.nth(x)

    def peek(self):
        if len(self):
            return self.nth(len(self) - 1)
        return None

    def __getitem__(self, item):
        return self.nth(item)

    def seq(self):
        if not len(self):
            return None
        return IndexableSeq(self, 0)
