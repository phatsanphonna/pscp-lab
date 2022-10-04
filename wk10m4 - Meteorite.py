'''
Midterm 4 - Meteorite
Week 10 - Meteorite
https://ejudge.it.kmitl.ac.th/problem/8272
'''


def main():
    '''Main Function'''

    meteorite_weight = float(input())
    meteorite_split = int(input())
    safe_weight = float(input())

    missile_shoot = 0
    missile_indicator = 0

    while not meteorite_weight < safe_weight:
        meteorite_weight = meteorite_weight / meteorite_split
        missile_shoot += meteorite_split ** missile_indicator
        missile_indicator += 1

    print(missile_shoot)


main()
