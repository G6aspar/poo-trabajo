class PetDAO:
    def add_pet(self, pet):
        raise NotImplementedError

    def update_pet(self, pet):
        raise NotImplementedError

    def delete_pet(self, name):
        raise NotImplementedError

    def get_pet(self, name):
        raise NotImplementedError

    def get_all_pets(self):
        raise NotImplementedError

class PetDAOImpl(PetDAO):
    def __init__(self):
        self.pets = []

    def add_pet(self, pet):
        self.pets.append(pet)

    def update_pet(self, pet):
        for i, p in enumerate(self.pets):
            if p.name == pet.name:
                self.pets[i] = pet

    def delete_pet(self, name):
        self.pets = [p for p in self.pets if p.name != name]

    def get_pet(self, name):
        for pet in self.pets:
            if pet.name == name:
                return pet
        return None

    def get_all_pets(self):
        return self.pets
