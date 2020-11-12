class Animal:
    def __init__(self,name,age,color):
        #properties
        self.__name=name #private property
        self.age=age
        self.color=color

    def getName(self): #getter
        return self.__name

    def setName(self,newName): #setter
        self.__name=newName


class Horse(Animal): #derived from Animal class

    def __init__ (self,name,age,color,height,speed):
        super().__init__(name,age,color)
        self.__height=height
        self.__speed=speed
    def getHeight(self): #getter
        return self.__height

    def getSpeed(self): #getter
        return self.__speed

    def setHeight(self,newHeight): #setter
        self.__height=newHeight

    def setSpeed(self,newSpeed): #setter
        self.__speed=newSpeed
