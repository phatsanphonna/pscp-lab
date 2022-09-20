'''Week 5 - BrickBridge'''


def main():
    '''Main Function'''

    small_brick = int(input())
    large_brick = int(input())
    goal = int(input())

    large_brick_need = goal // 5

    if large_brick_need < large_brick:
        large_brick = large_brick_need

    small_brick_use = goal - large_brick * 5

    if ()