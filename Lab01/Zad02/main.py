# by Crowfunder
# I do not feel regret for any mess I've made.
# This is pre-hackathon training.

import time
from array import array

def Listy():

    # lista danych
    data = [1,2]
    for i in range(2,48):
        data.append((data[i-1]+data[i-2])/(data[i-1]-data[i-2]))

    # policz średnią aryt
    avg = sum(data)/len(data)

    # policz modę
    moda = 0
    for num in data: 
        if data.count(num) > data.count(moda):
            moda = num

    #print(f'Moda: {moda}')
    #print(f'Średnia: {avg}')

    data_index = dict()
    for num in data:
        if num not in data_index.keys():
            data_index[num] = 1
        else:
            #print(f'Wartość {num} występuje {data_index[num]} razy')
            data_index[num] += 1

    if not any(value > 1 for value in data_index.values()):
        #print('Brak wartości powtarzających się.')
        pass
        

def Arrays():
    # lista danych
    data = array('f',(1,2))
    for i in range(2,48):
        data.append((data[i-1]+data[i-2])/(data[i-1]-data[i-2]))

    # policz średnią aryt
    avg = sum(data)/len(data)

    # policz modę
    moda = 0
    for num in data: 
        if data.count(num) > data.count(moda):
            moda = num

    #print(f'Moda: {moda}')
    #print(f'Średnia: {avg}')

    data_index = dict()
    for num in data:
        if num not in data_index.keys():
            data_index[num] = 1
        else:
            #print(f'Wartość {num} występuje {data_index[num]} razy')
            data_index[num] += 1

    if not any(value > 1 for value in data_index.values()):
        #print('Brak wartości powtarzających się.')
        pass

iterations=1000

time_start = time.time()
for i in range(iterations):
    Listy()
time_stop = time.time()
print(f'Listy:  {(time_stop-time_start)/iterations} sekund')

time_start = time.time()
for i in range(iterations):
    Arrays()
time_stop = time.time()
print(f'Arrays: {(time_stop-time_start)/iterations} sekund')

