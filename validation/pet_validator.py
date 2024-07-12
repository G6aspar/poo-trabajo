class PetValidator:
    def __init__(self):
        self.strategies = []

    def add_strategy(self, strategy):
        self.strategies.append(strategy)

    def validate(self, pet):
        return all(strategy.validate(pet) for strategy in self.strategies)
