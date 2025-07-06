from typing import Iterable
from functools import total_ordering
'''
Написати додаток, який допомагає керувати піснями

Song (author, title, duration)

Playlist (Collection of Songs) 

Playlist(Userlist)

__str__, __repr__, __eq__, __hash__, __lt__
'''


@total_ordering
class Song:
    def __init__(self, author: str, title: str, genres: list[str], duration_in_seconds: int = 0):
        self.author = author
        self.title = title
        self.genres = genres
        self.duration_in_seconds = duration_in_seconds

    def __eq__(self, other):
        return self.author == other.author and self.title == other.title
    
    def __lt__(self, other):
        return self.duration_in_seconds < other.duration

    # def __str__(self) -> str:
    #     return f'Song(author={self.author}, title={self.title}, duration_in_seconds={self.duration_in_seconds})'

    # def __repr__(self):
    #     # return f'Song(author={self.author}, title={self.title})'
    #     return f'"{self.title}" by {self.author}'


class Playlist:
    ''' Contains a list of songs and playlist name '''
    def __init__(self, playlist_name: str):
        self.playlist_name = playlist_name
        # self.songs = magic_list()
        self.songs = []

    def __isub__(self, data):
        if isinstance(data, Song):
            self.songs.remove(data)
        return self

    def __sub__(self, data):
        return self.__isub__(data)

    def __iadd__(self, song: Song):
        return self.__add__(song)

    def __add__(self, data):
        self.add_song(data)
        return self
    
    # def __getitem__(self, key: int):
    #     # if key > len(self.songs):
    #     #     raise IndexError # This is not needed because we use list
    #     return self.songs[key]

    def __iter__(self):
        '''Початок перебирання елементів (виклик iter). Має повертати щось що має метод __next___'''
        self.current_song_index = 0
        return self

    def __next__(self):
        '''Повернення наступного елемента (виклик next)'''
        if self.current_song_index >= len(self.songs): # 0 1 2
            raise StopIteration
        next_song = self.songs[self.current_song_index]
        self.current_song_index += 1
        return next_song
    
    def __setitem__(self, key, value):
        if not isinstance(value, Song):
            raise ValueError
        self.songs[key] = value

    def add_song(self, data):
        if isinstance(data, Song):
            self.songs.append(data)
        elif isinstance(data, Iterable):
            self.songs += data
        # elif isinstance(data, set):
        #     ...
            # raise ValueError("Can only add songs to playlist")
        

    def __str__(self) -> str:
        return f'Playlist({self.songs})'

if __name__ == '__main__':
    song_one = Song('Author One', 'Song Two', [], 100)
    song_two = Song('Author One', 'Song Two', [], 100)
    # print(song_one)
    # print(song_two)
    # print(song_one == song_two)
    # print('0x102b127b0>' == '0x102abf890')
    playlist = Playlist("Playlist One")
    # songs_list = []
    # song_one = Song('Author One', 'Song One', [], 100)
    # song_two = Song('Author Two', 'Song Two', [], 250)
    # songs_list.append(song_one)
    # songs_list.append(song_two)

    # playlist + songs_list
    # playlist + songs_list
    # playlist + songs_list


    playlist + song_one
    playlist + song_two

    for song in playlist:
        print(song)

    # playlist[0] = Song("Author One", "Song Three", [], 200)
    # print(playlist)

    # playlist - song_one
    # print(playlist)

    # songs_list.append(song_one)
    # songs_list.append(song_two)
    # print(str(songs_list))
    # str()

    # print(f"My favorite song is: {song_two!r}")

    # playlist = Playlist("Playlist One") # "Playlist One", ["Song One" by Author One]
    # playlist_two = Playlist("Playlist Two") # "Playlist Two", []
    # song_one = Song('Author One', 'Song One', 100)

    # # playlist.add_song(song_one)

    # # playlist.songs += [song_one]
    # playlist += song_one
    # # print(playlist + song_one + song_two)
    # # playlist + song_one
    # # playlist + song_one

    # print(playlist.songs)

    # print(playlist_two.songs)
