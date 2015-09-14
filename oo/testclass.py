class CoolObject(object):

	def __init__(self, value):
		self.value = value

	def action(self):
		print self.value


def only_singleton(array=[1,2,3,4,5,6,1,2,4,5,6]):
	xor = 0
	for i in array:
		xor ^= i
	return xor

def bit_shift(x):
	return x<<3

if __name__=='__main__':
	co = CoolObject(3.5)
	co.action()
	print only_singleton()
	print bit_shift(5)