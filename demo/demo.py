# demo use
from dataclass_example import Book as DataclassBook
from class_example import Book as ClassBook
from serialization import serialize, deserialize

# Create instances of the two classes
dataclass_book = DataclassBook("The Great Gatsby", ["F. Scott Fitzgerald"], 180, 10.99)
class_book = ClassBook("The Great Gatsby", ["F. Scott Fitzgerald"], 180, 10.99)

# Serialize the instances without saving them to files
dataclass_json_string = serialize(dataclass_book)
class_json_string = serialize(class_book)

# Serialize the instances and save them to files
dataclass_json = serialize(dataclass_book, save_file=True, file_path="dataclass_book.json")
class_json = serialize(class_book, save_file=True, file_path="class_book.json")

# Deserialize the instances from the JSON strings
dataclass_book = deserialize(DataclassBook, "dataclass_book.json")
class_book = deserialize(ClassBook, "class_book.json")

# Print the instances
print(dataclass_book.__dict__)
print(class_book.__dict__)
