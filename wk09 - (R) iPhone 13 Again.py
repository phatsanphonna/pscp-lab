'''
[Recommend]
Week 9 - iPhone 13 Again
https://ejudge.it.kmitl.ac.th/problem/8260
'''


def model_mini_price(capacity: str):
    '''Return price of mini model'''

    if capacity == '128 GB':
        return 25900
    elif capacity == '256 GB':
        return 28900
    elif capacity == '512 GB':
        return 37900
    else:
        return 'Not Available'


def model_pro_price(capacity: str):
    '''Return price of Pro model'''

    if capacity == '128 GB':
        return 38900
    elif capacity == '256 GB':
        return 42900
    elif capacity == '512 GB':
        return 50900
    elif capacity == '1 TB':
        return 58900
    else:
        return 'Not Available'


def model_promax_price(capacity: str):
    '''Return price of Pro Max model'''

    if capacity == '128 GB':
        return 42900
    elif capacity == '256 GB':
        return 46900
    elif capacity == '512 GB':
        return 54900
    elif capacity == '1 TB':
        return 62900
    else:
        return 'Not Available'


def main():
    '''Main Function'''

    series = input().split(' ')
    capacity = input()

    if series[0].lower() != 'iphone':
        print('Not Available')
        return

    if series[1] != '13':
        print('Not Available')
        return

    model = ''

    if len(series) > 2:
        model = model.join(series[2:]).lower()

    else:
        # iPhone 13

        if capacity == '128 GB':
            print(29900)
        elif capacity == '256 GB':
            print(33900)
        elif capacity == '512 GB':
            print(42900)
        else:
            print('Not Available')

        return

    price = 0

    if model == 'mini':
        # iPhone 13 mini
        price = model_mini_price(capacity)
    elif model == 'pro':
        # iPhone 13 Pro
        price = model_pro_price(capacity)
    elif model == 'promax':
        # iPhone 13 Pro Max
        price = model_promax_price(capacity)
    else:
        price = 'Not Available'

    print(price)


main()
