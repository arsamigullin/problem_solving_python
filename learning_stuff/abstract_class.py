import abc
from abc import ABC, abstractmethod

class A(ABC):
    def method(self):
        print('method')

    @abstractmethod
    def abstract_method(self):
        print('abstract_method')

class B(A):
    def abstract_method(self):
        print('abstract_method B')


class C(A):
    def abstract_method(self):
        print('abstract_method C')


if __name__ == '__main__':
    b = B()
    b.abstract_method()