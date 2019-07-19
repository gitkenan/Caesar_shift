# This programme will take a string and output an encrypted
# version of the string via a Caesar shift. The string 
# package lets us create dictionaries more easily using the 
# lists string.asci_lowercase
import string

# For transferring letters to numbers & visaversa
alph_to_num = dict(zip(string.ascii_lowercase, range(0, 26)))
num_to_alph = dict(zip(range(0, 26), string.ascii_lowercase))

# this funcion performs the shifting itself on lowercase letters,
# ensuring that spaces get mapped to spaces because we don't want
# to interfere with them
def Caesar_shift(string, shift):
	letterz = list(str(string))
	shifted = []

	for i in letterz:
		if i != ' ':
			shifted.append((int(alph_to_num[i]) + int(shift)) % 26)
		else:
			shifted.append(i)

	done_let = []

	for i in shifted:
		if i != ' ':
			done_let.append(num_to_alph[i])
		else: 
			done_let.append(i)

	return ''.join(done_let)


# We load a text file of english words to draw from as a database
# for this script to refer to when trying different shifts of 
# an encoded string
with open('words_alpha.txt') as word_file:
   	valid_words = set(word_file.read().split())



def rev_c_shift(string):
	letterz2 = list(str(string))

	shifted_lists = [[] for i in range(26)]
	
	

	for k in range(26):
		global English_count
		English_count = 0
		
		for i in letterz2:
			if i != ' ':
				shifted_lists[k].append(Caesar_shift(i, k))
			else: 
				shifted_lists[k].append(i)

		shifted_lists[k] = ''.join(shifted_lists[k])
		shifted_lists[k] = shifted_lists[k].split(' ') 

		for i in shifted_lists[k]:
			if i in valid_words:
				English_count += 1
			else:
				English_count -= 1

		if English_count > 0:
			return shifted_lists[k], "also", k, "is what we shifted by"
		else:
			pass



# to handle the top-level interaction with the user
def main():
	print """Welcome to the Caesar cipher script.
What would you like to do?
1. Encrypt
2. Decrypt
Enter your option below."""

	user_answer = raw_input("> ")

	if user_answer == "1":
		print "Enter the text you would like to encrypt."
		encrypt = raw_input("> ")
		print "Enter the shifting constant."
		shifter = raw_input("> ")

		print str(Caesar_shift(encrypt, shifter)), "is the encrypted string."

	elif user_answer == "2":
		print "Enter the text you would like to decrypt."
		decrypt = raw_input("> ")
		print "The decrypted string is", rev_c_shift(decrypt)

	else:
		print "That is not an option. Try again."
		main()

	print """Thank you for using this programme,
written by Kenan Al-Shamie."""

if __name__ == "__main__":
	main()