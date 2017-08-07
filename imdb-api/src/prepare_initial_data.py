"""
Takes a json file as a sample input and creates initial data file
which can be used to populate the database initially.
"""

import json
import os


def prepare_initial_data(filename):
    genre_set = set()
    output = []
    movie_dict = {}
    with open(filename, 'r') as _file:
        data = json.loads(_file.read())
    # Iterate over the data and create a distinct genre set.
    for index, item in enumerate(data):
        genres = item['genre']
        for genre in genres:
            genre_set.add(genre.strip())
        # create data for movie table.
        output.append({"fields": {"name": item["name"], "popularity": item["99popularity"],
                                  "director": item["director"], "imdb_score": item["imdb_score"]},
                       "model": "imdb-api.movie", "pk": index + 1})
        movie_dict[item["name"]] = index + 1

    genre_set = list(genre_set)
    genre_dict = {}
    # create data for genre table.
    for index, item in enumerate(genre_set):
        output.append({"fields": {"name": item}, "model": "imdb-api.genre", "pk": index + 1})
        genre_dict[item] = index + 1

    for index, item in enumerate(data):
        # create data for genre mapping table.
        genres = item['genre']
        movie_id = movie_dict[item["name"]]
        for genre in genres:
            genre_id = genre_dict[genre.strip()]

            output.append({"fields": {"genre_id": genre_id, "movie_id": movie_id},
                       "model": "imdb-api.genremapping", "pk": index + 1})

    # write the data into the initial data file
    with open(os.path.join('fixtures', 'initial_data.json'), 'w') as _json_file:
        _json_file.write(json.dumps(output, indent=4))


def main():
    # to run the script from the imdb-api directory run python src/prepare_initial_data.py
    filename = os.path.join('data', 'imdb.json')
    prepare_initial_data(filename)

if __name__ == '__main__':
    main()
