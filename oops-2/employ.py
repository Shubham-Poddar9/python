class employ:
    def __init__(self):
        print("Employ is created.")
    def __del__(self):
        print("Employ is deleted")
obj=employ()
del obj
print(obj)