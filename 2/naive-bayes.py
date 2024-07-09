from nlpia.data import get_data

movies = get_data('hutto_movies')

print(movies.head().round(2))