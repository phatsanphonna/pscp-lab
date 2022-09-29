'''Week 8 - ValidVar'''


# เนื้อหาในวันนี้คือการตั้งชื่อตัวแปร
# การตั้งชื่อตัวแปรนั้น มีกฎง่ายๆอยู่สี่ข้อ นอกเหนือจากกฎนี้แล้ว จะสามารถตั้งชื่อยาวเท่าไหร่ก็ได้ โดยที่ไม่ผิดไวยากรณ์
# โดยที่ประกอบด้วยอักษรภาษาอังกฤษพิมพ์เล็ก และพิมพ์ใหญ่ และตัวเลข และ Underscore (_) โดยชื่อตัวแปรจะเป็น Case-Sensitive

# 1. ห้ามมีอักขระพิเศษผสมอยู่ในชื่อตัวแปร (Punctuation) เช่น % $ < เป็นต้น ยกเว้น Underscore _ ได้เท่านั้น
# 2. ห้ามมี white space  เช่น เว้นวรรค อยู่ภายในตัวแปร (ยกเว้น whitespace ด้านหน้าและด้านหลังของตัวแปร) 
# 3. ห้ามขึ้นตัวชื่อตัวแปรด้วยตัวเลข
# 4. ห้ามตั้งชื่อซ้ำกับคำสงวน (Reserved Word) โดยที่ Reserved Word มีหลายตัวดังนี้
RESTRICTED_WORDS = 'if else elif while for True False continue break \
    return is in and or from as pass not def None'


def check_punctuation(char: str):
    return char == '_'



def main():
    '''Main Function'''

    loops = int(input())

    for _ in range(loops):
        variable_name = input()

        # ห้ามขึ้นตัวชื่อตัวแปรด้วยตัวเลข
        if variable_name[0].isnumeric():
            print('Invalid')
        elif 

