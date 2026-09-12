class Song:
    all = []
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre=""):
        self.name = name
        self.artist = artist
        self.genre = genre

        # Register instance to class tracking
        Song.all.append(self)
        Song.count = len(Song.all)

        # Track unique genres and update counts
        if genre:
            if genre not in Song.genres:
                Song.genres.append(genre)
            Song.genre_count[genre] = Song.genre_count.get(genre, 0) + 1

        # Track unique artists and update counts
        if artist:
            if artist not in Song.artists:
                Song.artists.append(artist)
            Song.artist_count[artist] = Song.artist_count.get(artist, 0) + 1

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

    @classmethod
    def create(cls, name, artist, genre=""):
        return cls(name, artist, genre)