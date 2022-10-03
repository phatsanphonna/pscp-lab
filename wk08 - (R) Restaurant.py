'''
[Recommend]
Week 8 - Restaurant
https://ejudge.it.kmitl.ac.th/problem/8235
กูขอเหอะ จงทำได้แบบไม่มีอุปสรรคด้วยเถิด สาธุ
'''


def main():
    '''
    Main Function
    ขอให้ฟังก์ชั่น "เมน" อันนี้รันโค้ดผ่านได้ด้วยดีเถิด
    '''

    total_order_price = float(input())  # ค่าอาหารทั้งหมด a บาท
    order_until_price = float(input())  # ทานครบ b บาท
    discount = 1 - float(input()) / 100  # จะได้ลด c%
    order_more_price = float(input())  # ถ้าสั่งอาหารราคา d บาทเพิ่ม

    if total_order_price + order_more_price >= order_until_price:
        discount_price = (total_order_price + order_more_price) * discount
    else:
        discount_price = total_order_price + order_more_price

    if total_order_price >= order_until_price:
        non_discount_price = total_order_price * discount
    else:
        non_discount_price = total_order_price

    different_price = abs(discount_price - non_discount_price)

    if discount_price < non_discount_price:
        print('Yes %.3f' % different_price)
    elif discount_price > non_discount_price:
        print('No %.3f' % different_price)
    else:
        print('Yes')


main()
