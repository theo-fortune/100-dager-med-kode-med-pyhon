# !String 
# print("Hello"[4])

# !Integer
print(123_456_789)

# !Float
3.142

# !Boolean
True
False

# num_char = len(input("What's your name?"))
# print(type(num_char))
# !print("your name has " + str(num_char) + " characters")

# two_digit_number = input()

# first_digit = int(two_digit_number[0])
# second_digit = int(two_digit_number[1])

# *Add the two integers together

# two_digit_number = first_digit + second_digit
# print(two_digit_number)
# print(3 + 3 / 3 * 3 - 3)

# height = input();
# weight = input();

# bmi = int(weight) / (float(height) ** 2) 
# print(int(bmi))

result = 8 / 3
# print(type(result))

score = 3

#* User scores a point
score += 1
print(score)

height = 1.85
isWinning = True

print(f"Your score is {score}, your height is {height}, you are winning is {isWinning}")

age = int(input())
weeks_in_a_year = 52
year90 = 90 * weeks_in_a_year
weeks_lived = age * weeks_in_a_year
weeks_remaining = year90 - weeks_lived
message = f"you are {age} years old and you've lived {weeks_lived} weeks, you have {weeks_remaining} left"
print(message)