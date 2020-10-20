import unittest
from kata import Score
from unittest.mock import Mock
from kata import Game


class test(unittest.TestCase):
    def test_failed(self):
        self.assertEqual(True, True)

    def test_return_one_when_one_rolls_are_down(self):
        res = ["1-"]
        self.assertEqual(Score(res), 1)

    def test_return_two_when_two_rolls_are_down(self):
        res = ["2-"]
        self.assertEqual(Score(res), 2)

    def test_return_3_when_one_and_two_rolls_down(self):
        res = ["12"]
        self.assertEqual(Score(res), 3)

    def test_return_4_when_dash_and_four(self):
        res = ["-4"]
        self.assertEqual(Score(res), 4)

    def test_return_0_when_0_and_0(self):
        res = ["--"]
        self.assertEqual(Score(res), 0)

    def test_return_10_when_spare(self):
        res = ["5/"]
        self.assertEqual(Score(res), 10)

    def test_return_10_when_strike(self):
        res = ["X"]
        self.assertEqual(Score(res), 10)

    def test_return_real_score_when_spare(self):
        res = ["5/", "12"]
        self.assertEqual(Score(res), 14)

    def test_return_real_score_when_spare_1(self):
        res = ["5/", "1-"]
        self.assertEqual(Score(res), 12)

    def test_return_real_score_when_spare_2(self):
        res = ["5/", "--"]
        self.assertEqual(Score(res), 10)

    def test_return_score_when_2_spares(self):
        res = ["5/", "5/"]
        self.assertEqual(25, Score(res))

    def test_return_score_when_strike_and_strike(self):
        res = ["X", "X"]
        self.assertEqual(30, Score(res))

    def test_return_score_when_three_three(self):
        res = ["12", "12", "12"]
        self.assertEqual(9, Score(res))

    def test_return_score_when_three_three_2(self):
        res = ["-3", "6-", "--"]
        self.assertEqual(9, Score(res))

    def test_return_score_when_three_three_3(self):
        res = ["--", "-9", "--"]
        self.assertEqual(9, Score(res))

    def test_return_score_when_spare_and_two_three(self):
        res = ["5/", "-3", "-3"]
        self.assertEqual(16, Score(res))

    def test_return_score_when_spare_and_two_three_1(self):
        res = ["-3", "5/", "-3"]
        self.assertEqual(16, Score(res))

    def test_return_score_when_spare_and_two_three_2(self):
        res = ["-3", "-3", "5/"]
        self.assertEqual(16, Score(res))

    def test_return_score_when_spare_and_two_three_3(self):
        res = ["5/", "5/", "-3"]
        self.assertEqual(28, Score(res))

    def test_return_score_when_spare_and_two_three_4(self):
        res = ["5/", "5/", "-3"]
        self.assertEqual(28, Score(res))

    def test_return_score_when_spare_and_two_three_5(self):
        res = ["5/", "5/", "5/"]
        self.assertEqual(40, Score(res))

    def test_return_score_when_spare_and_two_three_6(self):
        res = ["X", "12", "12"]
        self.assertEqual(19, Score(res))

    def test_return_score_when_spare_and_two_three_7(self):
        res = ["X", "-5", "12"]
        self.assertEqual(23, Score(res))

    def test_return_score_when_spare_and_two_three_8(self):
        res = ["X", "5/", "12"]
        self.assertEqual(34, Score(res))

    def test_return_score_when_spare_and_two_three_8(self):
        res = ["X", "3/", "12"]
        self.assertEqual(34, Score(res))

    def test_with_mock(self):
        mocker1 = Mock()
        mocker2 = Mock()
        mocker1.play = play_mock1
        mocker1.expect_value = 100
        mocker2.play = play_mock2
        mocker2.expected_value = 0
        game = Game(mocker1, mocker2)
        game.play()
        game.pretty_printer()
        # self.assertEqual(Score(game.scores_one), mocker1.expect_value)
        self.assertEqual(mocker2.expected_value, Score(game.scores_two))


def play_mock1():
    return "X"

def play_mock2():
    return "--"


if __name__ == '__main__':
    unittest.main()
