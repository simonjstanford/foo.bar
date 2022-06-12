import unittest

from challenge2 import solution


class TestChallenge2(unittest.TestCase):
    def test_cases(self):
        cases = [
            (3, [1, 4, 7], [3, 6, -1]),
            (3, [7, 3, 5, 1], [-1, 7, 6, 3]),
            (5, [19, 14, 28], [21, 15, 29]),
        ]

        for case in cases:
            with self.subTest(msg=f"{case}"):
                result = solution(case[0], case[1])
                self.assertEqual(result, case[2])