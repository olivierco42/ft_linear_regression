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

def ft_sigma(lst: list) -> int:
	average: int = ft_average(lst)
	#standard_deviation: int = ft_standard_deviation(lst)