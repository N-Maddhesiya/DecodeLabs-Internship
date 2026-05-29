def score_movie(movie, preferences):
    score = 0
    reasons = []

    user_genres = set(preferences["genres"])
    user_moods = set(preferences["moods"])
    user_keywords = set(preferences["keywords"])
    user_language = preferences["language"].lower().strip()
    min_year = preferences["min_year"]

    movie_genres = set(movie["genres"])
    movie_moods = set(movie["mood"])
    movie_keywords = set(movie["keywords"])

    genre_matches = user_genres & movie_genres
    if genre_matches:
        score += 2 * len(genre_matches)
        reasons.append(f"matching genres: {', '.join(sorted(genre_matches))}")

    if user_language and movie["language"].lower() == user_language:
        score += 3
        reasons.append(f"language matches: {movie['language']}")

    mood_matches = user_moods & movie_moods
    if mood_matches:
        score += 2 * len(mood_matches)
        reasons.append(f"matching mood: {', '.join(sorted(mood_matches))}")

    keyword_matches = user_keywords & movie_keywords
    if keyword_matches:
        score += 1 * len(keyword_matches)
        reasons.append(f"matching keywords: {', '.join(sorted(keyword_matches))}")

    if min_year and movie["year"] >= min_year:
        score += 1
        reasons.append(f"released after {min_year}")

    if movie["rating"] >= 8.5:
        score += 1
        reasons.append("high rating bonus")

    return score, reasons


def recommend_movies(movies, preferences, top_n=5):
    scored_movies = []

    for movie in movies:
        score, reasons = score_movie(movie, preferences)
        scored_movies.append({
            "title": movie["title"],
            "genres": ", ".join(movie["genres"]),
            "language": movie["language"],
            "year": movie["year"],
            "rating": movie["rating"],
            "score": score,
            "reasons": reasons
        })

    scored_movies.sort(key=lambda x: x["score"], reverse=True)

    return [movie for movie in scored_movies if movie["score"] > 0][:top_n]