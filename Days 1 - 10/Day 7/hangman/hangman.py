import random
import ui_elements
import words

#Improving UI: Day 7 Challenge 5
print(ui_elements.logo)

chosen_word = random.choice(words.word_list)
cw_char = list(chosen_word)
cw_length = len(chosen_word)

print(cw_char)
lives = 6 

# Iterating and Replacing the Blanks: Day 7 Challenge 2
skel_length = len(chosen_word)
skeleton = []
for skelement in range(skel_length):
    skeleton.append("_")
finish = False
while not finish: # Checking User's Victory : Day 7 Challenge 3
    # Checking User's Input: Day 7 Challenge 1
    guess = input("Guess a Letter: ").lower()
    if guess in chosen_word:
        print("You have already guessed it, shit doesn't work twice")
    for i in range(cw_length):
        letter = chosen_word[i]
        if guess == letter and '_' in skeleton:
            skeleton[i] = letter    
    print(skeleton)
    # Tracking User Lives : Day 7 Challenge 4
    if guess not in chosen_word or guess == "":
            lives -= 1
            print(f"The Letter is not in the word. \n{lives} tries remaining, think carefully")
            if lives == 0:
                finish = True
                print("You Lose")
    print(f"{' '.join(skeleton)}")
    if '_' not in skeleton:
        finish = True
        print("You Win")
    print(ui_elements.stages[lives])