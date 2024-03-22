########################
# by Crowfunder
# 
########################

INIT_INT = 500
END_INT = 3000

Result = ''

for number in range(INIT_INT, END_INT + 1):
    if not number%7 and number%5:
        Result+=str(number)

print(f'Concatenated string: {Result}')
print(f'\n21 wystąpiło {Result.count("21")} razy.')
print(f'\nWith replaced data: {Result.replace("21", "XX")}')