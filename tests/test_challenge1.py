import unittest

from challenge1 import solution


class TestChallenge1(unittest.TestCase):
    def test_cases(self):
        cases = [
            (0, '23571'),
            (3, '71113'),    
        ]

        for case in cases:
            with self.subTest(msg=f"{case}"):
                result = solution(case[0])
                self.assertEqual(result, case[1])