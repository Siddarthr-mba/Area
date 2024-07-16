
from abc import abstractmethod

class Shape:
    __type = ''   # The double underscore '__' defines a private member which an object cannot touch

    # __init__ is a special reserved method for a class which is called 'constructor'. This is called at the time of object creation
    def __init__(self):
        self.__type = self.__class__.__name__

    # annotation for an abstract method (a method without any implementation aka body)
    @abstractmethod
    def getArea(self):
        pass

    # Tip: have a def to access a private member/attribute
    def getType(self):
        return self.__type

    def whoAmI(self, args=[]):    # args is an optional parameter which is assigned a default value
        # return ('This is a {0} with area {1}'.format(args[0],args[1])) # Tip: This line is equal to the line below
        if args == []:
            return
        return ('This is a '+args[0]+' with area '+args[1])

class Circle(Shape):
    Radius:int = 0

    def __init__(self, *args):
        super().__init__()
        # Tip: Initialize your 'must-have' attributes as part of constructor always to enforce the requirement.
        args:list = list(args)
        self.Radius = args[0]

    def getArea(self):
        return 3.14 * self.Radius*self.Radius
    
class Rectangle(Shape):
    Length:int=0
    Breadth:int=0
    
    
    def __init__(self,*args):
        super().__init__()
        args = list(args)
        self.Length = args[0]
        self.Breadth= args[1]

    # def __init__(self,Length:int,Breadth:int):
    #     super().__init__()
    #     self.Length=Length
    #     self.Breadth=Breadth
        
    def getArea(self):
        return self.Length*self.Breadth
    
#class Trapezium(Shape):

 #   def __init__(self):
  #      super().__init__()
   # return

