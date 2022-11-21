'''Week 16 - iPad Air'''


def main():
    '''Main Function'''

    color_list = ['Space Gray', 'Silver', 'Green', 'Rose Gold', 'Sky Blue']
    storage_list = [64, 256]
    tele_list = ['Wi-Fi + Cellular', 'Wi-Fi']

    color = input()
    storage = int(input())
    tele = input()

    if color not in color_list \
        or storage not in storage_list \
            or tele not in tele_list:
        print('Not Available')
        return

    if storage == 64 and tele == 'Wi-Fi':
        print(19900)
    elif storage == 64 and tele == 'Wi-Fi + Cellular':
        print(24400)
    elif storage == 256 and tele == 'Wi-Fi':
        print(24900)
    elif storage == 256 and tele == 'Wi-Fi + Cellular':
        print(29400)


main()
