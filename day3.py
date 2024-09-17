a = 12
print(a > 10)

print("Welcome to the rollercoaster!")
height = int(input("What's your height in CM? "))
bill = 0

if height >= 120:
  print("You can ride the rollercoaster")
  age = int(input("What is your age? "))
  if age < 12:
    bill = 5
    print(f"Please pay ${bill}.")
  if age <= 18:
    bill = 7
    print(f"Please pay ${bill}.")
  else:
    bill = 12
    print(f"Please pay ${bill}.")

  wants_photo = input("Do you want a photo taken? Y or N ")
  if wants_photo == "Y":
    bill += 3
    print(f"Your final bill is {bill}")
  else:
    print(f"Your final bill is {bill}")
else:
  print("Sorry, you have to grow taller before you can ride.")

#* Coding Challenge
number = int(input())

if (number % 2 == 0):
  print(f"{number} is an even number")
else:
  print(f"{number} is an odd number")

year = int(input())

if (year % 4 == 0):
  print("Leap Year")
else:
  print("Year")

