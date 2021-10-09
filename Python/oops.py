#in classes, variables are called attributes and functions are called methods
#classes are a blueprint of creating an object. Class has no memory.
#An object is an instance of a class. When an object is created, memory is allocated to it

class test:
    def __init__(self):  #self parameter is a reference to the current instance (object). it can be called anything, but it has to be the first parameter.
        self.name = ''
        self.marks = ''
    def printvalues(self):
        print(self.name)
        print(self.marks)
    def getvalues(self):
        self.name = input()
        self.marks = input()

# var = test()
# var.printvalues()  #prints the value set by __init__()
# var.getvalues()    #updates the values of the objects attributes
# var.printvalues()

#Example to understand classes better
class Complex:
    def __init__(self,num,imag):
        self.num = num
        self.imag = imag
    def sum(self,obj):
        real = self.num + obj.num
        imag = self.imag + obj.imag
        ans = Complex(real, imag)
        return ans
inst1 = Complex(11, 5)
inst2 = Complex(4, 3)
result = inst1.sum(inst2)
print(result.num)
print(result.imag)

#inheritance
''' It allows us to inherit attributes  and methods from parent class to child classes'''
class parent:
    def __init__(self):
        print("I am parent class init")
    def parentprint(self):
        print('Parent function')

class child(parent):
    def __init__(self):
        print('I am child class init')
        super().parentprint() #super() acts as a object of parent class, here we are calling a method of parent class
        
obj = child()