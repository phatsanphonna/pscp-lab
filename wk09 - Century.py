'''
Week 9 - Century
https://ejudge.it.kmitl.ac.th/problem/8262
'''


def calculate_century(year: int):
    '''Calculate century'''

    century, fraction = divmod(year, 100)

    if year < 1:
        return 'ERROR'

    if fraction:
        century += 1

    return century


def main():
    '''Main Function'''

    loops = int(input())

    century_list = []

    for _ in range(loops):
        year_input = input()

        year_temp = year_input[year_input.count('. ') + 4: len(year_input)]

        year = int(year_temp)

        if 'B.E.' in year_input:
            year -= 543
            century_list.append(calculate_century(year))
        elif 'A.D.' in year_input:
            century_list.append(calculate_century(year))

    for century in century_list:
        print(century)


main()
