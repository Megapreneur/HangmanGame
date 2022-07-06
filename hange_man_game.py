import random

word_list = ["python", "java", "javascript", "golang", "kotlin", "react", "angular", "vue"]

random_word = random.choice(word_list)

display = []
word_length = len(random_word)
for _ in range(word_length):
    display += "_"
print(display)

guess_word = input("Guess the word: ").lower()

for position in range(word_length):
    letter = random_word[position]
    if letter == guess_word:
        display[position] = letter


print(display)


