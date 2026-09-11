import csv
from math_formula import ft_normalisation

def ft_estimate_price(theta0: int, theta1: int, mileage: int) -> int:
	return theta0 + (theta1 * mileage)

def save_data(iteration: int, theta0: int, theta1: int):

	data_lst: lst = [['iteration', iteration + 1],
					['theta0', theta0],
					['theta1', theta1]]

	#print(data_lst)

	with open('test.csv', 'a', newline='') as csvfile:
		writer = csv.writer(csvfile, delimiter=' ')
		writer.writerows(data_lst)
		writer.writerow([])

def calculation(mileage_price_list: list):
	theta0: int = 0
	theta1: int = 0
	iteration: int = 1000
	learning_rate: int = 0.01
	mileage_lst = ft_normalisation(mileage_price_list[0])
	price_lst =  ft_normalisation(mileage_price_list[1])
	theta0_tmp: float = 0
	theta1_tmp = float = 0

	for x in range(iteration):
		for index, (price, mileage) in enumerate(zip(price_lst, mileage_lst)):
			estimate_price = ft_estimate_price(theta0, theta1, mileage)

			theta0_tmp += (estimate_price - price)

			theta1_tmp += ((estimate_price - price) * mileage)


			if index == len(price_lst) - 1:
				theta0 = learning_rate * (theta0_tmp / len(price_lst))
				#print("theta0", theta0)
				theta1 += -(learning_rate * (theta1_tmp / len(price_lst)))
				#print("theta1", theta1)
				theta0_tmp = 0
				theta1_tmp = 0
				save_data(x, theta0,theta1)
				#print()
	print("theta0", theta0, "  theta1", theta1)

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