from exceptions import AbstractMethodCall


class IDeref(object):
    def deref(self):
        raise AbstractMethodCall()