from abc import ABC,abstractmethod
from Car import Car

class Builder:
    car = None

    @abstractmethod
    def setModel(self):
        pass

    @abstractmethod
    def buildBody(self):
        pass

    @abstractmethod
    def buildEngine(self):
        pass
        
        
    @abstractmethod
    def buildWheels(self):
        pass

    @abstractmethod
    def buildFeatures(self):
        pass

    @abstractmethod
    def buildOptionalFeatures(self):
        pass

    @abstractmethod
    def getCar(self) -> Car:
        pass