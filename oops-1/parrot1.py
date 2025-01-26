class parrot1:
    species="bird"
    def __init__(self,name,age):
        self.name=name
        self.age=age
a=parrot1("Huuu",14)
b=parrot1("umum",14)
print("a is a",a.species)
print("b is a",b.species)
print(a.age,a.name)
print(b.age,b.name)