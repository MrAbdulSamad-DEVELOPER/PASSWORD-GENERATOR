"""Secure password generator.

Generate random passwords with a chosen length and character sets,
and check how strong a password is.
"""

import secrets
import string

LOWER = string.ascii_lowercase
UPPER = string.ascii_uppercase
DIGITS = string.digits
SYMBOLS = "!@#$%^&*()-_=+"


def generate_password(length=12, use_upper=True, use_digits=True, use_symbols=True):
    if length < 4:
        raise ValueError("Password length must be at least 4.")
    chars = LOWER
    required = [secrets.choice(LOWER)]
    if use_upper:
        chars += UPPER
        required.append(secrets.choice(UPPER))
    if use_digits:
        chars += DIGITS
        required.append(secrets.choice(DIGITS))
    if use_symbols:
        chars += SYMBOLS
        required.append(secrets.choice(SYMBOLS))
    password = required + [secrets.choice(chars) for _ in range(length - len(required))]
    secrets.SystemRandom().shuffle(password)
    return "".join(password)


def password_strength(password):
    score = 0
    if len(password) >= 12:
        score += 1
    if any(c.islower() for c in password):
        score += 1
    if any(c.isupper() for c in password):
        score += 1
    if any(c.isdigit() for c in password):
        score += 1
    if any(c in SYMBOLS for c in password):
        score += 1
    if score <= 2:
        return "Weak"
    if score <= 4:
        return "Good"
    return "Strong"


def main():
    password = generate_password(16)
    print(f"Generated password: {password}")
    print(f"Strength: {password_strength(password)}")


if __name__ == "__main__":
    main()
