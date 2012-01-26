#!/usr/bin/env python

import readline
import sys

from py.clojure.lang.lispreader import read
from py.clojure.lang.fileseq import StringReader
from py.clojure.lang.globals import currentCompiler
import py.clojure.lang.rt as RT
from py.clojure.lang.compiler import Compiler


def main():
    with open("./clj/clojure/core.clj") as fl:
        r = StringReader(fl.read())

    RT.init()
    comp = Compiler()
    currentCompiler.set(comp)
    code = comp.standardImports()

    try:
        while True:
            s = read(r, True, None, True)

            try:
                res = comp.compile(s)
                comp.executeCode(res)
            except IOError as exp:
                print s
                raise exp

            while True:
                ch = r.read()

                if ch == "":
                    raise IOError()

                if ch not in [" ", "\t", "\n", "\r"]:
                    r.back()
                    break
    except IOError as e:
        pass

    if not sys.argv[1:]:
        while True:
            try:
                line = raw_input(comp.getNS().__name__ + "=> ")
            except EOFError:
                break

            if not line:
                continue

            while unbalanced(line):
                try:
                    line += raw_input('.' * len(comp.getNS().__name__) + '.. ')
                except EOFError:
                    break

            # Propogate break from above loop.
            if unbalanced(line):
                break

            r = StringReader(line)
            s = read(r, True, None, True)

            try:
                res = comp.compile(s)
                print comp.executeCode(res)
            except Exception:
                import traceback; traceback.print_exc()


def unbalanced(s):
    return (s.count('(') != s.count(')')
            or s.count('[') != s.count(']')
            or s.count('{') != s.count('}'))



if __name__ == "__main__":
    main()
