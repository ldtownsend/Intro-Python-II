class Item:
    def __init__(self, item_name, description):
        self.item_name = item_name
        self.description = description
    
    def __str__(self):
        return f"Item: {self.item_name}\n\nDescription: {self.description}"
