import numpy as np

# Item database with category scores (0-10)
ITEMS = {
    "Action Movie": {"action": 9, "comedy": 3, "drama": 4, "romance": 2, "thriller": 8, "scifi": 6},
    "Romantic Comedy": {"action": 2, "comedy": 8, "drama": 6, "romance": 9, "thriller": 1, "scifi": 1},
    "Sci-Fi Epic": {"action": 7, "comedy": 2, "drama": 5, "romance": 2, "thriller": 6, "scifi": 10},
    "Drama Series": {"action": 3, "comedy": 4, "drama": 9, "romance": 6, "thriller": 4, "scifi": 2},
    "Horror Thriller": {"action": 5, "comedy": 1, "drama": 5, "romance": 1, "thriller": 10, "scifi": 3},
    "Animated Family": {"action": 4, "comedy": 9, "drama": 3, "romance": 2, "thriller": 1, "scifi": 4},
}

CATEGORIES = ["action", "comedy", "drama", "romance", "thriller", "scifi"]


def cosine_similarity(vec_a, vec_b):
    a = np.array(vec_a)
    b = np.array(vec_b)
    dot_product = np.dot(a, b)
    magnitude_a = np.linalg.norm(a)
    magnitude_b = np.linalg.norm(b)
    if magnitude_a == 0 or magnitude_b == 0:
        return 0.0
    return dot_product / (magnitude_a * magnitude_b)


def main():
    print("=" * 60)
    print("   AI RECOMMENDATION LOGIC - DecodeLabs Project 3")
    print("=" * 60)

    # 1. Take user input (Pre-defined user who loves Sci-Fi & Action, hates Romance)
    user_prefs = {"action": 9, "comedy": 3, "drama": 4, "romance": 1, "thriller": 7, "scifi": 10}

    print("\n[1] User Preferences Loaded:")
    for cat, val in user_prefs.items():
        bar = "█" * val + "░" * (10 - val)
        print(f"    {cat.capitalize():<12} : {bar} ({val}/10)")

    # 2. Match preferences using Cosine Similarity logic
    print("\n[2] Calculating Similarity Scores...")
    user_vector = [user_prefs[cat] for cat in CATEGORIES]

    scores = {}
    for item_name, item_attrs in ITEMS.items():
        item_vector = [item_attrs[cat] for cat in CATEGORIES]
        similarity = cosine_similarity(user_vector, item_vector)
        scores[item_name] = round(similarity, 4)

    # Sort items by highest similarity score
    ranked_items = sorted(scores.items(), key=lambda x: x[1], reverse=True)

    # 3. Display recommended items
    print("\n[3] 🏆 Top Recommendations for You:")
    print("-" * 60)
    for i, (item, score) in enumerate(ranked_items, 1):
        match_percent = score * 100
        bar_length = int(score * 30)
        bar = "█" * bar_length + "░" * (30 - bar_length)
        print(f"  {i}. {item:<20} | Match: {match_percent:>5.1f}% [{bar}]")

    print("\nProject 3 completed successfully!")


if __name__ == "__main__":
    main()