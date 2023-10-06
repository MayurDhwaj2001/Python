from abc import ABC, abstractmethod


class Computer(ABC):
    @abstractmethod
    def process(self):
        pass


class Laptop:
    def process(self):
        print("Processing...")


c1 = Laptop()
c1.process()
