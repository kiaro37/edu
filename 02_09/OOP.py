
# Публичный класс

class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hello(self):
        return f"Привет, я {self.name}, мне {self.age} лет"


u = User("Evgeniy", 20)
print(u.say_hello())

# Наследование классов

class User:
    def __init__(self, name):
        self.name = name

    def say_hello(self):
        return f"Hello {self.name}!"

class Admin(User):
    def say_hello(self):
        return f"Hello, i'm admin {self.name}"

admin = Admin("Evgeniy")
print(admin.say_hello())

# Инкапсуляция

class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance

acc = BankAccount(1000)
acc.deposit(500)
print(acc.get_balance())



class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        return f"Меня зовут {self.name}, мне {self.age} лет!"

class Employee(Person):
    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.__salary = salary

    def get_salary(self):
        return f"Я зарабатываю {self.__salary}"

    def work(self):
        return f"Я {self.name}, и я работаю"

emp = Employee("Евгений", 30, 100000)
print(emp.introduce())
print(emp.work())
print(emp.get_salary())