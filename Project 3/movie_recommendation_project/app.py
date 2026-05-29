from src.data_loader import load_movies
from src.recommender import recommend_movies
from src.utils import get_user_preferences


def main():
    print("\n=== Movie Recommendation System ===\n")

    movies = load_movies("data/movies.csv")
    preferences = get_user_preferences()

    recommendations = recommend_movies(movies, preferences, top_n=5)

    if not recommendations:
        print("\nNo recommendations found. Try different preferences.")
        return

    print("\nTop Recommendations:\n")
    for i, movie in enumerate(recommendations, start=1):
        print(f"{i}. {movie['title']} ({movie['year']})")
        print(f"   Genre     : {movie['genres']}")
        print(f"   Language  : {movie['language']}")
        print(f"   Rating    : {movie['rating']}")
        print(f"   Score     : {movie['score']}")
        print(f"   Why       : {', '.join(movie['reasons']) if movie['reasons'] else 'General match'}")
        print()


if __name__ == "__main__":
    main()