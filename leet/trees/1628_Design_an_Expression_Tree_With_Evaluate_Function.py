import abc
from abc import ABC, abstractmethod
import operator as op
from typing import List

"""
This is the interface for the expression tree Node.
You should not remove it, and you can define some classes to implement it.
"""


class Node(ABC):
    @abstractmethod
    def evaluate(self) -> int:
        pass


class NumberNode(Node):

    def __init__(self, val):
        self.val = val

    def evaluate(self):
        return self.val


class OperatorNode(Node):
    ops = {'+': op.add, '-': op.sub, '*': op.mul, '/': op.truediv}

    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def evaluate(self):
        return int(OperatorNode.ops[self.val](self.left.evaluate(), self.right.evaluate()))


"""    
This is the TreeBuilder class.
You can treat it as the driver code that takes the postinfix input
and returns the expression tree represnting it as a Node.
"""

"""    
This is the TreeBuilder class.
You can treat it as the driver code that takes the postinfix input
and returns the expression tree represnting it as a Node.
"""


class TreeBuilder(object):
    def buildTree(self, postfix: List[str]) -> 'Node':
        stack = []
        for ch in postfix:
            if ch.isnumeric():
                stack.append(NumberNode(int(ch)))
            else:
                node = OperatorNode(ch)
                node.right = stack.pop()
                node.left = stack.pop()
                stack.append(node)
        return stack[0]


"""
Your TreeBuilder object will be instantiated and called as such:
obj = TreeBuilder();
expTree = obj.buildTree(postfix);
ans = expTree.evaluate();
"""
