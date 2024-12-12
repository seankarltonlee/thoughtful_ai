import unittest
from robots import sort_package

class TestPackageSorter(unittest.TestCase):
    
    def test_standard_packages(self):
        test_cases = [
            (10, 10, 10, 10),
            (50, 50, 50, 19),
            (100, 100, 99, 15)
        ]
        for w, h, l, m in test_cases:
            with self.subTest(w=w, h=h, l=l, m=m):
                self.assertEqual(sort_package(w, h, l, m), "STANDARD")
    
    def test_special_packages(self):
        test_cases = [
            (100, 100, 100, 15),
            (151, 50, 50, 15),
            (50, 160, 50, 15),
            (50, 50, 155, 15),
            (100, 100, 90, 20)
        ]
        for w, h, l, m in test_cases:
            with self.subTest(w=w, h=h, l=l, m=m):
                self.assertEqual(sort_package(w, h, l, m), "SPECIAL")
    
    def test_rejected_packages(self):
        test_cases = [
            (100, 100, 100, 25),
            (151, 50, 50, 20),
            (200, 200, 200, 30),
            (200, 200, 200, 30)
        ]
        for w, h, l, m in test_cases:
            with self.subTest(w=w, h=h, l=l, m=m):
                self.assertEqual(sort_package(w, h, l, m), "REJECTED")
    
    def test_edge_cases(self):
        test_cases = [
            (99.99, 100, 100, 15),
            (100, 100, 100, 15),
            (149.99, 50, 50, 15),
            (150, 50, 50, 15),
            (100, 100, 90, 19.99),
            (100, 100, 90, 20)
        ]
        expected = ["STANDARD", "SPECIAL", "STANDARD", "SPECIAL", "STANDARD", "SPECIAL"]
        for (w, h, l, m), exp in zip(test_cases, expected):
            with self.subTest(w=w, h=h, l=l, m=m):
                self.assertEqual(sort_package(w, h, l, m), exp)
    
    def test_invalid_inputs(self):
        invalid_inputs = [
            (-1, 10, 10, 10),
            (10, -1, 10, 10),
            (10, 10, -1, 10),
            (10, 10, 10, -1)
        ]
        for w, h, l, m in invalid_inputs:
            with self.subTest(w=w, h=h, l=l, m=m):
                with self.assertRaises(ValueError):
                    sort_package(w, h, l, m)