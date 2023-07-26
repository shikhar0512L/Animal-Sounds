class Animal:
    def make_sound(self):
        print("Generic animal sound")

class Dog(Animal):
    def make_sound(self):
        print("Bark")

class Cat(Animal):
    def make_sound(self):
        print("Meow")

def animal_sound_in_zoo(animal):
    animal.make_sound()

# Create instances of Dog and Cat classes
dog = Dog()
cat = Cat()

# Call the animal_sound_in_zoo() function with these instances
print("Sound of dog in the zoo:")
animal_sound_in_zoo(dog)

print("\nSound of cat in the zoo:")
animal_sound_in_zoo(cat)
