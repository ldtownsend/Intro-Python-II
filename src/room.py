# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, title, description, items):
        self.title = title
        self.description = description
        self.items = items
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None

    def __str__(self):
        return f"{self.title}\n\n{self.description}\n\nItems in the Room: {[x.item_name for x in self.items]}"
        #List comprehension practice