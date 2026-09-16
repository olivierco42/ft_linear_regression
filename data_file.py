import csv

def extract_data() -> list: #verif a faire liste vide, element egeuax
	mileage_price_list = [], []
	with open('data.csv', mode='r', encoding='utf-8') as csvfile:
		spamreader = csv.reader(csvfile, delimiter=',')
		next(spamreader)
		for row in spamreader:
			mileage_price_list[0].append(int(row[0]))
			mileage_price_list[1].append(int(row[1]))
	return mileage_price_list

def save_data(iteration: int, theta0: int, theta1: int):

	data_lst: lst = [['iteration', iteration + 1],
					['theta0', theta0],
					['theta1', theta1]]

	with open('theta_result.csv', 'a', newline='') as csvfile:
		writer = csv.writer(csvfile, delimiter=' ')
		writer.writerows(data_lst)
		writer.writerow([])