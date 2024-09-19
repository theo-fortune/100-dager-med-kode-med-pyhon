import random
import maths

random_integer = random.randint(1, 10)
print(random_integer)

print(maths.pi)

random_float = random.random() * 5
print(random_float)

heads = 0
tails = 1

rand = random.randint(heads, tails)
print(rand)

if rand == 0:
  print("Heads")
else:
  print("Tails")

cars = ["BMW-X6", "Lamborghini Lanzador", "Audi R8", "Mercedes Benz G Class", "Porsche Cayenne", "Tesla CyberTruck"]
cars[-1] = "Tesla Model Y"
cars.append("Lotus Emira")
cars.extend(["Lucid Air Sapphire", "GMC Hummer EV Pickup"])
print(cars[-1])
print(cars)

print(len(cars))

foodAvailable = ["Strawberries", "Spinach", "Kale", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears", "Tomatoes", "Celeries", "Potatoes"]

fruits = ["Strawberries",  "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
veggies = ["Tomatoes", "Celeries", "Potatoes" "Spinach", "Kale"]