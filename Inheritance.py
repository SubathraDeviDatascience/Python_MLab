class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def greet(self):
        print(f"My name is {self.name},I am {self.age} years old.")
class student(person):
    def __init__(self,name,age,student_id):
        super().__init__(name,age)
        self.student_id=student_id
    def display(self):
        print(f"My student_id is {self.student_id}")
student1=student("bob",30,123)
student1.greet()
student1.display()