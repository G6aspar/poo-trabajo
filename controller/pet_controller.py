class PetController:
    def __init__(self, pet_service):
        self.pet_service = pet_service

    def add_pet(self, pet):
        self.pet_service.add_pet(pet)

    def update_pet(self, pet):
        self.pet_service.update_pet(pet)

    def delete_pet(self, name):
        self.pet_service.delete_pet(name)

    def get_pet(self, name):
        return self.pet_service.get_pet(name)

    def get_all_pets(self):
        return self.pet_service.get_all_pets()
