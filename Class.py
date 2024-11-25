class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def greet(self):
        print(f"My name is{self.name},I am{self.age}years old.")
person1=person("ALice",30)
person1.greet()