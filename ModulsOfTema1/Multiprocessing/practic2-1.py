from pprint import pprint

import requests
from threading import Thread

# www.example.com/search?q=some_query&type=music&genre=classic

ACCESS_TOKEN = 'CXyFeSBw2lAdG41xkuU3LS6a_nwyxwwCz2dCkUohw-rw0C49x2HqP__6_4is5RPx'
RANDOM_GENERE_API_URL = 'https://binaryjazz.us/wp-json/generator/v1/genre/'
GENIUS_API_URL = 'https://api.genius.com/search'
GENIUS_URL = 'https://genius.com'

genre = requests.get(RANDOM_GENERE_API_URL).json()

data = requests.get(GENIUS_API_URL, params={'access_token': ACCESS_TOKEN, 'q': genre})
data = data.json()
song_id = data['response']['hits'][0]['result']['api_path']
print(f'{GENIUS_URL}{song_id}/music_player')