**📄 Reddit User Persona Generator**

    This project generates a User Persona from a given Reddit profile by analyzing posts and comments.
    It outputs a clean .txt file with key communities, vocabulary, and inferred personality traits.

🚀 How It Works :

    1️⃣ Scrapes Reddit posts and comments for a given username
    2️⃣ Analyzes the content to build a User Persona
    3️⃣ Outputs a .txt file containing the insights

📂 Project Structure :

    ├── outputs/               # Generated files stored here
    ├── src/                   # Source code
    │   ├── reddit_scraper.py  # Scrapes Reddit posts/comments via PRAW
    │   ├── persona_builder.py # Builds persona .txt
    ├── run_persona_cli.py     # Main CLI to run everything easily
    ├── requirements.txt       # Dependencies
    └── README.md               # You're reading this

🔧 Setup Instructions :

    1️⃣ Clone the Repository
        git clone https://github.com/YOUR_USERNAME/reddit_user_persona.git
        cd reddit_user_persona

    2️⃣ Create a praw.ini for Reddit API Credentials
        Inside the root directory, create a .env file:
        client_id=YOUR_CLIENT_ID
        client_secret=YOUR_CLIENT_SECRET
        user_agent=script:reddit.scraper:v1.0 (by /u/YOUR_USERNAME)

    3️⃣ Install Requirements
        pip install -r requirements.txt
    
🛠️ How to Run : Simply run the main CLI file:
    
        python3 run_persona_cli.py

✍️ Example CLI Flow : 

    =========================================
    🔍 Reddit User Persona Report
    =========================================

    👤 Username: Hungry-Move-6603

    🏠 Key Communities / Interests (Top Subreddits):
    -------------------------------------------------
    These indicate the user's most engaged communities and interests.

    1. lucknow (7 posts/comments)
    2. nagpur (2 posts/comments)
    3. IndiaUnfilter (1 posts/comments)
    4. indiasocial (1 posts/comments)
    5. amiugly (1 posts/comments)

    💬 Frequently Used Words / Topics:
    ------------------------------------------
    Common words hint at conversation themes, hobbies, and thought patterns.

    - common (2 times)
    - delhi (2 times)
    - friends? (2 times)
    - everyone (2 times)
    - caught (1 times)
    - without (1 times)
    - helmet (1 times)
    - license (1 times)
    - (close (1 times)
    - home). (1 times)

    🔗 Sample Comments That Informed Analysis:
    ---------------------------------------------
    Cited to justify personality and interests.

    1. https://www.reddit.com/r/nagpur/comments/1lyb0p5/a_very_odd_experience/n2ybup0/
    2. https://www.reddit.com/r/nagpur/comments/1lyb0p5/a_very_odd_experience/n2y7g0s/
    3. https://www.reddit.com/r/IndiaUnfilter/comments/1lw6ijt/people_are_smoking_hookah_in_the_middle_of_the/n2vkdpb/
    4. https://www.reddit.com/r/lucknow/comments/1lwbwu9/any_tiffin_service_providing_high_quality_food/n2kh3aq/
    5. https://www.reddit.com/r/lucknow/comments/1lwyhny/everyone_is_something_in_lko/n2ilsqh/

    🔗 Sample Posts That Informed Analysis:
    ------------------------------------------
    Cited to justify topics and tone.

    1. https://www.reddit.com/r/lucknow/comments/1lx50qm/productive_weekend_activities_in_lko/
    2. https://www.reddit.com/r/lucknow/comments/1lwyhny/everyone_is_something_in_lko/

    🧠 Personality Insights (Preliminary Guess):
    ------------------------------------------------
    Inferred from writing tone, subreddit participation, and post style.

    - Possible tone: Casual, inquisitive, observational.
    - Possible personality traits: Curious, community-driven, enjoys discussions across diverse topics.


Assignment Requirements Checklist :  

    ✅Takes Reddit username as input

    ✅Scrapes posts and comments

    ✅Builds user persona

    ✅Outputs .txt file

    ✅Cites posts/comments used

    ✅Clean CLI for easy usage

    ✅PEP-8 Compliant

    ✅README.md with instructions

🛡️ Note
Your Reddit API credentials are required for scraping.
We recommend creating a free Reddit App via Reddit Apps if you haven't already.

💼 License
This project is for assignment/demo purposes only.
All rights reserved to the author.
