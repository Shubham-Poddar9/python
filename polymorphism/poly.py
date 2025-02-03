class cat:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def info(self):
        print("The name of cat is ",self.name)
        print("the age of cat is",self.age)
    def sound(self):
        print("The sound of cat is meou")

class dog:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def info(self):
        print("The name of dog is ",self.name)
        print("the age of dog is",self.age)
    def sound(self):
        print("The sound of dog is bhou")


a=cat("kitty",3)
b=dog("tyson",6)
for i in(a,b):
    i.info()
    i.sound()