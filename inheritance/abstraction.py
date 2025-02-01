from abc import ABC
class animal(ABC):
    def move(self):
        pass
class human(animal):
    def move(self):
        print("Human can run")
class lion(animal):
    def move(self):
        print("Lion can also run")
class dog(animal):
    def move(self):
        print("dog can bark")
a=human()
a.move()
b=lion()
b.move()
c=dog()
c.move()