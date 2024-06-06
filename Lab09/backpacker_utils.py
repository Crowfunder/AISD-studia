######################
# by Crowfunder
# with love
######################

from backpacker_classes import Package

def PackageFileParser(list_of_sizes):
	"""
	Parse package files and return a dictionary of packages.

	Parameters:
	list_of_sizes (list): List of package sizes.

	Returns:
	dict: Dictionary containing packages for each size.
	"""
	packages = {}
	
	for size in list_of_sizes:
		packages[size] = []
		with open(f'Lab09/packages/packages{size}.txt') as file:
			for line in file.readlines():
				data = line.strip().split(',')

				# Skip headers
				if not data[0].isnumeric():
					continue

				package_obj = Package(int(data[0]), int(data[1]), int(data[2]), int(data[3]))
				packages[size].append(package_obj)

	return packages