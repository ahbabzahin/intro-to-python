class Robot:
    def __init__(self, name, model, purpose):
        self.name = name
        self.model = model
        self.purpose = purpose

    def introduce_self(self):
        print(f"Greetings, my name is {self.name}.")
        print(f"I am a {self.model} model robot.")
        print(f"My primary purpose is to {self.purpose}.")

class MedicalRobot(Robot):
    def __init__(self, name, model, purpose, specialty):
        super().__init__(name, model, purpose)
        self.specialty = specialty

    def introduce_self(self):
        super().introduce_self()
        print(f"My specialty is {self.specialty}.")

my_robot = Robot("Robo-1", "Humanoid", "assist with household tasks")
my_robot.introduce_self()
print("-" * 20)

my_medical_robot = MedicalRobot("Medi-Bot", "Surgical-3000", "perform complex surgeries", "neurosurgery")
my_medical_robot.introduce_self()