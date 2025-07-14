import praw
import os
from dotenv import load_dotenv
import argparse
import json

# Load credentials from .env
load_dotenv()

reddit = praw.Reddit(
    client_id=os.getenv("CLIENT_ID"),
    client_secret=os.getenv("CLIENT_SECRET"),
    user_agent=os.getenv("USER_AGENT")
)


def fetch_user_data(username):
    user = reddit.redditor(username)
    data = {
        "username": username,
        "comments": [],
        "posts": [],
    }
    
    # Fetch comments
    try:
        for comment in user.comments.new(limit=50):
            data["comments"].append({
                "body": comment.body,
                "subreddit": comment.subreddit.display_name,
                "permalink": f"https://www.reddit.com{comment.permalink}"
            })
    except Exception as e:
        print(f"Error fetching comments: {e}")

    # Fetch posts
    try:
        for post in user.submissions.new(limit=50):
            data["posts"].append({
                "title": post.title,
                "selftext": post.selftext,
                "subreddit": post.subreddit.display_name,
                "permalink": f"https://www.reddit.com{post.permalink}"
            })
    except Exception as e:
        print(f"Error fetching posts: {e}")

    return data


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Scrape Reddit user posts and comments.")
    parser.add_argument("username", help="Reddit username (not URL)")
    args = parser.parse_args()

    user_data = fetch_user_data(args.username)

    # Save raw data
    output_dir = "./outputs"
    os.makedirs(output_dir, exist_ok=True)
    with open(f"{output_dir}/{args.username}_raw.json", "w", encoding="utf-8") as f:
        json.dump(user_data, f, indent=4, ensure_ascii=False)

    print(f"Data for user {args.username} saved to {output_dir}/{args.username}_raw.json")
