"""
This script loads the initial json data and prepare the initial sql
insert statements to initialize the models when they are first loaded.
"""

import json
import os


def prepare_initial_data(filename):
    genre_set = set()
    output = []
    movie_dict = {}
    with open(filename, 'r') as _file:
        data = json.loads(_file.read())
    for index, item in enumerate(data):
        genres = item['genre']
        for genre in genres:
            genre_set.add(genre.strip())
        output.append({"fields": {"name": item["name"], "popularity": item["99popularity"],
                                  "director": item["director"], "imdb_score": item["imdb_score"]},
                       "model": "imdb-api.movie", "pk": index + 1})
        movie_dict[item["name"]] = index + 1

    genre_set = list(genre_set)
    genre_dict = {}
    for index, item in enumerate(genre_set):
        output.append({"fields": {"name": item}, "model": "imdb-api.genre", "pk": index + 1})
        genre_dict[item] = index + 1

    for index, item in enumerate(data):
        genres = item['genre']
        movie_id = movie_dict[item["name"]]
        for genre in genres:
            genre_id = genre_dict[genre.strip()]

            output.append({"fields": {"genre_id": genre_id, "movie_id": movie_id},
                       "model": "imdb-api.genremapping", "pk": index + 1})

    with open(os.path.join('fixtures', 'initial_data.json'), 'w') as _json_file:
        _json_file.write(json.dumps(output, indent=4))


def main():
    filename = os.path.join('data', 'imdb.json')
    prepare_initial_data(filename)

if __name__ == '__main__':
    main()
