'''
Написати додаток, який допомагає керувати піснями

Song (author, title, duration)

Playlist (Collection of Songs) 

Playlist(Userlist)
'''


class Song:
    def __init__(self, author: str, title: str, genres: list[str], duration_in_seconds: int = 0):
        self.author = author
        self.title = title
        self.genres = genres
        self.duration_in_seconds = duration_in_seconds

    def __str__(self) -> str:
        return f'Song(author={self.author}, title={self.title}, duration_in_seconds={self.duration_in_seconds})'

    def __repr__(self):
        # return f'Song(author={self.author}, title={self.title})'
        return f'"{self.title}" by {self.author}'


class Playlist:
    ''' Contains a list of songs and playlist name '''
    def __init__(self, playlist_name: str):
        self.playlist_name = playlist_name
        # self.songs = magic_list()
        self.songs = []

    def __add__(self, song: Song):
        self.add_song(song)
        return self

    def add_song(self, song: Song):
        if not isinstance(song, Song):
            raise ValueError("Can only add songs to playlist")
        self.songs.append(song)

    def __str__(self) -> str:
        return f'Playlist({self.songs})'

if __name__ == '__main__':
    # songs_list = []
    # song_one = Song('Author One', 'Song One', 100)
    # song_two = Song('Author Two', 'Song Two', 250)

    # songs_list.append(song_one)
    # songs_list.append(song_two)
    # print(str(songs_list))
    # str()

    # print(f"My favorite song is: {song_two!r}")

    playlist = Playlist("Playlist One") # "Playlist One", ["Song One" by Author One]
    playlist_two = Playlist("Playlist Two") # "Playlist Two", []
    song_one = Song('Author One', 'Song One', 100)

    # playlist.add_song(song_one)

    # playlist.songs += [song_one]
    # playlist += song_one
    print(playlist + song_one)
    playlist + song_one
    playlist + song_one

    print(playlist.songs)

    print(playlist_two.songs)
