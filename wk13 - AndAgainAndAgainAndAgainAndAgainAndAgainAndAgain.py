'''
Week 13 - AndAgainAndAgainAndAgainAndAgainAndAgainAndAgain
https://ejudge.it.kmitl.ac.th/problem/8348
'''


def main():
    '''Main Function'''

    sentence = input().split(' ')

    result = []

    for word in sentence:
        word = ''.join(char for char in word if char.isalnum())

        vowels = 0

        for char in word:
            if char.lower() in 'aeiou':
                vowels += 1

        if vowels >= 2:
            result.append(word)

    if not result:
        print('Nope')
        return

    print(*sorted(result), sep='\n')


main()
