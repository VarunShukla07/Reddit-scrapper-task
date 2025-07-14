import subprocess
import os


def run_scraper(username):
    print("\n🔍 Running Reddit Scraper...")
    subprocess.run(["python3", "./reddit_scraper.py", username])


def run_persona(username):
    print("\n📝 Generating TXT Persona...")
    subprocess.run(["python3", "./persona_builder.py", username])


def main():
    print("="*50)
    print("🚀 Reddit User Persona Generator")
    print("="*50)
    username = input("\nEnter Reddit username (without '/u/' or URL): ").strip()

    run_scraper(username)
    run_persona(username)

    persona_file = f"./outputs/{username}_persona.txt"

    print("\n✅ Task Complete!")
    print(f"👉 Persona TXT stored at: {persona_file}")
    print("\nOpen it to view the detailed user analysis.\n")


if __name__ == "__main__":
    main()
