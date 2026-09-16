from math_formula import ft_normalisation

class Modele:
	theta0: float = 0
	theta1: float = 0
	theta0_tmp: float = 0
	theta1_tmp: float = 0
	mileage: float = 0
	iteration: int = 1000
	learning_rate: float = 0.01
	original_mileage_lst: list = []
	original_price_lst : list = []
	mileage_lst: list = []
	price_lst : list = []

	def __init__(self, lst: list):
		self.original_mileage_lst = lst[0]
		self.original_price_lst = lst[1]

		self.mileage_lst = ft_normalisation(lst[0])
		self.price_lst = ft_normalisation(lst[1])