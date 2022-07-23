import random

word_list = ["python", "java", "javascript", "golang", "kotlin", "react", "angular", "vue", "springboot", "maven"]

random_word = random.choice(word_list)

lives = 6

display = []
word_length = len(random_word)
for _ in range(word_length):
    display += "_"
print(display)

end_of_game = False

while not end_of_game:
    guess_word = input("Guess the word: ").lower()

    for position in range(word_length):
        letter = random_word[position]
        # print(f"Current position: {position} \n Current letter: {letter}\n"
        #       f"Guessed letter: {guess_word}")
        if letter == guess_word:
            display[position] = letter

    print(display)

    if guess_word not in random_word:
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose")

    print(f"{''.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You win.")


