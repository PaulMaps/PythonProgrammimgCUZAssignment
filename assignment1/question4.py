# Define the Dog class
class Dog:
    def make_sound(self):
        print("Woof!")

# Define the Cat class
class Cat:
    def make_sound(self):
        print("Meow!")

# Function that takes any object with a make_sound method
def process_sound(sound_object):
    sound_object.make_sound()

# Create objects
dog = Dog()
cat = Cat()

# Use the same function for both
process_sound(dog)  # Output: Woof!
process_sound(cat)  # Output: Meow!
