#import modules needed to run the program
import random
import hangman_art as art
import hangman_words as words
from replit import clear

#get the program to generate a random word from word list and create a display to receive correct guesses. 
#set the display to contain the same num of placeholder spaces as the randomly generated word.
generated_word = random.choice(words.word_list)
display = []
for i in range(len(generated_word)):
  display.append("_")

# determine the number of lives the user has
lives = 6

#create a loop function to iterate through guesses and match correct guesses with the letters in the generated word

print(art.logo)
print(generated_word)
end_of_game = False
while not end_of_game:
  guess = input("Guess a letter: ")
  clear()
  if guess in display:
      print(f"You have guessed {guess} before.")
  #check guess letter against word  
  for position in range(len(generated_word)):
    letter = generated_word[position]
    if letter == guess:
      display[position] = guess    
  #check if guess is wrong
  if guess not in generated_word:
    lives -= 1
    print(f"{guess} is not in word. You have lost a life. You have {lives} lives left")
    if lives == 0:
      print("You are out of lives.")
      end_of_game = True    
  # Check if all guess have been made accurately 
  if "_" not in display:
    print("You have accurately guessed the word. You win.")
    end_of_game = True
    
  print(''.join(display))
  print(art.stages[lives])
  
  