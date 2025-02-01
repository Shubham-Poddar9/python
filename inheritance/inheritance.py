class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print(self.name,self.age)   
class employ(person):
    def __init__(self,name,age,salary):
        self.salary=salary
        person.__init__(self,name,age)
obj=employ("Shubham",14,"$31500")
obj.display()
print(obj.salary)