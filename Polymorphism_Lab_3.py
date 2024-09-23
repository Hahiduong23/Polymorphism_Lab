import math
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def dien_tich(self):
        pass
    def chu_vi(self):
        pass

class Tron(Shape):
    def __init__(self, R):
        self.__R = R
    def dien_tich(self):
        return 3.14 * self.__R ** 2
    def chu_vi(self):
        return 2 * 3.14 *self.__R
class Chu_Nhat(Shape):
    def __init__(self, dai, rong):
        self.__dai = dai
        self.__rong = rong
    def dien_tich(self):
        return self.__dai * self.__rong
    def chu_vi(self):
        return (self.__dai + self.__rong) * 2
tron = Tron(5)
print(tron.dien_tich())
print(tron.chu_vi())
chu_nhat = Chu_Nhat(5,10)
print(chu_nhat.dien_tich())
print(chu_nhat.chu_vi())


     