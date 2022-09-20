'''
[Recommend]
Week 6 - Key
'''

# 1) หาผลรวมของตัวเลขทั้ง 13 หลัก
# 2) เอาค่า 3 หลักสุดท้าย คูณด้วย 10
# 3) เอาค่าจากข้อ 1) และ 2) มาบวกกัน จะได้เป็น Key
# ถ้าหากได้ค่ามากกว่าสี่หลักให้ตัดเอาแค่สี่หลักสุดท้าย
# แต่ถ้าค่าน้อยกว่า 1,000 ให้บวก เพิ่ม 1,000 ก็จะได้เลขสี่หลัก ซึ่งเป็น Key


def main():
    '''Main Function'''

    id_number = input()

    # 1) Find sum of 13-digit id_number
    id_sum = 0

    for num in id_number:
        id_sum += int(num)

    # 2) Take last 3 digits of id_number and multiply by 10
    last_3_digts_id_num = int(id_number[-3:]) * 10

    # 3) Combine first and second steps together
    key = id_sum + last_3_digts_id_num

    if key > 9999:
        key = str(key)[-4:]
    elif key < 1000:
        key += 1000

    print(key)


main()
