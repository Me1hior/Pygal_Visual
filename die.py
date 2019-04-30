from random import randint

class Die():
	numb = 0
	"""Класс, представляющий один кубик."""
	def __init__(self, num_sides=6):
		"""По умолчанию используется шестигранный кубик."""
		self.num_sides = num_sides
		Die.numb += 1
		
	def __del__(self):
		Die.numb -= 1

	def roll(self):
		""""Возвращает случайное число от 1 до числа граней."""
		return randint(1, self.num_sides)
		
		
