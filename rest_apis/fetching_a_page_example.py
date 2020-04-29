import requests
import json

#page = requests.get("https://api.datamuse.com/words?rel_rhy=morning")
kval_pairs = {'rel_rhy': 'funny'}
page = requests.get("https://api.datamuse.com/words", params = kval_pairs)
print(type(page))
print(page.text[:150])
print(page.url)
print(page.status_code)
print(page.headers)
print("-------")
x = page.json()
print(type(x))
print("---first item in the list---")
print(x[0:5])
#print("---the whole list, pretty printed---")
#print(json.dumps(x, indent=2))


#--------------------------------------------------------

import requests_with_caching
import json

def get_movies_from_tastedive(movie_title):
    base_url = 'https://tastedive.com/api/similar'
    kval_pairs = {'q': movie_title, 'type': 'movies', 'limit': 5}
    page = requests_with_caching.get(base_url, params = kval_pairs)
    x = page.json()
    return x

def extract_movie_titles(x):
    return [d['Name'] for d in x['Similar']['Results']]

def get_related_titles(title_list):
    related_titles = []
    for title in title_list:
        related = extract_movie_titles(get_movies_from_tastedive(title))
        related_titles.extend(related)
    return list(set(related_titles))

extract_movie_titles(get_movies_from_tastedive("Sherlock Holmes"))

get_related_titles("Sherlock Holmes")


import requests_with_caching
import json

def get_movie_data(movie_title):
    base_url = 'http://www.omdbapi.com/'
    kval_pairs = {'t': movie_title, 'r': 'json'}
    page = requests_with_caching.get(base_url, params = kval_pairs)
    x = page.json()
    return x

def get_movie_rating(x):
    ratings = x['Ratings']
    rating = 0
    for r in ratings:
        if r['Source']=='Rotten Tomatoes':
            rating = int(r['Value'].replace('%',''))
    return rating

def get_sorted_recommendations(list_titles):
    related = get_related_titles(list_titles)
    related_ratings = [(title, get_movie_rating(get_movie_data(title))) for title in related]
    related_ratings_s = sorted(related_ratings, key=lambda x:(x[1],x[0]), reverse=True)
    return [pair[0] for pair in related_ratings_s]
    