import unittest
from roman_letter import convert_number_to_roman_letter

class RomanLetterTest(unittest.TestCase):

    def test_failed(self):
        self.assertNotEqual(True, False)

    def test_is_one(self):
        one = convert_number_to_roman_letter(1)
        self.assertEqual(one, "I")

    def test_is_four(self):
        four = convert_number_to_roman_letter(4)
        self.assertEqual(four, "IV")

    def test_is_five(self):
        five = convert_number_to_roman_letter(5)
        self.assertEqual(five, "V")

    def test_is_nine(self):
        nine = convert_number_to_roman_letter(9)
        self.assertEqual(nine, "IX")

    def test_is_ten(self):
        ten = convert_number_to_roman_letter(10)
        self.assertEqual(ten, "X")

    def test_is_fifty(self):
        fifty = convert_number_to_roman_letter(50)
        self.assertEqual(fifty, "L")

    def test_is_three(self):
        thirteen = convert_number_to_roman_letter(3)
        self.assertEqual(thirteen, "III")

    def test_is_between_six(self):
        six = convert_number_to_roman_letter(6)
        self.assertEqual(six, "VI")

    def test_is_eleven(self):
        eleven = convert_number_to_roman_letter(11)
        self.assertEqual(eleven, "XI")

    def test_is_twelve(self):
        twelve = convert_number_to_roman_letter(12)
        self.assertEqual(twelve, "XII")

    def test_is_fifteen(self):
        fifteen = convert_number_to_roman_letter(15)
        self.assertEqual(fifteen, "XV")

    def test_is_sixteen(self):
        sixteen = convert_number_to_roman_letter(16)
        self.assertEqual(sixteen, "XVI")

    def test_is_twenty(self):
        twenty = convert_number_to_roman_letter(20)
        self.assertEqual(twenty, "XX")
    def test_is_twenty_two(self):
        twenty_two = convert_number_to_roman_letter(22)
        self.assertEqual(twenty_two, "XXII")

    def test_is_twenty_five(self):
        twenty_five = convert_number_to_roman_letter(25)
        self.assertEqual(twenty_five, "XXV")

    def test_is_thirty_nine(self):
        thirty_nine = convert_number_to_roman_letter(39)
        self.assertEqual(thirty_nine, "XXXIX")


if __name__ == '__main__':
    unittest.main()
