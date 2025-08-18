class person:
    def __init__(self, fname,lname):
        self.firstname = fname
        self.lastname = lname
    def greet(self):
       print(self.firstname, self.lastname)
class student(person):
    def __init__(self,fname,lname,year):
        super().__init__(fname, lname)
        self.graduationyear = year
x=student("John", "Doe", 2023)
x.greet()
print(x.graduationyear)