fruits = ["Apple", "Peach", "Pear"]
for fruit in fruits:
  print(fruit)

for number in range(1, 10):
  print(number)

total = 0
target = int(input("What's your number ")) + 1
for even in range(0, target, 2):
  print(even)
  total += even
print(total)
