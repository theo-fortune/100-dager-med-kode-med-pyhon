programming_dictionary = {
  "Bug": "An error in a program that prevents the program from running as expected.", 
  "Function": "A piece of code that you can easily call over and over again.",
}

#* Retrieving items from dictionary
# print(programming_dictionary["Bug"])

#* Adding new items to dictionary
programming_dictionary["Loop"] = "The action of doing something over and over and again"

print(programming_dictionary)

#* Create an empty dictionary.
emptyDictionary = {}

#* Wipe an existing dictionary
# programming_dictionary = {}

#* Edit an item in a dictionary
programming_dictionary["Bug"] = "The moth in your computer"
print(programming_dictionary)

#* Loop through a dictionary
for key in programming_dictionary:
  print(key)
  print(programming_dictionary[key])

studentScores = {
  "Harry": 81,
  "Samantha": 78,
  "Fortune": 99,
  "Mario": 74,
  "Nelly": 62,
}

scoresGrade = {}

newObject = {}
for key in studentScores:
  scores = studentScores[key]
  if (scores <= 70):
    scoresGrade[key] = "Fail"
  elif (scores > 70 and scores <= 80):
    scoresGrade[key] = "Acceptable"
  elif (scores > 80 and scores <= 90):
    scoresGrade[key] = "Exceeds Expectation"
  else:
    scoresGrade[key] = "Outstanding"
  print(studentScores[key])

print(scoresGrade)

country = input("What's the country name? ")
visits = input("How many times have you visited? ")
listOfVisits = input("What are the list of visits? ")

#* Nesting a Dictionary
travelLog = [
  {
    "country": "Norway",
    "citiesVisited": ["Bergen", "Lofoten", "Oslo"],
    "totalNumberOfVisits": 3 
  },
  {
    "country": "Finland",
    "citiesVisited": ["Helsinki", "Lapland", "Nyland"],
    "totalNumberOfVisits": 12
  }

]

# def addNewCountry(country, visits, list_of_cities):



# addNewCountry(country, visits, list_of_cities)
# print(f"I've been to {travelLog[2]['country']} {travelLog[2]['visits']} times.")
# print(f"My favorite city was {travelLog[2]['cities'][0]}.")