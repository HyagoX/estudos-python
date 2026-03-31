class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        with open('log.txt', 'a+') as archive:
            archive.write(f'New Person added:\n Name: {self.name}\n Age:{self.age}\n')
            archive.write('----------------------------------\n')

    def say_hi(self):
        return f'Hi, my name is {self.name}, and i am {self.age} years old!'

class Worker(Person):
    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.salary = salary
        with open('log.txt', 'a+') as archive:
            archive.write(f'New Worker added:\n Name: {self.name}\n Age: {self.age}\n Salary: {self.salary}\n')
            archive.write('----------------------------------\n')
    def say_hi(self):
        base_text = super().say_hi()
        return f'{base_text} And my actual salary is about ${self.salary}'

w1 = Worker('John', 18, 1512)
print(w1.say_hi())