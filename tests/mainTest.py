import unittest
from dataclasses import dataclass
from sol239_serialization.serialization import serialize


@dataclass
class Painting:
    name:str
    price:float
    year_painted:int

class TestSerializationClass(unittest.TestCase):

    def test_serialization(self):
        painting = Painting(name="Picture 1", price=29011.11, year_painted=1999)

        expected = """{"name": "Picture 1", "price": 29011.11, "year_painted": 1999}"""
        actual = serialize(painting)
        self.assertEqual(expected, actual, "Serialization failed")

    