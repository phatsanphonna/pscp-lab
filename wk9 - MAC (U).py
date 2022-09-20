'''
wk9 - MAC
- ติด Testcase อันรองสุดท้าย
'''


def show_result(valid_1, valid_2, valid_3, is_error):
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


def check_seperator(valid_seperator, count):
    '''Check seperator'''

    return valid_seperator == count


def main():
    '''Main Function'''

    mac_address = input()

    is_error = False

    valid_1 = False
    valid_2 = False
    valid_3 = False

    for char in mac_address:
        if not char.lower() in '0123456789abcdef:-.':
            is_error = True
            break

    if is_error:
        print('ERROR')
        return

    valid_1_seperator = 0

    # check for valid 1
    for i in range(2, len(mac_address), 3):
        if mac_address[i] == '-':
            valid_1_seperator += 1

    valid_1 = check_seperator(valid_1_seperator, 5)

    valid_2_seperator = 0

    # check for valid 2
    for i in range(2, len(mac_address), 3):
        if mac_address[i] == ':':
            valid_2_seperator += 1

    valid_2 = check_seperator(valid_2_seperator, 5)

    valid_3_seperator = 0

    # check for valid 3
    for i in range(4, len(mac_address), 5):
        if mac_address[i] == '.':
            valid_3_seperator += 1

    valid_3 = check_seperator(valid_3_seperator, 2)

    if valid_1 or valid_2:
        if len(mac_address) != 17:
            is_error = True

    if valid_3 and len(mac_address) != 14:
        is_error = True

    show_result(valid_1, valid_2, valid_3, is_error)


main()
