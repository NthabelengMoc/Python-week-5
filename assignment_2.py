class Animal:
    def __init__(self, name):
        self.name = name
       
    def move(self):
        pass  # To be overridden by subclasses
       
    def introduce(self):
        print(f"I am a {self.name}!")
       
class Dolphin(Animal):
    def move(self):
        print(f"{self.name} is swimming with jumps! 🐬")
    
    def communicate(self):
        print(f"{self.name} is clicking and whistling! 🔊")
       
class Owl(Animal):
    def move(self):
        print(f"{self.name} is flying silently! 🦉")
    
    def hunt(self):
        print(f"{self.name} turns its head 270 degrees looking for prey! 👀")
       
class Cheetah(Animal):
    def move(self):
        print(f"{self.name} is sprinting at high speed! 🐆")
    
    def rest(self):
        print(f"{self.name} is resting after a fast run! 😴")
       
class Penguin(Animal):
    def move(self):
        print(f"{self.name} is waddling and sliding on its belly! 🐧")
    
    def swim(self):
        print(f"{self.name} dives into the water and swims rapidly! 💦")

print("\n=== Animal Kingdom  ===")
animals = [
    Dolphin("Flipper"),
    Owl("Hedwig"),
    Cheetah("Chester"),
    Penguin("Rico")
]

for animal in animals:
    animal.introduce()
    animal.move()
    
    if isinstance(animal, Dolphin):
        animal.communicate()
    elif isinstance(animal, Owl):
        animal.hunt()
    elif isinstance(animal, Cheetah):
        animal.rest()
    elif isinstance(animal, Penguin):
        animal.swim()
    
    print()