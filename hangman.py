import random
print("Welcome to the hangman game!")

words_categories = {
    "Europe cities" : ["Riga", "Talinn", "Vilnius", "Warsaw", "Berlin", "Zagreb", "Brussels", "Andorra", "Vatican City", "Sarajevo"],
    "Food" : ["chicken", "bread", "milk", "tomato", "grapes", "eggs", "cheese", "peanut butter and jam sandwich", "apple", "carrot"],
    "Animals" : ["cat", "butterfly", "guinea Pig", "tarantula", "dog", "shark", "lobster", "narwhal", "manatee", "seahorse"]
    }
categories = input("Choose  a category (Europe cities), (Food), (Animals): ")
chosen_list = words_categories[categories]

hangman = [
    """
       +---+
       |   |
           |
           |
           |
           |
    =========
    """,
    """
      +---+
      |   |
      o   |
          |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      o   |
      |   |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      o   |
     /|   |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      o   |
     /|\  |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      o   |
     /|\  | 
     /    |
          |
    =========
    """,
    """
      +---+
      |   |
      o   |
     /|\  |
     / \  |
          |
    =========
    """
]

max_index = len(chosen_list) - 1 # length of a list
random_index = random.randint(0, max_index)
random_word = chosen_list[random_index] # 0 1 2 3


fails = 0
guessed_letters = [' ']

while fails < 6:

    word = "" 
    for char in random_word: 
        if char in guessed_letters: 
            word += char 
        else:
            word += "-" 

    
    print(hangman[fails])
    print(f"You have {6 - fails} tries left.")
    print("Guessed letters:", guessed_letters)
    print(word.capitalize())

    if word == random_word:
        print ("You won!")
        break

    letter = input("Enter your letter: ").lower()
    guessed_letters.append(letter)

    if letter in random_word:
        print("Letter is in the word!")
    else:
        print("Letter is not in the word!")
        fails += 1

if fails == 6:
    print(hangman[6])
    print("You lose!")