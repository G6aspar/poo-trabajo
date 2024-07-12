from domain.pet import Pet
from dao.pet_dao import PetDAOImpl
from service.pet_service import PetService
from controller.pet_controller import PetController
from validation.pet_validation_strategy import NameValidationStrategy, TypeValidationStrategy, AgeValidationStrategy
from validation.pet_validator import PetValidator
from handler.pet_handler import PetCreationHandler, PetNotificationHandler

if __name__ == "__main__":
    pet_dao = PetDAOImpl()
    pet_service = PetService(pet_dao)
    pet_controller = PetController(pet_service)

    pet_validator = PetValidator()
    pet_validator.add_strategy(NameValidationStrategy())
    pet_validator.add_strategy(TypeValidationStrategy())
    pet_validator.add_strategy(AgeValidationStrategy())

    creation_handler = PetCreationHandler()
    notification_handler = PetNotificationHandler()
    creation_handler.set_next_handler(notification_handler)

    pet = Pet("CON BOTAS", "GATO", 3)

    if pet_validator.validate(pet):
        pet_controller.add_pet(pet)
        creation_handler.handle(pet)
    else:
        print("Pet validation failed.")
