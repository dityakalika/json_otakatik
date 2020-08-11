# PROJECT : MOVIE REVIEW (JSON TO CSV)

# MODULE
import json
import requests
import pandas as pd

# SOURCE : GITHUB

# PREPARE THE DATA
url = 'https://raw.githubusercontent.com/FEND16/movie-json-data/master/json/movies-coming-soon.json'
response = requests.get(url)
#print(response.status_code)
#print(response.text)

# LOAD THE DATA JSON INTO PYTHON
data_json = json.loads(response.text)
# print(data_json)

# PREPARE THE TABLE
movie_list = []

# SCRAP THE DATA
for ambil in data_json:
    number = ambil['id']
    title = ambil['title']
    genre = ambil['genres']
    rating = ambil['imdbRating']
    release_date = ambil['releaseDate']
    actors = ambil['actors']
    age = ambil['contentRating']
    duration= ambil['duration']
    # print(number,title,genre,rating,release_date,actors,age,duration)
    table ={
        'No': number,
        'Title' : title,
        'Genre' : genre,
        'Rating' : rating,
        'Release Date' : release_date,
        'Actors' : actors,
        'PG' : age,
        'Duration' : duration,
    }
    movie_list.append(table)

print(movie_list)

# EXPORT TO CSV

df = pd.DataFrame(movie_list)
df.to_csv("./ MovieList.csv", index = False)
