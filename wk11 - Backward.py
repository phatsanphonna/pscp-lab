'''
Week 11 - Backward
https://ejudge.it.kmitl.ac.th/problem/8280
'''


def main():
    '''Main Function'''

    sentence_list = []

    while True:
        sentence = input()

        if sentence == 'NULL':
            break

        sentence_list.append(sentence)

    sentence_list.reverse()

    print(*sentence_list, sep='\n')


main()
