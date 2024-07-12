class PetValidationStrategy:
    def validate(self, pet):
        raise NotImplementedError

class NameValidationStrategy(PetValidationStrategy):
    def validate(self, pet):
        return bool(pet.name)

class TypeValidationStrategy(PetValidationStrategy):
    def validate(self, pet):
        return bool(pet.pet_type)

class AgeValidationStrategy(PetValidationStrategy):
    def validate(self, pet):
        return pet.age > 0
