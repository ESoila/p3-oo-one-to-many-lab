class Owner:
    def __init__(self, name):
        self.name = name
        self._pets = []

    def pets(self):
        """Returns a full list of the owner's pets."""
        return self._pets

    def add_pet(self, pet):
        """Adds a pet to the owner, ensures the pet is an instance of Pet."""
        if not isinstance(pet, Pet):
            raise Exception("The pet must be an instance of Pet.")
        if pet.owner is None: 
            pet.owner = self
        self._pets.append(pet)

    def get_sorted_pets(self):
        """Returns a sorted list of the owner's pets by their names."""
        return sorted(self._pets, key=lambda pet: pet.name)


class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []

    def __init__(self, name, pet_type, owner=None):
        if pet_type not in Pet.PET_TYPES:
            raise Exception(f"Invalid pet type. Choose from {', '.join(Pet.PET_TYPES)}.")
        self.name = name
        self.pet_type = pet_type
        self.owner = owner
        Pet.all.append(self)
        if self.owner:
            self.owner.add_pet(self)  

    def __repr__(self):
        return f"Pet(name={self.name}, type={self.pet_type})"

owner1 = Owner("John")


pet1 = Pet("Clifford", "dog", owner1) 
pet2 = Pet("Whiskers", "cat", owner1)

print(owner1.pets())  

print(owner1.get_sorted_pets()) 