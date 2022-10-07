'''
Week 11 - Cat Parade
https://ejudge.it.kmitl.ac.th/problem/8278
'''


def main():
    '''Main Function'''

    specie_list = []
    while True:
        specie = input()

        if specie == 'END':
            break

        if specie == "IT'S A DOG":
            specie_list.pop()
            continue

        specie = specie.split(', ')

        for spc in specie:
            specie_list.append(spc)

    printed = []
    print_list = []

    for specie in specie_list:
        if specie in printed:
            continue

        print_list.append('%s %d %d' % (
            specie, specie_list.index(specie) + 1, specie_list.count(specie)))
        printed.append(specie)

    print_list = sorted(print_list)

    print(*print_list, sep='\n')


main()
