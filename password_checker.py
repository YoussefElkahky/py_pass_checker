import string 

def load_common_passwords(filepath):
    """Load common passwords from a file and return as a set."""
    common = []
    try:
        with open(filepath, "r") as f:
            for line in f:
                common.append(line.strip().lower())
    except FileNotFoundError:
        print(f"warning: '{filepath}' not found. skipping common passwords check.")
    return common

def check_password(password, common_list):
    """Evaluate a password and return (score, feedback_list)."""
    score = 0
    feedback = []

    # Length check
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters.")

    if len(password) >= 12:
        score += 1

    # Character variety checks
    if any(c in string.ascii_uppercase for c in password):
        score += 1
    else:
        feedback.append("Add at least one uppercase letter.")

    if any(c in string.digits for c in password):
        score += 1
    else:
        feedback.append("Add at least one digit.")

    if any(c in string.punctuation for c in password):
        score += 1
    else:
        feedback.append("Add at least one special character (e.g., !, @, #).")

    # Common password check (overrides all other scoring)
    if password.lower() in common_list:
        score = 0
        feedback = ["This password is in the common-passwords list. Choose another."]

    return score, feedback

def main():
    strength_labels = {
        0: "weak", 1: "weak",
        2: "moderate", 3: "moderate",
        4: "strong", 5: "strong"
    }

    common_list = load_common_passwords("common-passwords.txt")

    while True:
        password = input("\nEnter a password to check (or 'exit' to quit): ")

        if password.lower() == "quit":
            print("Goodbye!")
            break

        if len(password) == 0:
            print("Password cannot be empty. Please try again.")
            continue

        score, feedback = check_password(password, common_list)
        label = strength_labels.get(score, "unknown")

        print(f"Strength: {label} ({score}/5)")

        if feedback:
            print("Suggestions:")
            for tip in feedback:
                print(f"  - {tip}")

        # Log the result(mask the actual password with asterisks)
        with open("Password_log.txt", "a") as log:
            log.write(f"Password: {'*' * len(password)} | Strength: {label} ({score}/5)\n")


main()