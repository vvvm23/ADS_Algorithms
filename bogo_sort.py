import random
def sort(L):
	def sorted(L):
		prev = L[0]
		for i in range(1, len(L)):
			if L[i] < prev:
				return False
			prev = L[i]
		return True

	s = sorted(L)

	while not s:
		random.shuffle(L)
		s = sorted(L)

	return L

