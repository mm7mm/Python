# استيراد مكتبة unittest لاختبار الوحدات
import unittest

# التحقق من صحة تعبير معين باستخدام assert
assert 3 * 4 == 12, "should Be 12"  # تحقق من أن 3 مضروبة في 4 تساوي 12

# تعريف اختبار بسيط كدالة
def test_case_one():
    assert 5 * 4 == 20, "should Be 20"  # تحقق من أن 5 مضروبة في 4 تساوي 20

# تعريف اختبار بسيط آخر كدالة
def test_case_two():
    assert 5 * 6 == 30, "should Be 30"  # تحقق من أن 5 مضروبة في 6 تساوي 30

# تنفيذ الاختبارات البسيطة إذا كان هذا الملف هو الملف الرئيسي
if __name__ == "__main__":
    test_case_one()  # تنفيذ الاختبار الأول
    test_case_two()  # تنفيذ الاختبار الثاني
    print("All test cases passed")  # طباعة رسالة إذا كانت جميع الاختبارات ناجحة

# تعريف مجموعة اختبارات باستخدام unittest
class MyTestCase(unittest.TestCase):
    # اختبار للتأكد من أن 100 أكبر من 10
    def test_case_one(self):
        self.assertTrue(100 > 10, "Should Be True")  # تحقق من أن التعبير هو True
  
    # اختبار للتأكد من أن 5 * 6 تساوي 30
    def test_case_two(self):
        self.assertEqual(5 * 6, 30, "Should Be 30")  # تحقق من أن الناتج يساوي 30

    # اختبار للتأكد من أن 100 ليس أصغر من 10
    def test_case_three(self):
        self.assertFalse(100 < 10, "Should Be True")  # تحقق من أن التعبير هو False

# تنفيذ اختبارات الوحدة باستخدام unittest إذا كان هذا الملف هو الملف الرئيسي
if __name__ == "__main__":
    unittest.main()  # تشغيل جميع اختبارات الوحدة المعرفة في MyTestCase
