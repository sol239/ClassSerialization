import unittest
from dataclasses import dataclass
from serialization import serialize, deserialize

@dataclass
class Painting:
    name:str
    price:float
    year_painted:int
    
class TestSerializationClass(unittest.TestCase):
    def test_serialization(self):
        
        painting = Painting(name="Picture 1", price=29011.11, year_painted=1999)
        
        # data
        expected = """{"name":"Picture 1", "price":29011.11, "year_painted":1999}"""
        actual = serialize(painting)
        self.assertEqual(expected. actual)