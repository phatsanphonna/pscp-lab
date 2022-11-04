'''Week 15 - BloodDonation'''


def main():
    '''Main Function'''

    age = int(input())
    weight = int(input())
    donate_total = int(input())

    letter = False

    if 60 <= age <= 70 or age == 17:
        granted = input()

        if granted == 'True':
            letter = True
        elif granted == 'False':
            letter = False

    if not 17 <= age <= 70:
        print('No')
        return

    if weight < 45:
        print('No')
        return

    if donate_total == 0 and age >= 55:
        print('No')
        return

    if age == 17 and not letter:
        print('No')
        return

    if 60 <= age <= 70 and not letter:
        print('No')
        return

    print('Yes')


main()
