'''
Week 11 - LineSorting
https://ejudge.it.kmitl.ac.th/problem/8289
'''


def main():
    '''Main Function'''

    loops = int(input())

    sentence_list = []

    for _ in range(loops):
        sentence = input()
        sentence_list.append(sentence)

    sentence_list.sort(key=len)

    print(*sentence_list, sep='\n')


main()
