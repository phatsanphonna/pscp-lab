"""Week 7 - Align"""


def main():
    """Main Function"""

    size = int(input())
    align = input().lower()
    sentence = input()

    if align == "left":
        print(sentence+(" "*(size-(len(sentence)))))
    elif align == "center":
        spac = size - (len(sentence))
        if spac % 2 != 0:
            print(((" ")*((spac//2)+1))+sentence+((" ")*((spac//2))))
        else:
            print(sentence.center(size))
    elif align == "right":
        print((" "*(size-(len(sentence))))+sentence)


main()
