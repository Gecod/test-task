class Animal:
    inst_count = 0
    
    def __init__(self):
        Animal.inst_count += 1
        
    def voice(self):
        pass
    
    @classmethod
    def print_inst_count(cls):
        print(cls.inst_count)


class Cat(Animal):
    def voice(self):
        print('Meow')


class Dog(Animal):
    def voice(self):
        print('Woof')


class Cow(Animal):
    def voice(self):
        print('Moo')


tom = Cat()
tom.voice()

rex = Dog()
rex.voice()

betty = Cow()
betty.voice()

Animal.print_inst_count()
