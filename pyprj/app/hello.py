from abc import ABCMeta, abstractmethod


class Hello(metaclass=ABCMeta):
    def __init__(self):
        self.msg = 'Hello'

    def say(self):
        print(self.msg)