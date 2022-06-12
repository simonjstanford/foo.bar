import unittest

from challenge3 import solution


class TestChallenge3(unittest.TestCase):
    def test_cases(self):
        cases = [
            (0, 1, 3),
            (19, 36, 1),    
        ]

        for case in cases:
            with self.subTest(msg=f"{case}"):
                result = solution(case[0], case[1])
                self.assertEqual(result, case[2])