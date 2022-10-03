'''
<Recommend>
Week 9 - Squid Game 3 - Tug-of-War
https://ejudge.it.kmitl.ac.th/problem/8261
'''


def main():
    '''Main Function'''

    team_a_force = 0
    team_b_force = 0

    for _ in range(10):
        force = int(input())
        team_a_force += force

    for _ in range(10):
        force = int(input())
        team_b_force += force

    if team_a_force == team_b_force:
        print('AB')
    elif team_a_force > team_b_force:
        print('B')
    else:
        print('A')


main()
