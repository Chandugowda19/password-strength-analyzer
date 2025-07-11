import argparse
from analyzer import analyze_password
from generator import collect_inputs, generate_variations, save_wordlist

def main():
    parser = argparse.ArgumentParser(description="🔐 Password Strength Analyzer & Wordlist Generator")
    parser.add_argument("-p", "--password", help="Password to analyze")
    parser.add_argument("--name", help="User's name")
    parser.add_argument("--dob", help="Date of birth (YYYY-MM-DD)")
    parser.add_argument("--pet", help="Pet's name")
    args = parser.parse_args()

    if args.password:
        print("🔍 Analyzing password...")
        result = analyze_password(args.password)
        print(f"Password Score: {result['score']} / 4")
        print(f"Estimated Crack Time: {result['crack_time']}")
        print("Feedback:", result['feedback']['suggestions'] or "Good password!")

    if args.name or args.dob or args.pet:
        print("\n🛠️ Generating wordlist...")
        words = collect_inputs(args.name or "", args.dob or "", args.pet or "")
        variations = generate_variations(words)
        save_wordlist(variations)
        print(f"✅ Wordlist saved as 'wordlist_output.txt' with {len(variations)} entries.")

if __name__ == "__main__":
    main()
