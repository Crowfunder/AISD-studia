######################
# by Crowfunder
# with love
######################

from bdb import effective
from time import time
from backpacker_algorithms import BackpackerGambler, BackpackerGreedy, BackpackerULTRAGREED

def TimeEffectivenessTester(packages_list, backpack_size, repetitions=100):
	SEPARATOR = '#######################'
	print(f'\n\nPackages {backpack_size}')
	print(SEPARATOR*2)

	print('\nBackpackerGreedy')
	print(SEPARATOR)
	time_start = time()
	for _ in range(repetitions):
		backpack_greedy = BackpackerGreedy(packages_list, backpack_size)
	time_delta = (time()-time_start)/repetitions
	effective_greed = backpack_greedy.total_value/time_delta
	print(f'Time: {time_delta}s')
	print(f'Value: {backpack_greedy.total_value}')
	print(f'Effectiveness: {effective_greed}')
	
	print('\nBackpackerGambler')
	print(SEPARATOR)
	time_start = time()
	for _ in range(repetitions):
		backpack_gamble = BackpackerGambler(packages_list, backpack_size, 5)
	time_delta = (time()-time_start)/repetitions
	effective_gamble = backpack_gamble.total_value/time_delta
	print(f'Time: {time_delta}s')
	print(f'Value: {backpack_gamble.total_value}')
	print(f'Effectiveness: {effective_gamble}')
	
	print('\nBackpackerULTRAGREED')
	print(SEPARATOR)
	time_start = time()
	for _ in range(repetitions):
		backpack_ultragreed = BackpackerGreedy(packages_list, backpack_size)
	time_delta = (time()-time_start)/repetitions
	effective_ultragreed = backpack_ultragreed.total_value/time_delta
	print(f'Time: {time_delta}s')
	print(f'Value: {backpack_ultragreed.total_value}')
	print(f'Effectiveness: {effective_ultragreed}')
	
	return backpack_size, effective_greed, effective_gamble, effective_ultragreed
		