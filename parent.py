class person:
    def __init__(self, name, idnumber):
        self.name = name
        self.idnumber = idnumber

    def display(self):
        print(f"Name: {self.name}, ID: {self.idnumber}")
class employee(person):
    def __init__(self, name, idnumber, salary,post):
        self.post = post
        self.salary = salary
        person.__init__(self, name, idnumber)
a=employee("John Doe", "12345", 50000, "Software Engineer")
a.display()