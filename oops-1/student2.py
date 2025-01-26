class student2:
    a=9
    b="Shubham"
    def intro(self):
        print("Hi I am a student")
    def details(self):
        print("My name is ",self.b)
        print("My grade is",self.a)
object=student2()
object.intro()
object.details()