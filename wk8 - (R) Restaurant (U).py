'''
[Recommend]
Week 8 - Restaurant
กูขอเหอะ จงทำได้แบบไม่มีอุปสรรคด้วยเถิด สาธุ
'''


def main():
    '''
    Main Function
    ขอให้ฟังก์ชั่น "เมน" อันนี้รันโค้ดผ่านได้ด้วยดีเถิด
    '''

    a_value = float(input())  # ค่าอาหารทั้งหมด a บาท
    b_value = float(input())  # ทานครบ b บาท
    c_value = 1 - float(input()) / 100  # จะได้ลด c%
    d_value = float(input())  # ถ้าสั่งอาหารราคา d บาทเพิ่ม

    if b_value == 0 or d_value == 0:
        print('Yes')
        return

    total_to_pay = a_value + d_value
    discount_price = total_to_pay * c_value

    if total_to_pay < b_value:
        print('Yes')
        return

    if discount_price == a_value:
        print('Yes')
    elif discount_price > a_value:
        print('No %.3f' % (discount_price - a_value))
    elif discount_price < a_value:
        print('Yes %.3f' % (a_value - discount_price))


main()
