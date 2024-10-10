import random
import math

def greet():
  print("Czar")
greet()

def greetWithName(name):
  print(f"Hello {name}")

greetWithName("Fortune")

def greetWithLocation(name, location):
  print(f"Hello {name}")
  print(f"What is it like in {location}")
greetWithLocation(name="Fortune", location="Norway")



# def primeChecker(number):
#   if (number 

def paintCalc(height, width, cover):
  numCans = (height * width) / cover
  roundUpCans = math.ceil(numCans)
  print(f"You'll need {roundUpCans} cans of paint.")

test_h = int(input("Height of Wall"))
test_w = int(input("Width of Wall"))
coverage = 5

paintCalc(height=test_h, width=test_w, cover=coverage)