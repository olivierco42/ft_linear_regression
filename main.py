import csv
from mathematical_formula import ft_normalisation

def ft_estimate_price(theta0: int, theta1: int, mileage: int) -> int:
	return theta0 + (theta1 * mileage)

def calculation(mileage_price_list: list):
	theta0: int = 0
	theta1: int = 0
	#mileage: int = mileage_price_list[0][0]
	#price: int = mileage_price_list[1][0]
	learning_rate: int = 0.01
	mileage_lst = ft_normalisation(mileage_price_list[0])
	price_lst =  ft_normalisation(mileage_price_list[1])

	for price, mileage in zip(price_lst, mileage_lst):
		estimate_price = ft_estimate_price(theta0, theta1, mileage)

		theta0_tmp = learning_rate * ((estimate_price - price))# / len(mileage_price_list[0]))
		print(theta0_tmp)
		theta0 = theta0_tmp

		theta1_tmp = learning_rate * (((estimate_price - price) * mileage))#/ len(mileage_price_list[0]))
		print(theta1_tmp)
		theta1 = theta1_tmp
		print()

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