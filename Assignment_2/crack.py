import pdb
import subprocess


def load_data():
	data = [] 

	with open("output", 'r') as file:
		for line in file:
			data.append(int(line.strip()))
	return data 


def create_initial_list(data):
	nones = [None] * 344	
	return nones + data


def create_two_possibilities(data):
	return [[element * 2, element * 2 + 1] for element in data]


def subtract_r(previous, latter):
	new_list = []

	for p in previous: 
		for l in latter:
			element = p - l
			new_list.append(element)

	return set(new_list)

def fill_data_list(data):
	for i in range(343, 30, -1):
		data[i] = subtract_r(data[i + 31], data[i + 28])
	return data 

def get_possible_seeds(data):
	possible_seeds = []

	for value in data[31]:
		possible_seeds.append(value % 2**31)

	return possible_seeds


def compare_possible_seeds(possible_seeds, first):
	valid_seeds = []
	for seed in possible_seeds:
		possible_first = call_c(1, seed)
		if possible_first[0] == first: 
			valid_seeds.append(seed)
	return valid_seeds


def call_c(size, seed):
	proc = subprocess.Popen(
		['./a.out', str(size), str(seed)], stdout=subprocess.PIPE)
	out, _ = proc.communicate()
	return [int(num) for num in out.decode('utf-8').split('\n') if num]


def main():

	data = load_data()
	first = data[0]

	data = create_two_possibilities(data)
	data = create_initial_list(data)
	
	data = fill_data_list(data)
	possible_seeds = get_possible_seeds(data)
	seeds = compare_possible_seeds(possible_seeds, first)
	print(f"Seeds: {seeds}")

	# ret = call_c(60, 1)
	# print(ret)


if __name__ == "__main__":	
	main()


