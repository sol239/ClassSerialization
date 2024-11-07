from dataclasses import dataclass

@dataclass
class Book:
    """
    Simple dataclass example.
    """
    title: str
    authors: list
    page_count:int
    price:float
    
    