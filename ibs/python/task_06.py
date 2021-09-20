class Animal:
    def voice(self):
        pass


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
