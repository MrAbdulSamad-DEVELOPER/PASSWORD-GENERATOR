"""Tests for the password generator."""

import string
import unittest

from password_gen import generate_password, password_strength


class TestPasswordGen(unittest.TestCase):
    def test_default_length(self):
        self.assertEqual(len(generate_password()), 12)

    def test_custom_length(self):
        self.assertEqual(len(generate_password(20)), 20)

    def test_too_short_fails(self):
        with self.assertRaises(ValueError):
            generate_password(3)

    def test_contains_upper_digit_symbol(self):
        password = generate_password(16)
        self.assertTrue(any(c.isupper() for c in password))
        self.assertTrue(any(c.isdigit() for c in password))
        self.assertTrue(any(c in "!@#$%^&*()-_=+" for c in password))

    def test_only_lowercase_when_options_off(self):
        password = generate_password(10, use_upper=False, use_digits=False, use_symbols=False)
        self.assertTrue(all(c in string.ascii_lowercase for c in password))

    def test_strength_weak(self):
        self.assertEqual(password_strength("abc"), "Weak")

    def test_strength_good(self):
        self.assertEqual(password_strength("Abcdef123"), "Good")

    def test_strength_strong(self):
        self.assertEqual(password_strength("Abcdef123!@#x"), "Strong")


if __name__ == "__main__":
    unittest.main()
