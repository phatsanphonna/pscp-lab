'''Week 5 - Stepper II'''


def main():
    '''Main Function'''

    m_value = int(input())
    n_value = int(input())

    if n_value < m_value:
        for i in range(m_value, n_value-1, -1):
            print(i)
    elif n_value >= m_value:
        for i in range(m_value, n_value+1):
            print(i)


main()
