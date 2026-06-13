"""
CodSoft AI Internship - Task 4
Movie Recommendation System
- Content-Based Filtering (by genre)
- Collaborative Filtering (by user similarity)
Author: Bandi Vijaya Siva Sai Naga Jyothi
"""

import math

MOVIES = {
    1:  {"title": "Inception",            "genres": ["Sci-Fi", "Thriller", "Action"]},
    2:  {"title": "The Dark Knight",      "genres": ["Action", "Thriller", "Crime"]},
    3:  {"title": "Interstellar",         "genres": ["Sci-Fi", "Drama", "Adventure"]},
    4:  {"title": "The Matrix",           "genres": ["Sci-Fi", "Action", "Thriller"]},
    5:  {"title": "Avengers: Endgame",    "genres": ["Action", "Adventure", "Sci-Fi"]},
    6:  {"title": "The Godfather",        "genres": ["Crime", "Drama", "Thriller"]},
    7:  {"title": "Forrest Gump",         "genres": ["Drama", "Romance", "Comedy"]},
    8:  {"title": "The Notebook",         "genres": ["Romance", "Drama"]},
    9:  {"title": "Titanic",              "genres": ["Romance", "Drama", "History"]},
    10: {"title": "La La Land",           "genres": ["Romance", "Drama", "Music"]},
    11: {"title": "Toy Story",            "genres": ["Animation", "Comedy", "Adventure"]},
    12: {"title": "The Lion King",        "genres": ["Animation", "Drama", "Adventure"]},
    13: {"title": "Joker",               "genres": ["Crime", "Drama", "Thriller"]},
    14: {"title": "Parasite",            "genres": ["Thriller", "Drama", "Crime"]},
    15: {"title": "3 Idiots",            "genres": ["Comedy", "Drama", "Romance"]},
    16: {"title": "Bahubali",            "genres": ["Action", "Adventure", "Drama"]},
    17: {"title": "RRR",                 "genres": ["Action", "Drama", "Adventure"]},
    18: {"title": "KGF Chapter 2",       "genres": ["Action", "Crime", "Drama"]},
    19: {"title": "Pushpa",              "genres": ["Action", "Crime", "Drama"]},
    20: {"title": "Vikram",              "genres": ["Action", "Thriller", "Crime"]},
}

USER_RATINGS = {
    "Alice": {1: 5, 2: 4, 3: 5, 4: 4, 6: 3, 13: 4},
    "Bob":   {5: 5, 2: 4, 16: 5, 17: 5, 18: 4, 19: 4},
    "Carol": {7: 5, 8: 5, 9: 4, 10: 5, 15: 4, 12: 3},
    "David": {1: 4, 3: 5, 4: 5, 5: 3, 14: 4, 20: 4},
    "Eva":   {6: 5, 13: 5, 14: 4, 2: 4, 18: 3, 19: 5},
    "Frank": {11: 5, 12: 5, 15: 4, 7: 4, 10: 3, 8: 3},
}


def genre_similarity(movie_id_1, movie_id_2):
    genres1 = set(MOVIES[movie_id_1]["genres"])
    genres2 = set(MOVIES[movie_id_2]["genres"])
    intersection = len(genres1 & genres2)
    union = len(genres1 | genres2)
    return intersection / union if union != 0 else 0


def content_based_recommendations(liked_movie_id, top_n=5):
    scores = []
    for movie_id in MOVIES:
        if movie_id == liked_movie_id:
            continue
        sim = genre_similarity(liked_movie_id, movie_id)
        scores.append((movie_id, sim))
    scores.sort(key=lambda x: x[1], reverse=True)
    return scores[:top_n]


def cosine_similarity(user1_ratings, user2_ratings):
    common = set(user1_ratings.keys()) & set(user2_ratings.keys())
    if not common:
        return 0
    dot = sum(user1_ratings[m] * user2_ratings[m] for m in common)
    mag1 = math.sqrt(sum(user1_ratings[m] ** 2 for m in common))
    mag2 = math.sqrt(sum(user2_ratings[m] ** 2 for m in common))
    return dot / (mag1 * mag2) if (mag1 * mag2) != 0 else 0


def collaborative_recommendations(current_user_ratings, top_n=5):
    seen = set(current_user_ratings.keys())
    movie_scores = {}
    for other_user, other_ratings in USER_RATINGS.items():
        sim = cosine_similarity(current_user_ratings, other_ratings)
        if sim <= 0:
            continue
        for movie_id, rating in other_ratings.items():
            if movie_id not in seen:
                movie_scores[movie_id] = movie_scores.get(movie_id, 0) + sim * rating
    ranked = sorted(movie_scores.items(), key=lambda x: x[1], reverse=True)
    return ranked[:top_n]


def show_movies():
    print("\n  Available Movies:")
    print("  " + "-" * 55)
    for mid, info in MOVIES.items():
        genres = ", ".join(info["genres"])
        print(f"  [{mid:2}] {info['title']:<30} {genres}")
    print("  " + "-" * 55)


def print_recommendations(recs, label):
    print(f"\n  {label}")
    print("  " + "-" * 50)
    if not recs:
        print("  No recommendations found.")
        return
    for i, (movie_id, score) in enumerate(recs, 1):
        title = MOVIES[movie_id]["title"]
        genres = ", ".join(MOVIES[movie_id]["genres"])
        print(f"  {i}. {title:<30} | {genres}")
    print("  " + "-" * 50)


def main():
    print("=" * 55)
    print("    Movie Recommendation System")
    print("    CodSoft AI Internship - Task 4")
    print("=" * 55)

    while True:
        print("\n  Choose an option:")
        print("  1. Content-Based Recommendations (by genre)")
        print("  2. Collaborative Filtering (by similar users)")
        print("  3. Show all movies")
        print("  4. Exit")

        choice = input("\n  Your choice (1/2/3/4): ").strip()

        if choice == "1":
            show_movies()
            try:
                movie_id = int(input("\n  Enter a movie ID you like: ").strip())
                if movie_id not in MOVIES:
                    print("  Invalid movie ID. Try again.")
                    continue
                recs = content_based_recommendations(movie_id, top_n=5)
                liked = MOVIES[movie_id]["title"]
                print_recommendations(recs, f"Because you liked '{liked}':")
            except ValueError:
                print("  Please enter a valid number.")

        elif choice == "2":
            show_movies()
            print("\n  Rate at least 3 movies (score 1-5). Type 'done' when finished.")
            user_ratings = {}
            while True:
                mid_input = input("  Movie ID (or 'done'): ").strip()
                if mid_input.lower() == "done":
                    if len(user_ratings) < 3:
                        print("  Please rate at least 3 movies.")
                        continue
                    break
                try:
                    mid = int(mid_input)
                    if mid not in MOVIES:
                        print("  Invalid ID.")
                        continue
                    rating = int(input(f"  Your rating for '{MOVIES[mid]['title']}' (1-5): ").strip())
                    if rating < 1 or rating > 5:
                        print("  Rating must be between 1 and 5.")
                        continue
                    user_ratings[mid] = rating
                    print(f"  Saved!")
                except ValueError:
                    print("  Invalid input. Try again.")

            recs = collaborative_recommendations(user_ratings, top_n=5)
            print_recommendations(recs, "Recommended for you based on similar users:")

        elif choice == "3":
            show_movies()

        elif choice == "4":
            print("\n  Thanks for using the Recommendation System. Goodbye!")
            break

        else:
            print("  Invalid choice. Please enter 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()