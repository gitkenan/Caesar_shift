
def Caesar_shift(string, shift):
	"""
   Encrypts the input text using the Caesar cipher.

   :param text: The text to encrypt.
   :param shift: The shifting constant.
   :return: The encrypted string.
   """
	shifted = ''			# for filling
	for symbol in string:
		if symbol.isalpha():		# if it's an alphabet symbol or not
			num = ord(symbol)
			num += int(shift)

			if symbol.isupper():		# if it's uppercase
				if num > ord('Z'):
					num -= 26
				elif num < ord('A'):
					num += 26
			
			elif symbol.islower():		# if it's lowercase
				if num > ord('z'):
					num -= 26
				elif num < ord('a'):
					num += 26
			
			shifted += chr(num)
		else:
			shifted += symbol
	
	return shifted

# to draw from as a database
# to refer to when trying different shifts of 
# for this script to refer to when trying different shifts of 
# an encoded string
with open('words_alpha.txt') as word_file:
   	valid_words = set(word_file.read().split())

def rev_c_shift(string):
	letterz = list(str(string))

	decipherings = [[] for i in range(26)]
	
	for k in range(26):
		global English_count
		English_count = 0
		
		for i in letterz:
			if i.isalpha():
				decipherings[k].append(Caesar_shift(i, k))
			else: 
				decipherings[k].append(i)

		decipherings[k] = ''.join(decipherings[k])
		decipherings[k] = decipherings[k].split(' ') 

		for i in decipherings[k]:
			if i in valid_words:
				English_count += 1
			else:
				English_count -= 1

		if English_count > 0:
			return decipherings[k], "also", k, "is what we shifted by"
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
