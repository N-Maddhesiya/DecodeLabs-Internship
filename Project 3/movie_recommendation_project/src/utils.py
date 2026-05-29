def clean_list_input(text):
    if not text.strip():
        return []
    return [item.strip().lower() for item in text.split(",") if item.strip()]


def get_user_preferences():
    print("Enter your preferences below.")
    genres = clean_list_input(input("Preferred genres (action, drama, comedy, sci-fi): "))
    language = input("Preferred language (English/Hindi/etc.) or press Enter to skip: ").strip()
    moods = clean_list_input(input("Preferred moods (exciting, funny, emotional, intense): "))
    keywords = clean_list_input(input("Any keywords (space, hero, school, friendship): "))

    year_input = input("Preferred minimum year or press Enter to skip: ").strip()
    min_year = int(year_input) if year_input.isdigit() else None

    return {
        "genres": genres,
        "language": language,
        "moods": moods,
        "keywords": keywords,
        "min_year": min_year
    }