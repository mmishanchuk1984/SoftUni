class PhotoAlbum:
    def __init__(self, pages):
        self.pages = pages
        self.photos = [[] for i in range(self.pages)]
        self.counter = 0

    @classmethod
    def from_photos_count(cls, photos_count):
        if photos_count % 4 != 0:
            pages = 1 + (photos_count % 4)
        else:
            pages = photos_count % 4
        return cls(pages)

    def add_photo(self, label: str):
        for row in range(self.pages):
            self.photos.append(label)
            self.counter += 1
            if self.counter > 4:
                self.counter = 1
                row += 1
            if row > self.pages:
                return "No more free slots"
            return f"{label} photo added successfully on page {row + 1} slot {self.counter}"

    def display(self):
        to_print = "-----------"
        for el in self.photos:
            if el:
                print([])
        return to_print


album = PhotoAlbum(2)

print(album.add_photo("baby"))
print(album.add_photo("first grade"))
print(album.add_photo("eight grade"))
print(album.add_photo("party with friends"))
print(album.photos)
print(album.add_photo("prom"))
print(album.add_photo("wedding"))

print(album.display())
