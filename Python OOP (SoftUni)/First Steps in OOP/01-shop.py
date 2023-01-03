class Shop:

    def __init__(self, name, items):
        self.name = name
        self.items =items

    def get_items_count(self):
        total_items = len(self.items)
        return total_items


shop = Shop("My Shop", ["Apples", "Bananas", "Cucumbers"])
print(shop.get_items_count())
