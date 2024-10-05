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

for letter in chosenWord:
  if letter == guessedLetter:
    print("✅Right!")
  else:
    print("❌Wrong")
