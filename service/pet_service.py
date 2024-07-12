class PetService:
    def __init__(self, pet_dao):
        self.pet_dao = pet_dao

    def add_pet(self, pet):
        self.pet_dao.add_pet(pet)

    def update_pet(self, pet):
        self.pet_dao.update_pet(pet)

    def delete_pet(self, name):
        self.pet_dao.delete_pet(name)

    def get_pet(self, name):
        return self.pet_dao.get_pet(name)

    def get_all_pets(self):
        return self.pet_dao.get_all_pets()
