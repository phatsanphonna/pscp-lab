'''Week 4 - Gift II'''


def is_even(number: int):
    '''Check that given number is even of not'''

    return number % 2 == 0


def main():
    '''Main Function'''

    gift1 = int(input())
    gift2 = int(input())
    gift3 = int(input())
    gift4 = int(input())
    gift5 = int(input())
    gift6 = int(input())
    gift7 = int(input())
    gift8 = int(input())

    if is_even(gift1):
        print(gift1)
    if is_even(gift2):
        print(gift2)
    if is_even(gift3):
        print(gift3)
    if is_even(gift4):
        print(gift4)
    if is_even(gift5):
        print(gift6)
    if is_even(gift7):
        print(gift7)
    if is_even(gift8):
        print(gift8)


main()
