from dataclasses import dataclass


@dataclass(frozen=True, init=True)
class Song:
    author: str
    title: str
    genres: list[str]
    duration_in_seconds: int = 0

    def __str__(self) -> str:
        return f'Song(author={self.author}, title={self.title}, duration_in_seconds={self.duration_in_seconds})'

    def __repr__(self):
        # return f'Song(author={self.author}, title={self.title})'
        return f'"{self.title}" by {self.author}'


if __name__ == '__main__':
    song_one = Song('Author One', 'Song One', 100)
    # songs_list = []
    # song_one = Song('Author One', 'Song One', 100)
    # song_one.duration_in_seconds = 300
    # song_two = Song('Author Two', 'Song Two', 250)

    # # song_one.genres.append("Hello")

    # print(song_one)

    # songs_list.append(song_one)
    # songs_list.append(song_two)
    # print(str(songs_list))

    # print(f"My favorite song is: {song_two!r}")
