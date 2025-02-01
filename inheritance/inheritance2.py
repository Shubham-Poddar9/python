class person:
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
    def display(self):
        print(self.fname,self.lname)
class student(person):
    def __init__(self,fname,lname,age):
        super().__init__(fname,lname)
        self.age=age
obj=student("shubham","Poddar",14)
obj.display()
print(obj.age)        