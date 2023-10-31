import os
import random
import linecache
from urllib import request
NUMBER_OF_VALID_WORDS = 854
NUMBER_OF_TRIES = 5
VICTORY = True
FILE_NAME = "words.txt"
URL = "https://raw.githubusercontent.com/Xethron/Hangman/master/words.txt"

random.seed()
if not os.path.isfile(FILE_NAME):
    request.urlretrieve(URL, FILE_NAME)


def main():
    running = True
    player_score = [0, 0]
    while running:
        target_word = generate_random_word()
        used_letters = []
        player_tries_left = NUMBER_OF_TRIES
        game_status = not VICTORY
        interface = []
        for i in range(len(target_word)):
            interface.append('-')

        while player_tries_left != 0 and game_status != VICTORY:
            print_interface(interface, used_letters)
            player_input = ''
            while len(player_input) != 1 or player_input in used_letters:
                player_input = input("Insert a letter ").upper()

            correct_answer = False
            for i in range(len(target_word)):
                if target_word[i] == player_input:
                    interface[i] = player_input
                    correct_answer = True
            if not correct_answer:
                player_tries_left -= 1
                print(f"\nWrong answer! \nTries left: {player_tries_left}\n")
            used_letters.append(player_input)

            if '-' not in interface:
                game_status = VICTORY

        if game_status == VICTORY:
            print("You won!\n")
            player_score[0] += 1
        else:
            print(f"\nYou lost! The solution was: {target_word}\n")
            player_score[1] += 1

        print(f"Score: {player_score[0]}-{player_score[1]}\n")
        continue_game = input("Press Q if you want to exit the game\n").upper()
        if continue_game == 'Q':
            running = False


def generate_random_word():
    """Returns a random word from the list of valid words"""
    random_line = random.randint(1, NUMBER_OF_VALID_WORDS)
    word = linecache.getline(FILE_NAME, random_line)
    return word.upper().strip('\n')


def print_interface(interface: list, used_letters: list):
    """Prints the interface of the game"""
    for element in interface:
        print(element, end="")
    print("\nUsed letters: ", used_letters, '\n')


if __name__ == "__main__":
    main()
