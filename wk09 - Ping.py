'''
Week 9 - Ping
https://ejudge.it.kmitl.ac.th/problem/8256
'''


import math


REQUEST_TIME_OUT_MSG = 'Request timed out.'
GENERAL_FAILURE_MSG = 'General failure.'


def get_address_from_dir(directory: str):
    '''Get address from directory'''

    ping_pos = directory.find('ping ')

    return directory[ping_pos+5:]


def get_address(pinging_msg: str, directory: str):
    '''Get address from pinging message'''

    first_bracket_pos = pinging_msg.find('[')
    last_bracket_pos = pinging_msg.find(']')

    if first_bracket_pos == -1:
        return get_address_from_dir(directory)

    return pinging_msg[first_bracket_pos+1:last_bracket_pos]


def find_ping_time(reply_msg: str):
    '''Find ping time'''

    time_pos = reply_msg.find('time')
    ms_pos = reply_msg.find('ms')

    time_msg = reply_msg[time_pos:ms_pos]

    equal_sign_pos = time_msg.find('=')
    less_than_sign_pos = time_msg.find('<')

    if less_than_sign_pos != -1:
        return int(time_msg[less_than_sign_pos+1:]), True

    return int(time_msg[equal_sign_pos+1:]), False


def main():
    '''Main Function'''

    directory = input()
    _ = input()
    pinging_msg = input()

    total_recived_packet = 0
    total_lost_packet = 0

    total_ping_time = 0
    maximum_ping_time = -99999
    minimum_ping_time = 99999

    for _ in range(4):
        reply_msg = input()

        if not reply_msg:
            continue

        if reply_msg == REQUEST_TIME_OUT_MSG \
                or reply_msg == GENERAL_FAILURE_MSG:
            total_lost_packet += 1
            continue

        ping_time, less_than = find_ping_time(reply_msg)

        if less_than:
            ping_time = 0

        total_ping_time += ping_time
        total_recived_packet += 1

        if ping_time > maximum_ping_time:
            maximum_ping_time = ping_time
        if ping_time < minimum_ping_time:
            minimum_ping_time = ping_time

    def display_statistics():
        '''Display statistics'''

        nonlocal directory
        nonlocal pinging_msg
        nonlocal total_ping_time
        nonlocal minimum_ping_time, maximum_ping_time
        nonlocal total_recived_packet, total_lost_packet

        address = get_address(pinging_msg, directory)

        total_sent_packet = total_recived_packet + total_lost_packet

        total_percent_loss = 0
        total_percent_loss = math.floor(
            total_lost_packet/total_sent_packet*100)

        print('Ping statistics for %s:' % address)
        print('    Packets: Sent = %d, Received = %d, Lost = %d (%d' % (
            total_sent_packet,
            total_recived_packet, total_lost_packet,
            total_percent_loss
        ) + '% loss),')

        if total_recived_packet:
            average_ping_time = total_ping_time // total_recived_packet

            print('Approximate round trip times in milli-seconds:')
            print('    Minimum = %dms, Maximum = %dms, Average = %dms' % (
                minimum_ping_time, maximum_ping_time, average_ping_time
            ))

    display_statistics()


main()
