#!/usr/bin/env python3

import symbol   # nonterminals
import tokenize # terminals
import token    # terminals
import keyword  # .iskeyword()

@decorated
class foo(object):

    def __init__(self, arg):
        self.arg = arg

    def __call__(self, fn):
        """do stuff."""
        return fn        
        
class DefinitionParameters(object):

    @classmethod
    @foo('foo')
    def matches_terminal(cl, node):
        return node.parent and \
               node.parent.identifier == symbol.tfpdef and \
               node.index == 0

