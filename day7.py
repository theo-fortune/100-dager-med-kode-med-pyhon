import random
word_list = ["Harvard", "Baboon", "Camel"]
listIndex = len(word_list)
print(f"The list index is: {listIndex}")
randomWordsIndex = random.randint(0, listIndex - 1)
print(f"The random word index is: {randomWordsIndex}")
chosenWord = word_list[randomWordsIndex]
#* chosenWord = random.choice(word_list)
print(f"The random word is: {chosenWord}")

guessedLetter = input("Guess a letter form the random word: ").lower()

display = []
for letter in chosenWord:
  display += "_"
print(display)

wordLength = len(chosenWord)
for position in range(wordLength):
  print(f"The position is: {position}")

if letter == guessedLetter:
  print("✅Right!")
else:
  print("❌Wrong")

print(display)

