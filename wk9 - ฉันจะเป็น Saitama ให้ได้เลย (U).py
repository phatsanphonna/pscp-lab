'''Week 9 - ฉันจะเป็น Saitama ให้ได้เลย'''


import math


def main():
    '''Main Function'''

    require_pushup = int(input())
    require_situp = int(input())
    require_looknang = int(input())
    require_running = int(input())

    pushup_per_day = int(input())
    situp_per_day = int(input())
    looknang_per_day = int(input())
    running_per_day = int(input())

    total_days = 0

    while require_pushup > 0 or require_situp > 0 \
            or require_looknang > 0 or require_running > 0:
        if require_pushup > 0:
            require_pushup -= pushup_per_day
        if require_situp > 0:
            require_situp -= situp_per_day
        if require_looknang > 0:
            require_looknang -= looknang_per_day
        if require_running > 0:
            require_running -= running_per_day

        total_days += 1

    print(total_days)


main()
