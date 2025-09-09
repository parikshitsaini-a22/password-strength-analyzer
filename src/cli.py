import argparse
from .analyzer import analyze_password
from .wordlist import generate_wordlist

def main():
    parser = argparse.ArgumentParser(description="Password Strength Analyzer & Wordlist Generator")
    parser.add_argument("--password", help="Password to analyze", required=True)
    parser.add_argument("--name", help="User name", default="")
    parser.add_argument("--pet", help="Pet name", default="")
    parser.add_argument("--years", help="Year range (e.g. 1990-2000)", default="")
    parser.add_argument("--out", help="Output wordlist file", default="wordlist.txt")
    args = parser.parse_args()

    score, feedback = analyze_password(args.password)
    print(f"Password Score: {score}/4")
    print(f"Feedback: {feedback}\n")

    wordlist = generate_wordlist(args.name, args.pet, args.years)
    with open(args.out, "w") as f:
        f.write("\n".join(wordlist))

    print(f"Wordlist saved to {args.out}")

if __name__ == "__main__":
    main()
