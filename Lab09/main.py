######################
# by Crowfunder
# with love
######################

from backpacker_utils import PackageFileParser
from backpacker_tests import TimeEffectivenessTester


def main():
	"""
	Main function to run the backpack packing algorithms.
	"""
	packages_ids = [20, 100, 500, 1000]
	packages = PackageFileParser(packages_ids)
	with open('Lab09/results.csv', 'w+') as file:
		file.write('Packages Set,BackpackerGreedy,BackpackerGamble,BackpackerULTRAGREED\n')
		for key in packages_ids:
			backpack_size, effective_greed, effective_gamble, effective_ultragreed = TimeEffectivenessTester(packages[key], key, repetitions=1)
			file.write(f'{backpack_size},{effective_greed},{effective_gamble},{effective_ultragreed}\n')
			file.flush()

if __name__ == '__main__':
	main()