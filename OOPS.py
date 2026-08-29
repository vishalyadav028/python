# class maths_bca: 
#     def addition(self,a, b=0, c=0, d=0,): 
#         print(a+b+c)

# m1=maths_bca()
# m1.addition(2,)      


class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sound(self):
        print(f"{self.name} sound is - woof")

class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sound(self):
        print(f"{self.name} sound is - meow")

d1 = Dog(name="tom", age=3)
c1 = Cat(name="jerry", age=1)

d1.sound()
c1.sound()