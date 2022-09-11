"""Virus I"""

def main():
    """Virus I"""
    virus = input()
    cnt = 0
    for ooo in virus:
        if ooo == "o":
            cnt += 1
    print(cnt)
main()
