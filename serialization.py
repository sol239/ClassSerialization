import json
from typing import Type, TypeVar, Optional

T = TypeVar('T')

def serialize(class_instance, save_file: bool = False, file_path: Optional[str] = None) -> str:
    json_string = json.dumps(class_instance.__dict__)
    if (save_file):
        file = open(file_path, "w", encoding="utf-8")
        file.write(json_string)
        file.close
    return json_string

def deserialize(class_type: Type[T], file_path: str) -> T:
    with open(file_path, "r", encoding="utf-8") as file:
        json_data = json.load(file)
    return class_type(**json_data)
    