class libary:
    def __init__(self,list_of,name):
        self.list_of=list_of
        self.name=name
        self.lendict={}
    def display(self):
        print("Welcome to the libary",self.name)
        print("We have these books")
        for i in self.list_of:
            print(i )
    def lend_book(self,uname,book):
        if book not in self.list_of:
            print("sorry the book is not aviable")
        elif(book in self.lendict):
            print("book is taken")
        else:
            self.lendict[book]=uname
            print("You can take the book now")
            self.list_of.remove(book)
    def addBook(self, book):
         self.list_of.append(book) 
         print("{book) has been added to the book list.")
if __name__ == "__main__":
    obj=libary(["Matilda","Charlie and chocolate factory","James and the jaint peach","Harry potter"],"lets upskill")
    username=input("Please enter your name")

    while True:
        print( f"\nHello {username}, welcome to the {obj.name} library. Please choose an option:")
        print("1 for display books 2 for lend book 3 for add book")
        userchoice=input("Please any option")
        if userchoice not in["1","2","3"]:
            print("Please enter a valid option")
            continue
        if userchoice == "1":
            obj.display()
        elif userchoice =="2":
            book=input("Enter the book name")
            obj.lend_book(username,book)
        elif userchoice =="3":
            book=input("Enter the book name")
            obj.addBook(book)

            
      

              