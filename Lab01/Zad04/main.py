# by Crowfunder
# I do not feel regret for any mess I've made.
# This is pre-hackathon training.

# ZeroDivisionError
try:
    a = 1 / 0
except ZeroDivisionError as e:
    print('Próbowano podzielić przez zero')
    
# IndexError
try: 
    a = [1,2,3]
    print(a[2137])
except IndexError as e:
    print('Wywołano indeks spoza zakresu listy')
    
# NameError
x = 1
del x
try:
    print(x)
except NameError as e:
    print('Zmienna nie istnieje')