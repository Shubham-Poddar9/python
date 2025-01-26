class parrot2:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def singing(self,song):
        return "{} is singing a {}song".format(self.name,song)
    def dancing(self):
        return"{} is now dancing".format(self.name)
a=parrot2("huuu",14)
print(a.singing("Beliver"))
print(a.dancing())