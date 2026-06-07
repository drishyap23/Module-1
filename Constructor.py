class Playlist:
    def __init__(self, name, genre):
        self.name = name
        self.genre = genre
        self.songs = []
        print(f"Playlist '{self.name}' ({self.genre}) is ready!")

    def __del__(self):
        print(f"Playlist '{self.name}' has been deleted. Goodbye!")

rock_mix = Playlist("Road Trip Mix", "Pop")
house_mix = Playlist("Party Mix", "Pop")
del rock_mix