import dataclasses
import json

def serialize_class(class_instance:object, save_file:bool = False, file_path:str = None) -> str:
    json_string = json.dumps(object)
    if (save_file):
        file = open(file_path, "w", encoding="utf-8")
        file.write(json_string)
        file.close
    return json_string

def serialize_dataclass(dataclass_instance:object, save_file:bool = False, file_path:str = None):
    json_string = json.dumps(object)
    if (save_file):
        file = open(file_path, "w", encoding="utf-8")
        file.write(json_string)
        file.close
    return json_string

def deserialize_dataclass(file_path:str) -> object:
    file = open(file_path, "r", encoding="utf-8")
    json_string = file.read()
    file.close()
    return json.loads(json_string)


def deserialize_class(file_path:str) -> object:
    file = open(file_path, "r", encoding="utf-8")
    json_string = file.read()
    file.close()
    return json.loads(json_string)