'''Week 5 - Stepper II'''


def main():
    '''Main Function'''

    m_value = int(input())
    n_value = int(input())

    mn_value = abs(m_value - n_value) + 1

    for i in range(mn_value):
        print(m_value + i)


main()
