# PASSWORD-GENERATOR

A small Python tool that generates secure random passwords and checks password strength.

## Features

- Random passwords with letters, digits and symbols
- Choose the length (minimum 4)
- Guarantees at least one of each selected character type
- Password strength check: Weak / Good / Strong

## Run it

```bash
python password_gen.py
```

## Run the tests

```bash
python -m unittest test_password_gen.py -v
```

## Project structure

- `password_gen.py` — password generation and strength check
- `test_password_gen.py` — unit tests (8 tests)
