# py_pass_checker

A simple Python script that checks password strength, including a check against a list of commonly used (easily guessable) passwords.

## What It Does

`password_checker.py` evaluates a given password's strength — typically checking things like length, use of uppercase/lowercase letters, numbers, and special characters — and cross-references it against `common_passwords.txt` to flag weak or commonly used passwords.

## Requirements

- Python 3.x (no external dependencies required, uses standard library)

## Usage

```bash
python3 password_checker.py
```

You'll be prompted to enter a password, and the script will report its strength and whether it matches a known common password.

## Files

| File | Description |
|---|---|
| `password_checker.py` | Main script — checks password strength and common-password matches. |
| `common_passwords.txt` | Wordlist of common/weak passwords used for comparison. |

## License

This project is open source and available for educational use.
