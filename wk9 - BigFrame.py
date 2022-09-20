'''Week 9 - BigFrame'''


def line(length: int):
    '''Print line out to screen'''

    print('*' * (length + 4))


def body(sentence: str, length: int):
    '''Print body to screen'''

    sentence_length = len(sentence)

    print('* ' + sentence + (' ' * (length-sentence_length)) + ' *')


def main():
    '''Main Function'''

    sentence_1 = input().rstrip()
    sentence_2 = input().rstrip()
    sentence_3 = input().rstrip()
    sentence_4 = input().rstrip()
    sentence_5 = input().rstrip()

    sentence_array = [
        sentence_1, sentence_2,
        sentence_3, sentence_4, sentence_5
    ]

    sentence_length_array = [
        len(sentence) for sentence in sentence_array
    ]

    max_length = max(sentence_length_array)

    line(max_length)

    for sentence in sentence_array:
        body(sentence, max_length)

    line(max_length)


main()
