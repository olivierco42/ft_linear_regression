import csv
from modele import Modele
from math_formula import ft_normalisation

def ft_estimate_price(theta0: int, theta1: int, mileage: int) -> int:
	return theta0 + (theta1 * mileage)

def save_data(iteration: int, theta0: int, theta1: int):

	data_lst: lst = [['iteration', iteration + 1],
					['theta0', theta0],
					['theta1', theta1]]

	with open('theta_result.csv', 'a', newline='') as csvfile:
		writer = csv.writer(csvfile, delimiter=' ')
		writer.writerows(data_lst)
		writer.writerow([])

def calculation(mileage_price_list: list):
	modele = Modele(ft_normalisation(mileage_price_list[0]), ft_normalisation(mileage_price_list[1]))
	print(modele.mileage_lst)

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
				#print()
	print("theta0", modele.theta0, "  theta1", modele.theta1)

def extract_data() -> list: #verif a faire liste vide, element egeuax
	mileage_price_list = [], []
	with open('data.csv', mode='r', encoding='utf-8') as csvfile:
		spamreader = csv.reader(csvfile, delimiter=',')
		next(spamreader)
		for row in spamreader:
			mileage_price_list[0].append(int(row[0]))
			mileage_price_list[1].append(int(row[1]))
	return mileage_price_list

def main():
	mileage_price_list = extract_data()
	calculation(mileage_price_list)

if __name__ == "__main__":
	main()