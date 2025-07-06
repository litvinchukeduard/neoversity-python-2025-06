from dataclasses import dataclass


@dataclass
class Song:
    author: str
    title: str
    duration_in_seconds: int = 0

    def __repr__(self):
        # return f'Song(author={self.author}, title={self.title})'
        return f'"{self.title}" by {self.author}'


if __name__ == '__main__':
    songs_list = []
    song_one = Song('Author One', 'Song One', 100)
    song_two = Song('Author Two', 'Song Two', 250)

    songs_list.append(song_one)
    songs_list.append(song_two)
    print(str(songs_list))

    print(f"My favorite song is: {song_two!r}")
