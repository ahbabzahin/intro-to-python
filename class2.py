class student():
    grade=10
    name='zahin'

    def introduction(self):
        print('I am a student')
    def details(self):
        print('my name is ',self.name)
        print('i read in grade ',self.grade)
    
ob1 = student()
ob1.introduction()
ob1.details()