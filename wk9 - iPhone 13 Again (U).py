'''Week 9 - iPhone 13 Again'''


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

    if model == 'mini':
        # iPhone 13 mini

        if capacity == '128 GB':
            print(25900)
        elif capacity == '256 GB':
            print(28900)
        elif capacity == '512 GB':
            print(37900)
        else:
            print('Not Available')

    elif model == 'pro':
        # iPhone 13 Pro

        if capacity == '128 GB':
            print(38900)
        elif capacity == '256 GB':
            print(42900)
        elif capacity == '512 GB':
            print(50900)
        elif capacity == '1 TB':
            print(58900)
        else:
            print('Not Available')

    elif model == 'promax':
        # iPhone 13 Pro Max

        if capacity == '128 GB':
            print(42900)
        elif capacity == '256 GB':
            print(46900)
        elif capacity == '512 GB':
            print(54900)
        elif capacity == '1 TB':
            print(62900)
        else:
            print('Not Available')

    else:
        print('Not Available')


main()
