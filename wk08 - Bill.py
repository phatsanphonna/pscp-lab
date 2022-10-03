'''
Week 8 - Bill
https://ejudge.it.kmitl.ac.th/problem/8231
'''


def main():
    '''Main Function'''

    price = int(input())

    service_charge = price * 0.10

    if service_charge < 50:
        service_charge = 50
    elif service_charge > 1000:
        service_charge = 1000

    total_price = price + service_charge
    total_price = total_price * 1.07

    print('%.2f' % total_price)


main()
