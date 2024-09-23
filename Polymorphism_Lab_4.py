class ImageArea:
    def __init__(self, dai, rong):
        self.dai = dai 
        self.rong = rong
    def get_area(self):
        return self.dai * self.rong
    
    def __eq__(self, other):
        return self.get_area() == other.get_area()
    
    def __ne__(self, other):
        return self.get_area() != other.get_area()
    
    def __gt__(self, other):
        return self.get_area() > other.get_area()
    
    def __ge__(self, other):
        return self.get_area() >= other.get.area()
    
    def __lt__(self, other):
        return self.get_area() < other.get_area()
    
    def __le__(self, other):
        return self.get_area() <= other.get_area()
    
#testtttt
a1 = ImageArea(5 , 10)
a2 = ImageArea(25 , 2)
a3 = ImageArea(5 , 20)
print(a1 == a2)
print(a1 == a2)
print(a2 != a3)
