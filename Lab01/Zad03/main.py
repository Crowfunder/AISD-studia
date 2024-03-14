# by Crowfunder
# I do not feel regret for any mess I've made.
# This is pre-hackathon training.

from time import time

# Iterowanie po obiekcie iterowalnm
def iterable(once = True):
    lista = [1,2,3,4,5]
    for i in lista:
        if once:
            print(i*i/432)
        else:
            return i*i/432
        
# Iterowanie a'la c++
def cplusplus(once = True):
    for i in range(1,6):
        if once:
            print(i*i/432)
        else:
            return i*i/432


if iterable() != cplusplus():
    print('Wyniki nie są takie same')
else:
    print('Wyniki są takie same')

iterations = 10000

time_start = time()
for i in range(iterations):
    iterable(False)
print(f'Obiekt iterowalny: {time()-time_start} sekund')

time_start = time()
for i in range(iterations):
    cplusplus(False)
print(f'Iterowanie a\'la c++: {time()-time_start} sekund')
