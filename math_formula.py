import math
#from modele import Modele

def ft_average(lst: list) -> int:
	x: int = 0
	for element in lst:
		x += element

	return x / len(lst)

def ft_standard_deviation(lst: list):
	x: int = 0
	average: int = ft_average(lst)

	for element in lst:
		x += (element - average) ** 2

	return (x / len(lst)) ** 0.5

def ft_normalisation(lst: list) -> list:
	list_normalisation = []
	average: int = ft_average(lst)
	standard_deviation: int = ft_standard_deviation(lst)

	for element in lst:
		list_normalisation.append((element - average) / standard_deviation)

	return list_normalisation

def ft_sigma(modele: Modele):
	standard_deviation_mileage = ft_standard_deviation(modele.original_mileage_lst)
	standard_deviation_price = ft_standard_deviation(modele.original_price_lst)

	average_mileage = ft_average(modele.original_mileage_lst)
	average_price = ft_average(modele.original_price_lst)

	modele.theta1 = modele.theta1 * (standard_deviation_price / standard_deviation_mileage)
	modele.theta0 = average_price + (standard_deviation_price * modele.theta0) - (modele.theta1 * average_mileage)
