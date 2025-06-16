

import string
import secrets

def generate_password(length=16, use_upper=True, use_lower=True, use_digits=True, use_symbols=True):
    if length < 8:
        raise ValueError("Password too short. Unless you WANT to get hacked. Bold move.")

    character_pool = ''
    if use_upper:
        character_pool += string.ascii_uppercase
    if use_lower:
        character_pool += string.ascii_lowercase
    if use_digits:
        character_pool += string.digits
    if use_symbols:
        character_pool += string.punctuation

    if not character_pool:
        raise ValueError("You selected NO character types. What exactly do you expect me to do, wizardry?")

    # Ensure at least one character from each selected type
    password = []
    if use_upper:
        password.append(secrets.choice(string.ascii_uppercase))
    if use_lower:
        password.append(secrets.choice(string.ascii_lowercase))
    if use_digits:
        password.append(secrets.choice(string.digits))
    if use_symbols:
        password.append(secrets.choice(string.punctuation))

    # Fill in the rest randomly, like your life decisions
    password += [secrets.choice(character_pool) for _ in range(length - len(password))]

    # Mix it like a DJ
    secrets.SystemRandom().shuffle(password)

    return ''.join(password)

def password_strength(password):
    score = 0
    if any(c.islower() for c in password): score += 1
    if any(c.isupper() for c in password): score += 1
    if any(c.isdigit() for c in password): score += 1
    if any(c in string.punctuation for c in password): score += 1
    if len(password) >= 12: score += 1

    levels = {
        5: "🔐 Fort Knox would be jealous.",
        4: "💪 Pretty solid. Could stop your nosy neighbor.",
        3: "🧐 Meh. Might keep out your little cousin.",
        2: "😬 This won't last 5 minutes on the dark web.",
        1: "💀 My cat could guess this.",
        0: "🤡 Did you just type 'password'? Shame."
    }
    return levels[score]

def main():
    print("\n🎉 Welcome to the World's Most Mediocre Password Generator 🎉")
    print("Built with sarcasm, secured with secrets. Let’s go!\n")

    try:
        length = int(input("🧠 Desired password length (minimum 8, or face the consequences): "))
        use_upper = input("Include UPPERCASE? (y/n): ").strip().lower() == 'y'
        use_lower = input("Include lowercase? (y/n): ").strip().lower() == 'y'
        use_digits = input("Include digits (0-9)? (y/n): ").strip().lower() == 'y'
        use_symbols = input("Include fancy symbols ($%@&)? (y/n): ").strip().lower() == 'y'

        password = generate_password(length, use_upper, use_lower, use_digits, use_symbols)

        print("\n✨ Here’s your totally unpredictable, hacker-repelling password:")
        print(f"🔐 {password}")
        print(f"🧪 Strength Score: {password_strength(password)}\n")

        print("📌 Pro Tip: Don’t write this on a sticky note and slap it on your monitor. You’re not in a 90s sitcom.")
    except ValueError as ve:
        print(f"\n🚨 Error Detected: {ve}")
        print("Try again, this time with feeling.")

if __name__ == "__main__":
    main()
