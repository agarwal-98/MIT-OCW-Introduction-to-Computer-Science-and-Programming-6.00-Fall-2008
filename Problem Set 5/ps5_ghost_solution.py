# # Problem Set 5: Ghost
# # Name: 
# # Collaborators: 
# # Time: 
# #

import random

# # -----------------------------------
# # Helper code
# # (you don't need to understand this helper code)
import string

WORDLIST_FILENAME = "words.txt"

def load_words():
	"""
	Returns a list of valid words. Words are strings of lowercase letters.
	
	Depending on the size of the word list, this function may
	take a while to finish.
	"""
	print ("Loading word list from file...")
	# inFile: file
	inFile = open(WORDLIST_FILENAME, 'r')
	# wordlist: list of strings
	wordlist = []
	for line in inFile:
		wordlist.append(line.strip().lower())
	print ("  ", len(wordlist), "words loaded.")
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


# # (end of helper code)
# # -----------------------------------

# # Actually load the dictionary of words and point to it with 
# # the wordlist variable so that it can be accessed from anywhere
# # in the program.
wordlist = load_words()

# # TO DO: your code begins here!

print ("go" in wordlist)
def ghost():
	print ('Welcome to Ghost!')
	player = 1
	print ('player', player, 'goes first')
	word_fragment = ''
	print ('Current word fragment:', word_fragment)
	game_mode = True
	while game_mode:
		while True:
			letter = input('please input a letter: ')
			if letter == '.':
				print ('player', player, 'has stopped the game')
				return word_fragment
			elif letter not in string.ascii_letters:
				print ('please read the instruction')
			else:
				break 
		# asserting all letters to be in lower case  
		letter = letter.lower()	
		print ('player', player, 'says letter: ', letter )
		# attaching the letter to the eisting word fragment
		word_fragment = word_fragment + letter 
		print ('Current word fragment:', word_fragment)
		if len(word_fragment) > 3:
			# if length of current word fragment is more than 3 and is a valid, the player loses
			if word_fragment in wordlist:
				print ('player', player, 'loses because', word_fragment, 'is a word!')
				if player == 1:
					print ('player 2 wins!')
				else:
					print ('player 1 wins!')
				return player 
		wordexist = False		
		for word in wordlist:
			# if the current word fragment is part of any valid word, the word exists
			if word_fragment == word[:len(word_fragment)]:
				wordexist = True
				break
		if wordexist == False:
			print ('player', player, 'loses because no word begins with', word_fragment, '!')
			if player == 1:
				print ('player 2 wins!')
			else:
				print ('player 1 wins!')
			return player
		if player == 1:
			player = 2
		else:
			player = 1
		print ('player', player,"'s", 'turn')


ghost()