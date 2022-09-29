'''Week 9 - ฉันจะเป็น Saitama ให้ได้เลย'''


def main():
    '''Main Function'''

    require_pushup = abs(int(input()))
    require_situp = abs(int(input()))
    require_looknang = abs(int(input()))
    require_running = abs(int(input()))

    pushup_per_day = abs(int(input()))
    situp_per_day = abs(int(input()))
    running_per_day = abs(int(input()))
    looknang_per_day = abs(int(input()))

    total_days = 0

    while require_pushup > 0 or require_situp > 0 \
            or require_looknang > 0 or require_running > 0:
        require_pushup -= pushup_per_day
        require_situp -= situp_per_day
        require_looknang -= looknang_per_day
        require_running -= running_per_day

        total_days += 1

    print(total_days)


main()
