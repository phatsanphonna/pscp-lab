'''
wk9 - MAC
ไอเหี้ย ในที่สุดกูก็แก้โจทย์นี้ได้สักที
แก้ได้สำเร็จตอน 22/09/2022 13:01:13
'''

BASE16_CHAR = '0123456789abcdef'


def show_result(valid_1: bool, valid_2: bool, valid_3: bool, is_error: bool):
    '''Show result'''

    if is_error:
        print('ERROR')
        return

    if valid_1:
        print('VALID 1')
    elif valid_2:
        print('VALID 2')
    elif valid_3:
        print('VALID 3')
    else:
        print('ERROR')


def check_seperator(valid_seperator: int, count: int):
    '''Check seperator'''

    return valid_seperator == count


def check_valid_1(mac_address: str):
    '''Check that if MAC address is equal to type 1'''

    seperator_position = '2 5 8 11 14'

    mac_address_length = len(mac_address)

    valid_seperator = 0

    # check for valid 1
    for i in range(mac_address_length):
        char = mac_address[i]

        if char == '-' and str(i) in seperator_position:
            valid_seperator += 1
        elif char.lower() not in BASE16_CHAR:
            return False

    return check_seperator(valid_seperator, 5)


def check_valid_2(mac_address: str):
    '''Check that if MAC address is equal to type 2'''

    seperator_position = '2 5 8 11 14'

    mac_address_length = len(mac_address)

    valid_seperator = 0

    # check for valid 2
    for i in range(mac_address_length):
        char = mac_address[i]

        if char == ':' and str(i) in seperator_position:
            valid_seperator += 1
        elif char.lower() not in BASE16_CHAR:
            return False

    return check_seperator(valid_seperator, 5)


def check_valid_3(mac_address: str):
    '''Check that if MAC address is equal to type 2'''

    seperator_position = '4 9'

    mac_address_length = len(mac_address)

    valid_seperator = 0

    # check for valid 3
    for i in range(mac_address_length):
        char = mac_address[i]

        if char == '.' and str(i) in seperator_position:
            valid_seperator += 1
        elif char.lower() not in BASE16_CHAR:
            return False

    return check_seperator(valid_seperator, 2)


def main():
    '''
    Main Function
    กูนี่แม่งสุดยอดจริง ๆ หว่ะ แก้ได้สำเร็จแล้วว้อยยยย
    '''

    mac_address = input()
    mac_address_length = len(mac_address)

    is_error = False

    for char in mac_address:
        if not char.lower() in '0123456789abcdef:-.':
            is_error = True
            break

    if is_error:
        print('ERROR')
        return

    valid_1 = check_valid_1(mac_address)
    valid_2 = check_valid_2(mac_address)
    valid_3 = check_valid_3(mac_address)

    if valid_1 or valid_2:
        if mac_address_length != 17:
            is_error = True

    if valid_3 and mac_address_length != 14:
        is_error = True

    show_result(valid_1, valid_2, valid_3, is_error)


main()
