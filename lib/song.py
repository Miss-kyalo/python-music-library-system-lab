class Song:
    all = []
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}
    artists_count = artist_count

    def __init__(self, name, artist, genre=""):
        self.name = name
        self.artist = artist
        self.genre = genre

        Song.all.append(self)
        Song.add_song_to_count()
        Song.add_to_genres(genre)
        Song.add_to_artists(artist)
        Song.add_to_genre_count(genre)
        Song.add_to_artists_count(artist)

    @classmethod
    def add_song_to_count(cls):
        cls.count += 1

    @classmethod
    def add_to_genres(cls, genre):
        if genre and genre not in cls.genres:
            cls.genres.append(genre)

    @classmethod
    def add_to_artists(cls, artist):
        if artist and artist not in cls.artists:
            cls.artists.append(artist)

    @classmethod
    def add_to_genre_count(cls, genre):
        if genre:
            cls.genre_count[genre] = cls.genre_count.get(genre, 0) + 1

    @classmethod
    def add_to_artists_count(cls, artist):
        if artist:
            cls.artist_count[artist] = cls.artist_count.get(artist, 0) + 1
            cls.artists_count = cls.artist_count

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and len(value) > 0:
            self._name = value
        else:
            raise ValueError("Name must be a non-empty string.")

    @property
    def artist(self):
        return self._artist

    @artist.setter
    def artist(self, value):
        if isinstance(value, str) and len(value) > 0:
            self._artist = value
        else:
            raise ValueError("Artist must be a non-empty string.")

    @property
    def genre(self):
        return self._genre

    @genre.setter
    def genre(self, value):
        if isinstance(value, str):
            self._genre = value
        else:
            raise ValueError("Genre must be a string.")

    @classmethod
    def clear(cls):
        cls.all.clear()
        cls.count = 0
        cls.genres.clear()
        cls.artists.clear()
        cls.genre_count.clear()
        cls.artist_count.clear()
        cls.artists_count = cls.artist_count

    @classmethod
    def create(cls, name, artist, genre=""):
        return cls(name, artist, genre)