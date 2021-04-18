from typing import List


class Markets:
    def __init__(self, name: str, area: int, categories: List[str]):
        self.name = name
        self.area = area
        self.categories = categories

    def __str__(self):
        return f"Supermarket {self.name} has an area of {self.area} m2 and has the following categories: {', '.join(self.categories)}."
