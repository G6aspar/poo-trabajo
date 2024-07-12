class PetHandler:
    def __init__(self):
        self.next_handler = None

    def set_next_handler(self, handler):
        self.next_handler = handler

    def handle(self, pet):
        raise NotImplementedError

class PetCreationHandler(PetHandler):
    def handle(self, pet):
        if pet:
            print(f"Pet created: {pet}")
            if self.next_handler:
                self.next_handler.handle(pet)

class PetNotificationHandler(PetHandler):
    def handle(self, pet):
        print(f"Notification sent for pet: {pet}")
        if self.next_handler:
            self.next_handler.handle(pet)
