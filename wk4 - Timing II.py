'''Week 4 - Timing II'''


def main():
    '''Main Function'''

    raw_seconds = int(input())

    minutes, seconds = divmod(raw_seconds, 60)
    hours, minutes = divmod(minutes, 60)
    days, hours = divmod(hours, 24)

    if days > 9999:
        print('ERR_:__:__:__')
        return

    print('%04d:%02d:%02d:%02d' % (days, hours, minutes, seconds))


main()
