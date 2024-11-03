
class Category:
    def __init__(self, id, name):
        self.id = id  # Unique identifier for the category
        self.name = name

    def __repr__(self):
        return f"Category(id={self.id}, name={self.name})"