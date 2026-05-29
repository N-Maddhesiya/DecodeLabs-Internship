import csv


def split_field(value):
    if not value:
        return []
    return [item.strip().lower() for item in value.split("|") if item.strip()]


def load_movies(csv_path):
    movies = []

    with open(csv_path, mode="r", encoding="utf-8-sig", newline="") as file:
        reader = csv.DictReader(file, skipinitialspace=True)

        if reader.fieldnames is None:
            raise ValueError("CSV file is empty or header row is missing.")

        # Normalize headers like " Title " or BOM hidden headers
        reader.fieldnames = [name.strip().lower() for name in reader.fieldnames]

        required_columns = {"title", "genres", "language", "year", "mood", "keywords", "rating"}
        missing = required_columns - set(reader.fieldnames)
        if missing:
            raise ValueError(f"Missing columns in movies.csv: {', '.join(sorted(missing))}")

        for row in reader:
            row = {k.strip().lower(): v for k, v in row.items()}

            movie = {
                "title": row["title"].strip(),
                "genres": split_field(row["genres"]),
                "language": row["language"].strip(),
                "year": int(row["year"]),
                "mood": split_field(row["mood"]),
                "keywords": split_field(row["keywords"]),
                "rating": float(row["rating"])
            }
            movies.append(movie)

    return movies