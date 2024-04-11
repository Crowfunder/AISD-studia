from lotto_module import Lotto

# Function for list flattening, regardless of depth.
def ListFlatten(input_list):

    while type(input_list[0]) is list:
        input_list = [item for sublist in input_list for item in sublist]

    return input_list


def main():
    #print(Lotto(5).override([1,2,3]).SPRAWDZ(Lotto(5).override([2,9,3])))

    # Roll 1000 lotto games with 6 digits
    all_games = []
    for _ in range(0, 1000):
        all_games.append(Lotto(6).rolls)

    # Count occurrences of all games
    count = {}
    all_games_digits = ListFlatten(all_games)
    for number in range(0,49):
        count[number] = all_games_digits.count(number)

    # Sort and pretty print the results
    count_sorted = sorted(count.items(), key=lambda item: item[1])
    for number, occurs in count_sorted:
        print(f'Liczba {number} pojawiła sie {occurs} razy.')

    # Write RAW results to file
    filename = str(count_sorted[-1][0]) + str(count_sorted[-2][0])
    with open(filename, 'w') as file:
        for number_occurs in count_sorted:
            file.write(str(number_occurs) + '\n')


if __name__ == '__main__':
    main()