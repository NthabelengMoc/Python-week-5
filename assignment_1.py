class Superhero:
    def __init__(self, name, secret_identity, powers, energy):
        self.name = name
        self.secret_identity = secret_identity
        self.powers = powers
        self.energy = energy
       
    def use_power(self, power):
        if power in self.powers:
            print(f"{self.name} used {power}!")
            self.energy -= 10
        else:
            print(f"{self.name} doesn't have the power {power}.")
           
    def recharge(self, amount):
        self.energy += amount
        print(f"{self.name} recharged {amount} energy!")
       
    def introduce(self):
        print(f"Hi, I'm {self.name}, also known as {self.secret_identity}.")
        print(f"I have the following powers: {', '.join(self.powers)}.")
        print(f"My current energy level is {self.energy}.")

class Villain(Superhero):
    def __init__(self, name, secret_identity, powers, energy, evil_plan):
        super().__init__(name, secret_identity, powers, energy)
        self.evil_plan = evil_plan
       
    def execute_plan(self):
        print(f"{self.name} is executing the evil plan: {self.evil_plan}!")
       
    def introduce(self):
        super().introduce()
        print(f"My evil plan is: {self.evil_plan}")
       
print("***** Batman vs Joker Demonstration *****")

batman = Superhero("Batman", "Bruce Wayne", ["Martial Arts", "Intelligence", "Gadgets"], 100)
batman.introduce()
batman.use_power("Gadgets")
batman.recharge(20)

print("\n" + "-"*40 + "\n")

joker = Villain("Joker", "Unknown", ["Chemical Weapons", "Psychological Manipulation"], 80, "Spread chaos in Gotham City")
joker.introduce()
joker.use_power("Psychological Manipulation")
joker.execute_plan()

print("\n" + "-"*40 + "\n")
print("Batman confronts the Joker!")
batman.use_power("Intelligence")
joker.use_power("Chemical Weapons")
print(f"Batman's energy: {batman.energy}")
print(f"Joker's energy: {joker.energy}")
