'''
Week 12 - WordSequence I
https://ejudge.it.kmitl.ac.th/problem/8331
'''


def main():
    '''Main Function'''

    sentence = input()

    for i in range(len(sentence)):
        print(sentence[:i+1])


main()
