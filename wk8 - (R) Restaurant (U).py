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

    total_order_price = float(input())  # ค่าอาหารทั้งหมด a บาท
    order_until_price = float(input())  # ทานครบ b บาท
    discount = 1 - float(input()) / 100  # จะได้ลด c%
    order_more_price = float(input())  # ถ้าสั่งอาหารราคา d บาทเพิ่ม

    if order_until_price == 0 or order_more_price == 0:
        print('Yes')
        return

    if total_order_price >= order_until_price:
        total_order_price = total_order_price * discount

    total_to_pay = total_order_price + order_more_price
    discount_price = total_to_pay * discount

    if total_to_pay < order_until_price:
        print('Yes')
        return

    if discount_price == total_order_price:
        print('Yes')
    elif discount_price > total_order_price:
        print('No %.3f' % (discount_price - total_order_price))
    elif discount_price < total_order_price:
        print('Yes %.3f' % (total_order_price - discount_price))


main()
