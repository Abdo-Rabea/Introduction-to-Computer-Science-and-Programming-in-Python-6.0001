# 6.0001 Problem Set 3
#
# The 6.0001 Word Game
# Created by: Kevin Luu <luuk> and Jenna Wiens <jwiens>
#
# Name          : <your name>
# Collaborators : <your collaborators>
# Time spent    : <total time>

import math
import random
import string

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10, '*':0
}

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.append(line.strip().lower())
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def get_frequency_dict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """
    
    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq
	

# (end of helper code)
# -----------------------------------

#
# Problem #1: Scoring a word
#
def get_word_score(word, n):
    """
    Returns the score for a word. Assumes the word is a
    valid word.

    You may assume that the input word is always either a string of letters, 
    or the empty string "". You may not assume that the string will only contain 
    lowercase letters, so you will have to handle uppercase and mixed case strings 
    appropriately. 

	The score for a word is the product of two components:

	The first component is the sum of the points for letters in the word.
	The second component is the larger of:
            1, or
            7*wordlen - 3*(n-wordlen), where wordlen is the length of the word
            and n is the hand length when the word was played

	Letters are scored as in Scrabble; A is worth 1, B is
	worth 3, C is worth 3, D is worth 2, E is worth 1, and so on.

    word: string
    n: int >= 0
    returns: int >= 0
    """
    word=word.lower()
    sum_points = 0
    greater =7 * len(word) - 3 * ( n-len(word))
    for letter in word:
        sum_points+=SCRABBLE_LETTER_VALUES[letter]
    if  greater > 1:
        return greater * sum_points
    else:
        return sum_points
    
    
        
      # TO DO... Remove this line when you implement this function

#
# Make sure you understand how this function works and what it does!
#
def display_hand(hand):
    """
    Displays the letters currently in the hand.

    For example:
       display_hand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
       a x x l l l e
    The order of the letters is unimportant.

    hand: dictionary (string -> int)
    """
    
    for letter in hand.keys():
        for j in range(hand[letter]):
             print(letter, end=' ')      # print all on the same line
    print()                              # print an empty line

#
# Make sure you understand how this function works and what it does!
# You will need to modify this for Problem #4.
#
def deal_hand(n):
    """
    Returns a random hand containing n lowercase letters.
    ceil(n/3) letters in the hand should be VOWELS (note,
    ceil(n/3) means the smallest integer not less than n/3).

    Hands are represented as dictionaries. The keys are
    letters and the values are the number of times the
    particular letter is repeated in that hand.

    n: int >= 0
    returns: dictionary (string -> int)
    """
    
    hand={}
    num_vowels = int(math.ceil(n / 3))

    for i in range(num_vowels-1):
        x = random.choice(VOWELS)
        hand[x] = hand.get(x, 0) + 1
    hand["*"]=1
    for i in range(num_vowels, n):    
        x = random.choice(CONSONANTS)
        hand[x] = hand.get(x, 0) + 1
    
    return hand

#
# Problem #2: Update a hand by removing letters
#
def update_hand(hand, word):
    """
    Does NOT assume that hand contains every letter in word at least as
    many times as the letter appears in word. Letters in word that don't
    appear in hand should be ignored. Letters that appear in word more times
    than in hand should never result in a negative count; instead, set the
    count in the returned hand to 0 (or remove the letter from the
    dictionary, depending on how your code is structured). 

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)    
    returns: dictionary (string -> int)
    """
    word=word.lower()
    hand2={}
    hand1=hand.copy()    
    for letter in word:
        hand1[letter]=hand1.get(letter,0)-1
        
    for letter in hand1.keys():
        if hand1[letter] >0:
            hand2[letter]=hand1[letter]  # TO DO... Remove this line when you implement this function
    return hand2
#
# Problem #3: Test word validity

def is_valid_word(word, hand, word_list):
    """
    Returns True if word is in the word_list and is entirely
    composed of letters in the hand. Otherwise, returns False.
    Does not mutate hand or word_list.
   
    word: string
    hand: dictionary (string -> int)
    word_list: list of lowercase strings
    returns: boolean
    """
    hand1=hand.copy()
    word=word.lower()
    for letter in word:
        if letter in hand1.keys():
            hand1[letter]-=1
            if hand1[letter]==0:
                del(hand1[letter])
        else:
            return False
        
    if word.find("*") != -1:
        for l in VOWELS:
            new_word=word.replace("*",l)
            if new_word in word_list:
                return True
    if word in word_list:
        return True
    else:
        return False
#
# Problem #5: Playing a hand
#
def calculate_handlen(hand):
    """ 
    Returns the length (number of letters) in the current hand.
    
    hand: dictionary (string-> int)
    returns: integer
    """
    handlen=0
    for letter in hand.keys():
        handlen+=hand[letter]
    return handlen
    
def play_hand(hand, word_list):

    Total=0
    hand1=hand.copy()
    word="c"
    while True:
    
        print("\nCurrent Hand:",end=" ")
        display_hand(hand1)
        
        word=input("Enter word, or !! to indicate that you are finished: ")
        if word == "!!":
            print("Total score of this hand:",Total,"points\n-----------")
            return Total
            break
        

        if is_valid_word(word,hand1,word_list):
            Total+=get_word_score(word,calculate_handlen(hand1))
            print("\""+word+"\" earned "+str(get_word_score(word,calculate_handlen(hand1)))+" points. Total: "+str(Total)+" points")
        else:
            print("That is not a valid word.",end=" ")
            if calculate_handlen(update_hand(hand1,word))==0:
                print("\nRan out of letters.\nTotal score of this hand:",Total,"points\n-----------")
                return Total
                break
            else:
                print("Please choose another word.")
        hand1=update_hand(hand1,word)
        if calculate_handlen(hand1) == 0:
            print("Ran out of letters.\nTotal score of this hand:",Total,"points\n-----------")
            return Total
            break
   


def substitute_hand(hand, letter):
    """ 
    Allow the user to replace all copies of one letter in the hand (chosen by user)
    with a new letter chosen from the VOWELS and CONSONANTS at random. The new letter
    should be different from user's choice, and should not be any of the letters
    already in the hand.

    If user provide a letter not in the hand, the hand should be the same.

    Has no side effects: does not mutate hand.

    For example:
        substitute_hand({'h':1, 'e':1, 'l':2, 'o':1}, 'l')
    might return:
        {'h':1, 'e':1, 'o':1, 'x':2} -> if the new letter is 'x'
    The new letter should not be 'h', 'e', 'l', or 'o' since those letters were
    already in the hand.
    
    hand: dictionary (string -> int)
    letter: string
    returns: dictionary (string -> int)
    """

    hand1=hand.copy()
    if letter not in hand.keys():
        return hand
    else:
        alpha=CONSONANTS+VOWELS
        while(True):
            new_letter = random.choice(alpha)
            if new_letter not in hand.keys():
                hand1[new_letter]=hand1[letter]
                del(hand1[letter])
                return hand1
                break
                
       
    
def play_game(word_list):
    """
    Allow the user to play a series of hands

    * Asks the user to input a total number of hands

    * Accumulates the score for each hand into a total score for the 
      entire series
 
    * For each hand, before playing, ask the user if they want to substitute
      one letter for another. If the user inputs 'yes', prompt them for their
      desired letter. This can only be done once during the game. Once the
      substitue option is used, the user should not be asked if they want to
      substitute letters in the future.

    * For each hand, ask the user if they would like to replay the hand.
      If the user inputs 'yes', they will replay the hand and keep 
      the better of the two scores for that hand.  This can only be done once 
      during the game. Once the replay option is used, the user should not
      be asked if they want to replay future hands. Replaying the hand does
      not count as one of the total number of hands the user initially
      wanted to play.

            * Note: if you replay a hand, you do not get the option to substitute
                    a letter - you must play whatever hand you just had.
      
    * Returns the total score for the series of hands

    word_list: list of lowercase strings
    """
    total_score=0
    temp_score2=0
    n="don't replay"
    n_hands=int(input("Enter total number of hands: "))
    while n_hands:
        if n!="replay":
            hand=deal_hand(HAND_SIZE)
        hand1=hand.copy()
        print("current hand: ",end="")
        display_hand(hand1)
        print()
        if input("Would you like to substitute a letter? ") == "yes":
            rep_letter=input("Which letter would you like to replace: ")
            hand1 = substitute_hand(hand1, rep_letter)
        #play hand
        temp_score=play_hand(hand1, word_list)
        if n!="replay":
            if input("Would you like to replay the hand? ")=="yes":
                n="replay"
                temp_score2=temp_score
                continue
        n_hands-=1
        n="don't replay"
        if temp_score>=temp_score2:   
            total_score+=temp_score
        else:
            total_score+=temp_score2
        temp_score2=0
    print("Total score over all hands:",total_score)
    
    


#
# Build data structures used for entire session and play game
# Do not remove the "if __name__ == '__main__':" line - this code is executed
# when the program is run directly, instead of through an import statement
#

if __name__ == '__main__':
    word_list = load_words()
    #play_hand(test_hand, word_list)
    play_game(word_list)
