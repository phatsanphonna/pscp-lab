'''Week 12 - BreachTheDoor'''


def main():
    '''Main Function'''

    word_list = input().split(' ')

    matched_word = []

    for word in word_list:
        word = ''.join(char for char in word if char.isalpha())

        if len(word) > 6:
            matched_word.append(word)

    print(*matched_word, sep=' ')


main()
