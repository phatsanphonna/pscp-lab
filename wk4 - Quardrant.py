"""Week 4 - Quadrant"""


def main():
    """Main Function"""

    xvalue = int(input())
    yvalue = int(input())
    
    if xvalue == 0 and yvalue == 0:
        print('O')
    elif xvalue > 0 and yvalue > 0:
        print("Q1")
    elif xvalue < 0 and yvalue > 0:
        print("Q2")
    elif xvalue < 0 and yvalue < 0:
        print("Q3")
    elif xvalue > 0 and yvalue < 0:
        print("Q4")
    elif xvalue == 0:
        print("Y")
    elif yvalue == 0:
        print("X")


main()
