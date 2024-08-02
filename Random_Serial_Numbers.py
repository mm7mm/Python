import string
import random

def make_serial(count):
    # تحديد مجموعة الأحرف الممكنة التي تتضمن الأحرف الأبجدية الكبيرة والصغيرة والأرقام
    all_Chars = string.ascii_letters + string.digits
    
    # حساب عدد الأحرف المتاحة
    chars_conut = len(all_Chars)
    print(chars_conut)  # طباعة عدد الأحرف المتاحة
    
    # قائمة لتخزين الأحرف المختارة
    serial_list = []
    
    # إنشاء سلسلة من الأحرف العشوائية بطول محدد بـ count
    while count > 0:
        # اختيار رقم عشوائي يتوافق مع فهرس حرف من مجموعة الأحرف
        random_number = random.randint(0, chars_conut - 1)
        
        # الحصول على الحرف العشوائي بناءً على الرقم العشوائي
        random_character = all_Chars[random_number]
        
        # إضافة الحرف العشوائي إلى قائمة الأحرف
        serial_list.append(random_character)
        
        # تقليل عدد الأحرف المتبقية
        count -= 1  # count = count - 1
    
    # طباعة السلسلة العشوائية المكونة من الأحرف
    print("".join(serial_list))

# استدعاء الدالة لإنشاء سلسلة عشوائية بطول 50 حرف
make_serial(50)