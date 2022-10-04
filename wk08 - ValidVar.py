'''
Week 8 - ValidVar
https://ejudge.it.kmitl.ac.th/problem/8227
'''

RESTRICTED_WORDS = 'if else elif while for True False continue break \
    return is in and or from as pass not def None'


def check_punctuation(char: str):
    '''Check punctuation'''

    return char in "!\"#$%&'()*+,-./:;<=>?[\\]^`{|}~."


def main():
    '''Main Function'''

    loops = int(input())

    for _ in range(loops):
        variable_name = input()

        # ห้ามขึ้นตัวชื่อตัวแปรด้วยตัวเลข
        if variable_name[0].isnumeric():
            print('Invalid')
            continue
        elif variable_name in RESTRICTED_WORDS:
            print('Invalid')
            continue

        have_punctuation = False

        for char in variable_name:
            if check_punctuation(char):
                have_punctuation = True
                break

        if have_punctuation:
            print('Invalid')
            continue

        if ' ' in variable_name:
            print('Invalid')
            continue

        print('Valid')


main()
