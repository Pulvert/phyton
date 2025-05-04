class User:
    def __init__(self, first_name, last_name, id, age):
        self.first_name = first_name
        self.last_name = last_name
        self.id = id
        self.age = age
        self.p = Privileges()
    
    def describe_user(self):
        print(f"{self.first_name} {self.last_name}, nº ID: {self.id}, Years Old: {self.age}")

    def greet_user(self):
        print(f"Hello {self.first_name}!, welcome to our community")


class Privileges:
    def __init__(self):
        self.privileges  = "ola"


prueba = User("DIego", "Serrano", 1, 41)

print(prueba.age)

print(prueba.p.privileges)


