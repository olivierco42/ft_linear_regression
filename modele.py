class Modele:
	theta0: float = 0
	theta1: float = 0
	theta0_tmp: float = 0
	theta1_tmp: float = 0
	mileage: float = 0
	iteration: int = 1000
	learning_rate: float = 0.01
	mileage_lst: list = []
	price_lst : list = []

	def __init__(self, mileage_lst: list, price_lst: list):
		self.mileage_lst = mileage_lst
		self.price_lst = price_lst