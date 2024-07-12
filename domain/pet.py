class Pet:
    def __init__(self, name, pet_type, age):
        self.name = name
        self.pet_type = pet_type
        self.age = age

    def __str__(self):
        return f"Pet(name={self.name}, type={self.pet_type}, age={self.age})"