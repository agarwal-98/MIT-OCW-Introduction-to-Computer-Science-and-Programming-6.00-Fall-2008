# Problem Set 5: 6.00 Word Game
# Name: 
# Collaborators: 
# Time: 
import random
import string
import time
from itertools import combinations

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 13
k = 4

SCRABBLE_LETTER_VALUES = {
	'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
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


# (end of helper code)
# -----------------------------------

#
#
def get_word_score(word, n):
	"""
	Returns the score for a word. Assumes the word is a
	valid word.

	The score for a word is the sum of the points for letters
	in the word, plus 50 points if all n letters are used on
	the first go.

	Letters are scored as in Scrabble; A is worth 1, B is
	worth 3, C is worth 3, D is worth 2, E is worth 1, and so on.

	word: string (lowercase letters)
	returns: int >= 0
	"""
	# TO DO ...
	total_score = 0
	if len(word) == n:
	# sets out the initial value of word as 50 or 0 depending on the length of the word
		total_score = 50
	for letter in word:
	# calls for the value of the letter from the dictionary
		letter_value = SCRABBLE_LETTER_VALUES[letter]
	# keeps summing up the score for each letter
		total_score = total_score + letter_value
	return total_score

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
			print (letter,)              # print all on the same line
	(print)                              # print an empty line



#
# Make sure you understand how this function works and what it does!
#
def deal_hand(n):
	"""
	Returns a random hand containing n lowercase letters.
	At least n/3 the letters in the hand should be VOWELS.

	Hands are represented as dictionaries. The keys are
	letters and the values are the number of times the
	particular letter is repeated in that hand.

	n: int >= 0
	returns: dictionary (string -> int)
	"""
	hand={}
	num_vowels = n / 3
	
	for i in range(int(num_vowels)):
		x = VOWELS[random.randrange(0,len(VOWELS))]
		hand[x] = hand.get(x, 0) + 1
		
	for i in range(int(num_vowels), n):    
		x = CONSONANTS[random.randrange(0,len(CONSONANTS))]
		hand[x] = hand.get(x, 0) + 1
		
	return hand

#

def update_hand(hand, word):
	"""
	Assumes that 'hand' has all the letters in word.
	In other words, this assumes that however many times
	a letter appears in 'word', 'hand' has at least as
	many of that letter in it. 

	Updates the hand: uses up the letters in the given word
	and returns the new hand, without those letters in it.

	Has no side effects: does not mutate hand.

	word: string
	hand: dictionary (string -> int)    
	returns: dictionary (string -> int)
	"""
	# TO DO ...

	for letter in word:
		# removing letter from hand
		hand[letter] = hand[letter] - 1
		if hand[letter] == 0:
		# if no more of the letter left, deleting the letter from the hand
			del hand[letter]
	return hand


#  ----------------------------------------------------------------

#
def is_valid_word(word, hand, word_list):
	"""
	Returns True if word is in the word_list and is entirely
	composed of letters in the hand. Otherwise, returns False.
	Does not mutate hand or word_list.
	
	word: string
	hand: dictionary (string -> int)
	word_list: list of lowercase strings
	"""
	# TO DO ...

	# checking if word is a valid word
	if word in word_list:
		word_count = get_frequency_dict(word)
		for letter in word:
			print (letter)

		# testing if the letter and the total nmumber of it is in the hand
			if letter in hand.keys() and  word_count[letter] <=hand[letter]:
				continue
			else:
				return False
	else:
		return False
	return True



#  ---------------------------------------------------------------------------
# Problem #1: Playing a hand (How Long?)



def play_hand(hand, word_list):
	"""
	Allows the user to play the given hand, as follows:

	* The hand is displayed.
	
	* The user may input a word.

	* An invalid word is rejected, and a message is displayed asking
	  the user to choose another word.

	* When a valid word is entered, it uses up letters from the hand.

	* After every valid word: the score for that word and the total
	  score so far are displayed, the remaining letters in the hand 
	  are displayed, and the user is asked to input another word.

	* The sum of the word scores is displayed when the hand finishes.

	* The hand finishes when there are no more unused letters.
	  The user can also finish playing the hand by inputing a single
	  period (the string '.') instead of a word.

	* The final score is displayed.

	  hand: dictionary (string -> int)
	  word_list: list of lowercase strings
	"""

	# You have a friend who consistently beats you when playing the word game because she takes forever
	# to play. You decide to change the rules of the game to fix her wagon. Points are awarded as before,
	# except the points awarded for a word are divided by the amount of time taken to find the word. Points
	# for a word should be displayed to two decimal places. 


	# # TO DO ...
	print ("Current Hand:",  display_hand(hand) )
	n = len(hand)
	total_sofar = 0
	while len(hand) > 0:
		# starting time count
		start_time = time.time()
		word = input('Enter word, or a . to indicate that you are finished: ')
		# ending time count
		end_time = time.time()
		total_time = float('%0.2f' % (end_time - start_time))
		if word != '.':
			if is_valid_word(word, hand, word_list):
				rough_score = get_word_score(word,n)
				if total_time == 0 :
					net_score = get_word_score(word,n)
				else:
					net_score = float('%0.2f' % (rough_score/total_time))
				total_sofar = total_sofar + net_score
				print  ('It took %0.2f to provide an answer' % total_time )
				print (word, "earned", net_score, "points." ,)
				print ("Total:", total_sofar, "points")
				print (update_hand(hand, word))
			else : 
				print ("Invalid word. Please choose again.")
		#indicates user is finished 
		else:
			print ("Total score: ", total_sofar, "points")
			return
	print ("Total score:", total_sofar, "points") 
	return


#  ---------------------------------------------------------------------

# Problem #2: Time Limit

# You still find it boring to watch your friend think for long periods of time while playing the 6.00 word
# game. You decide to add a "chess clock" to the game. This limits the total amount of time, in seconds,
# that a player can spend to play a hand. 

def play_hand(hand, word_list):
	print ("Current Hand:",  display_hand(hand)) 
	n = len(hand)
	total_sofar = 0
	remaining_time = 0
	# setting time limit
	time_limit = 30
	total_time_taken = 0
	while len(hand) > 0:
		start_time = time.time()
		word = input('Enter word, or a . to indicate that you are finished: ')
		end_time = time.time()
		# time taken during each round
		time_taken = float('%0.2f' % (end_time - start_time))
		# cumulative time taken by the player
		total_time_taken = total_time_taken + time_taken
		# remaining time for the player
		remaining_time = time_limit - total_time_taken
		if remaining_time >= 0:
			if word != '.':
				if is_valid_word(word, hand, word_list):
					rough_score = get_word_score(word,n)
					if time_taken == 0 :
						net_score = get_word_score(word,n)
					else:
						net_score = float('%0.2f' % (rough_score/time_taken))
					total_sofar = total_sofar + net_score
					print  ('It took %0.2f seconds to provide an answer' % time_taken)
					print ('You have %0.2f seconds remaining' % remaining_time)
					print (word, "earned", net_score, "points." ,)
					print ("Total:", total_sofar, "points")
					print (update_hand(hand, word))
				else : 
					print  ('It took %0.2f seconds to provide an answer' % time_taken)
					print ('You have %0.2f seconds remaining' % remaining_time)				
					print ("Invalid word. Please choose again.")
			else:
				print( "Total score: ", total_sofar, "points")
				return ''
		else:
			print ('It took %0.2f seconds to provide an answer' % time_taken)
			print ('Total time exceeds', time_limit, 'seconds. You earned', total_sofar, 'points')
			return 
	print( "Total score:", total_sofar, "points" )
	return ''


#  ------------------------------------------------------------------

# Problem #3: Computer Player

# Instead of having the user enter words, we will replace the call to raw_input (inside play_hand) with
# a call to the following functions: 


def get_words_to_points(word_list):
	#  Return a dict that maps every word in word_list to its point value. 
	pointsdict = {}
	for every_word in word_list:
		word_value = get_word_score(every_word, HAND_SIZE)
		pointsdict[every_word] = word_value
	return pointsdict


def pick_best_word(hand,points_dict):
	#  Return the highest scoring word from points_dict that can be made with the
	# given hand.
	best_word = ""
	best_val = 0
	for word in points_dict:
		if is_valid_word(word, hand,points_dict):
			word_val = get_word_score(word, HAND_SIZE)
			if word_val > best_val:
				best_val = word_val
				best_word = word 
	if  best_val > 0:
		return best_word
	else:
		return "."

def get_time_limit(points_dict, k):
# 
#  Return the time limit for the computer player as a function of the
# multiplier k.
#  points_dict should be the same dictionary that is created by
# get_words_to_points.

	start_time = time.time()
# Do some computation. The only purpose of the computation is so we can
# figure out how long your computer takes to perform a known task.
	for word in points_dict:
		get_frequency_dict(word)
		get_word_score(word, HAND_SIZE)
	end_time = time.time()
	time_limit = (end_time-start_time)*k
	print ('my time limit', time_limit)
	return time_limit



def is_valid_word(word, hand, points_dict):

	word_count = get_frequency_dict(word)
	for letter in word:
		if letter in hand.keys() and  word_count[letter] <=hand[letter]:
			continue
		else:
			return False
			# return result
	return word 



def play_hand(hand, word_list):
	print ("Current Hand:",  display_hand(hand) )
	total_sofar = 0
	remaining_time = 0
	total_time_taken = 0
	limit = time_limit
	while len(hand) > 0:
		start_time = time.time()
		# uncomment below for next problem on how to choose the best word faster
		# word = pick_best_word_faster(hand, rearranged_dict)
		word = pick_best_word(hand,points_dict)
		end_time = time.time()
		print (word)
		time_taken = float('%0.2f' % (end_time - start_time))
		total_time_taken = total_time_taken + time_taken
		remaining_time = limit - total_time_taken
		if remaining_time >= 0:
			if word != '.':
				rough_score = get_word_score(word,HAND_SIZE)
				if time_taken == 0 :
					net_score = get_word_score(word,HAND_SIZE)
				else:
					net_score = float('%0.2f' % (rough_score/time_taken))
				total_sofar = total_sofar + net_score
				print  ('It took %0.2f seconds to provide an answer' % time_taken)
				print ('You have %0.2f seconds remaining' % remaining_time)
				print( word, "earned", net_score, "points." ,)
				print ("Total:", total_sofar, "points")
				print (update_hand(hand, word))
			else:
				print ("Total score: ", total_sofar, "points")
				return ''
		else:
			print ('It took %0.2f seconds to provide an answer' % time_taken)
			print ('Total time exceeds', limit, 'seconds. You earned', total_sofar, 'points')
			return 
	print ("Total score:", total_sofar, "points" )
	return ''



#  ----------------------------------------------------------------


# Problem #4:  Even Faster Computer Player

# Now implement a faster computer player called pick_best_word_faster(hand, rearrange_dict). It
# should be based on the following approach described below. (This is a good example of what
# pseudocode should look like).
# First, do this pre-processing before the game begins:
# Let d = {}
# For every word w in the word list:
# Let d[(string containing the letters of w in sorted order)] = w


def get_word_rearrangements(word_list):
	d = {}
	for word in word_list:
		sorted_word = ''.join(sorted(word))
		d[sorted_word] = word
	return d 

# Now, given a hand, here's how to use that dict to find a word that can be made from that hand:
# To find some word that can be made out of the letters in HAND:
#  For each subset S of the letters of HAND:
#  Let w = (string containing the letters of S in sorted order)
# If w in d: return d[w] 

def pick_best_word_faster(hand, rearrange_dict):
	full_str = ''
	# creating a string of all the letters in hand
	for each in hand:
		full_str = full_str + each*hand[each]
	best_val = 0
	for i in range(len(full_str)):
		# finding different combos a string of a given length (max length = length of the hand)
		for combos in combinations(full_str,i):
		# sorting each combination
			subset = ''.join(sorted(combos))
		# finding each sorted subset in the rearranged dict and the value correspoding to its word 
		# to find the highest value
			if subset in rearrange_dict:
				word = rearrange_dict[subset]
				word_val = get_word_score(word, HAND_SIZE)
				if word_val > best_val:
					best_val = word_val
					best_word = word 

	if  best_val > 0:
		return best_word
	else:
		return "."


def play_game(word_list):
	"""
	Allow the user to play an arbitrary number of hands.

	* Asks the user to input 'n' or 'r' or 'e'.

	* If the user inputs 'n', let the user play a new (random) hand.
	  When done playing the hand, ask the 'n' or 'e' question again.

	* If the user inputs 'r', let the user play the last hand again.

	* If the user inputs 'e', exit the game.

	* If the user inputs anything else, ask them again.
	"""
	# TO DO ...
	# print "play_game not implemented."         # delete this once you've completed Problem #4
	# play_hand(deal_hand(HAND_SIZE), word_list) # delete this once you've completed Problem #4
	
	## uncomment the following block of code once you've completed Problem #4
	hand = deal_hand(HAND_SIZE) # random init
	while True:	
		cmd = input('Enter n to deal a new hand, r to replay the last hand, or e to end game: ')
		if cmd == 'n':
			hand = deal_hand(HAND_SIZE)
			play_hand(hand.copy(), word_list)
			print
		elif cmd == 'r':
			play_hand(hand.copy(), word_list)
			print
		elif cmd == 'e':
			break
		else:
			print ("Invalid command.")

#
# Build data structures used for entire session and play game
#

if __name__ == '__main__':
	word_list = load_words()
	points_dict = get_words_to_points(word_list)
	time_limit = get_time_limit(points_dict, k)
	rearranged_dict = get_word_rearrangements(word_list)
	play_game(word_list)

# Problem 5: Algorithm Analysis

# Characterize the time complexity of your implementation (in terms of the size of word_list and
# the number of letters in a hand) of both pick_best_word and pick_best_word_faster.