'''
Week 9 - B - Fully pair?
https://ejudge.it.kmitl.ac.th/problem/8263
'''


def main():
    '''Main Function'''

    sequence = input()

    missing_pairs_list = []

    is_skipped = False

    for index, char in enumerate(sequence):

        if is_skipped:
            is_skipped = False
            continue

        if char in missing_pairs_list:
            if sequence[index+1] == char:
                is_skipped = True
                continue

            missing_pairs_list.remove(char)
            continue

        missing_pairs_list.append(char)

    if len(missing_pairs_list):
        print(*missing_pairs_list, sep='')
    else:
        print('fully paired')


main()
