import copy

def print_factors(num = 96):
	print 'printing factors'
	print "1 * "+str(num)

	def print_factor_helper(num, smallest, numbers_so_far = [1]):
		# print str(numbers_so_far) + ': ' + str(num) + ' : '+str(smallest)
		if num == 1:
			print 'factors: ' + str(numbers_so_far)
		# if num == smallest:
		# 	nsf = copy.copy(numbers_so_far)
		# 	nsf.append(smallest)
		# 	print 'factors: ' + str(nsf)
		for i in range(smallest, num+1):
			if num % i == 0:
				nsf = copy.copy(numbers_so_far)
				nsf.append(i)
				print_factor_helper(num/i, i, nsf)

	print_factor_helper(num, 2)


def reverse_words(words = 'hello world there is a dog in my house'):
	print 'starting reverse string ...'

	def reverse_word(word = 'and abcdefg that you need to know', start=4, end=10):
		word = list(word)
		length = end-start
		for i in range(0, length/2+1):
			tmp = word[start + i]
			word[start + i] = word[end-i]
			word[end - i] = tmp
		return ''.join(word)

	reversed_words = reverse_word(words, 0, len(words)-1)
	spaces = []
	spaces.append(-1)
	for i in range(0, len(reversed_words)):
		if reversed_words[i] == ' ':
			spaces.append(i)
	spaces.append(len(reversed_words))
	for i in range(0, len(spaces)-1):
		a = spaces[i]+1
		b = spaces[i+1]-1
		reversed_words = reverse_word(reversed_words, a, b)



	print reversed_words


def forms_triangle(array = [2,4,5,6,7,10])

if __name__=='__main__':
	print 'running first method'
	# print_factors()


	reverse_words()
