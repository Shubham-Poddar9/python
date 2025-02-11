class Robot:
    def __init__(self, name, model, color):
        self.name = name
        self.model = model
        self.color = color

    def introduce(self):
        print(f"Hello! I am {self.name}.")
        print(f"I am a {self.model} model.")
        print(f"My color is {self.color}.")

    def perform_task(self, task):
        print(f"{self.name} is now performing: {task}")


my_robot = Robot('RoboMax', 'X500', 'Silver')
my_robot.introduce()
my_robot.perform_task('cleaning the house')
