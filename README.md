# ClassSerialization

Python library for class JSON serialization.

---

### Example usage

```python
from serialization import serialize, deserialize

class Book:
    """
    Simple class class example
    """
    def __init__(self, title:str, authors:list, page_count:int, price:float):
        self.title = title
        self.authors = authors
        self.page_count = page_count
        self.price = price

class_book = Book("The Great Gatsby", ["F. Scott Fitzgerald"], 180, 10.99)

# SERIALIZE
serialized_json_string = serialize(class_book, save_file=True, file_path="fl.json")
print(serialized_json_string)

# DESERIALIZE
book = deserialize(Book, "fl.json")
print(book.__dict__)
print(book.title)
```

---