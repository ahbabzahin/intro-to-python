class cat:
    def __init__(self, name,age):
        self.name = name
        self.age=age

    def speak(self):
        print(f"i am a cat, my name is {self.name} and I am {self.age} years old")
    def make_sound(self):
        print("Meow!")
class dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        print(f"i am a dog, my name is {self.name} and I am {self.age} years old")
    def make_sound(self):
        print("Woof!")
cat1=cat("Whiskers", 3  )
dog1=dog("Buddy", 5)
for animal in (cat1, dog1):
    animal.make_sound()
    animal.speak()
