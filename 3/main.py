'''
Написати додаток, який допомагає керувати піснями

Song (author, title, duration)

Playlist (Collection of Songs) 

Playlist(Userlist)
'''


class Song:
    def __init__(self, author: str, title: str, duration_in_seconds: int = 0):
        self.author = author
        self.title = title
        self.duration_in_seconds = duration_in_seconds

    def __str__(self) -> str:
        return f'Song(author={self.author}, title={self.title}, duration_in_seconds={self.duration_in_seconds})'

    def __repr__(self):
        # return f'Song(author={self.author}, title={self.title})'
        return f'"{self.title}" by {self.author}'


if __name__ == '__main__':
    songs_list = []
    song_one = Song('Author One', 'Song One', 100)
    song_two = Song('Author Two', 'Song Two', 250)

    songs_list.append(song_one)
    songs_list.append(song_two)
    # print(str(songs_list))

    print(f"My favorite song is: {song_two!r}")
