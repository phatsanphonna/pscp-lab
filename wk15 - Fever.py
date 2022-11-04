'''Week 15 - Fever'''


def main():
    ''''Main Function'''

    temperature = float(input())

    if 36 <= temperature < 38:
        print('No Fever')
    elif 38 <= temperature < 39:
        print('Mild Fever')
    elif 39 <= temperature < 40:
        print('High Fever')
    elif temperature >= 40:
        print('Very High Fever')


main()
