class computer:
    def __init__(self):
        self.__maxprice=315
    def display(self):
        print(self.__maxprice)
    def setmaxprice(self,newprice):
        self.__maxprice=newprice

obj=computer()
obj.display()
obj.__maxprice=400
obj.display()
obj.setmaxprice(4000)
obj.display()