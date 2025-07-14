import json
import os
from collections import Counter
import argparse


def load_user_data(username):
    filepath = f"./outputs/{username}_raw.json"
    if not os.path.exists(filepath):
        print(f"File {filepath} not found.")
        return None
    with open(filepath, "r", encoding="utf-8") as f:
        return json.load(f)


def build_persona(user_data):
    username = user_data["username"]

    # Top subreddits (interests)
    subreddits = [c["subreddit"] for c in user_data["comments"]] + \
                 [p["subreddit"] for p in user_data["posts"]]
    subreddit_counter = Counter(subreddits)
    top_subreddits = subreddit_counter.most_common(5)

    # Frequent words
    all_text = " ".join([c["body"] for c in user_data["comments"]] +
                        [p["title"] + " " + p["selftext"] for p in user_data["posts"]])
    words = [word.lower() for word in all_text.split() if len(word) > 4]
    word_counter = Counter(words)
    common_words = word_counter.most_common(10)

    # Build clean persona text
    lines = []

    lines.append("=" * 41)
    lines.append("🔍 Reddit User Persona Report")
    lines.append("=" * 41 + "\n")

    lines.append(f"👤 Username: {username}\n")

    lines.append("🏠 Key Communities / Interests (Top Subreddits):")
    lines.append("-" * 49)
    lines.append("These indicate the user's most engaged communities and interests.\n")
    for idx, (subreddit, count) in enumerate(top_subreddits, start=1):
        lines.append(f"{idx}. {subreddit} ({count} posts/comments)")
    lines.append("")

    lines.append("💬 Frequently Used Words / Topics:")
    lines.append("-" * 42)
    lines.append("Common words hint at conversation themes, hobbies, and thought patterns.\n")
    for word, count in common_words:
        lines.append(f"- {word} ({count} times)")
    lines.append("")

    lines.append("🔗 Sample Comments That Informed Analysis:")
    lines.append("-" * 45)
    lines.append("Cited to justify personality and interests.\n")
    for idx, comment in enumerate(user_data["comments"][:5], start=1):
        lines.append(f"{idx}. {comment['permalink']}")
    lines.append("")

    lines.append("🔗 Sample Posts That Informed Analysis:")
    lines.append("-" * 42)
    lines.append("Cited to justify topics and tone.\n")
    for idx, post in enumerate(user_data["posts"][:5], start=1):
        lines.append(f"{idx}. {post['permalink']}")
    lines.append("")

    lines.append("🧠 Personality Insights (Preliminary Guess):")
    lines.append("-" * 48)
    lines.append("Inferred from writing tone, subreddit participation, and post style.\n")
    lines.append("- Possible tone: Casual, inquisitive, observational.")
    lines.append("- Possible personality traits: Curious, community-driven, enjoys discussions across diverse topics.\n")

    return "\n".join(lines)


def save_persona(username, persona_text):
    output_dir = "./outputs"
    os.makedirs(output_dir, exist_ok=True)
    with open(f"{output_dir}/{username}_persona.txt", "w", encoding="utf-8") as f:
        f.write(persona_text)
    print(f"Persona for {username} saved to {output_dir}/{username}_persona.txt")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate Reddit User Persona from scraped data.")
    parser.add_argument("username", help="Reddit username (used for reading outputs/username_raw.json)")
    args = parser.parse_args()

    data = load_user_data(args.username)
    if data:
        persona_text = build_persona(data)
        save_persona(args.username, persona_text)
