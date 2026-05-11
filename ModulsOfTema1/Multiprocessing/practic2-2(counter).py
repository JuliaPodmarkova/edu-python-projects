from datetime import datetime
from pprint import pprint

import requests
from threading import Thread, Event
import queue

# www.example.com/search?q=some_query&type=music&genre=classic

ACCESS_TOKEN = '221D0eyK7BV5RwDXXCQglRlwVMULwYyNbOtDhN4TuoMAQWmhvfxfkiu4RgUA34BK'
RANDOM_GENERE_API_URL = 'https://binaryjazz.us/wp-json/generator/v1/genre/'
GENIUS_API_URL = 'https://api.genius.com/search'
GENIUS_URL = 'https://genius.com'

class GetGenre(Thread):

    def __init__(self, queue, stop_event):
        self.queue = queue
        self.stop_event = stop_event
        super().__init__()

    def run(self):
        while not self.stop_event.is_set():
            genre = requests.get(RANDOM_GENERE_API_URL).json()
            self.queue.put(genre)

class Genius(Thread):

    all_songs = []

    def __init__(self, queue, counter, stop_event):
        self.queue = queue
        self.counter = counter
        self.stop_event = stop_event
        super().__init__()

    def run(self):
        while not self.stop_event.is_set():
            genre = self.queue.get()
            #print(self.queue.qsize())
            data = requests.get(GENIUS_API_URL, params={'access_token': ACCESS_TOKEN, 'g': genre})
            data = data.json()
            try:
                song_id = data['response']['hits'][0]['result']['api_path']
                self.all_songs.append({'genre': genre, 'song': f'{GENIUS_URL}{song_id}/apple_music_player'})
                if self.list_is_filled():
                    self.stop_event.set()
            except IndexError as ie:
                self.run()

    def list_is_filled(self):
        return (self.all_songs) >= self.counter


queue = queue.Queue()
counter = 10
stop_event = Event()

genre_list = []
genius_list = []

start = datetime.now()

for _ in range(10):
    t = GetGenre(queue, stop_event)
    t.start()
    genre_list.append(t)

for _ in range(10):
    t = Genius(queue, stop_event, counter)
    t.start()
    genius_list.append(t)

for t in genius_list:
    t.join()

for t in genre_list:
    t.join()

stop_event.set()

print(queue.qsize())
pprint(Genius.all_songs)
print(len(Genius.all_songs))
end = datetime.now()
print(end - start)