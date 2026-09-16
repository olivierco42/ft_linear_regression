from modele import Modele
from math_formula import ft_sigma
from data_file import extract_data, save_data

def ft_estimate_price(theta0: int, theta1: int, mileage: int) -> int:
	return theta0 + (theta1 * mileage)

def training(modele: Modele):
	for x in range(modele.iteration):
		for index, (price, mileage) in enumerate(zip(modele.price_lst, modele.mileage_lst)):
			estimate_price = ft_estimate_price(modele.theta0, modele.theta1, mileage)

			modele.theta0_tmp += (estimate_price - price)

			modele.theta1_tmp += ((estimate_price - price) * mileage)

			if index == len(modele.price_lst) - 1:
				modele.theta0 = modele.learning_rate * (modele.theta0_tmp / len(modele.price_lst))
				modele.theta1 += -(modele.learning_rate * (modele.theta1_tmp / len(modele.price_lst)))
				modele.theta0_tmp = 0
				modele.theta1_tmp = 0
				save_data(x, modele.theta0,modele.theta1)

def main():
	mileage_price_list = extract_data()

	modele = Modele(mileage_price_list)	
	training(modele)

	ft_sigma(modele)
	print(modele.theta0)
	print(modele.theta1)

if __name__ == "__main__":
	main()