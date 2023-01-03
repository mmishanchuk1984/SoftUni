from unittest import TestCase
from project.mammal import Mammal


class TestMammal(TestCase):
    def setUp(self) -> None:
        self.mammal = Mammal("Leo", "cat", "Meow")

    def test_init(self):
        mammal = Mammal("Leo", "cat", "Meow")
        self.assertEqual("Leo", mammal.name)
        self.assertEqual("cat", mammal.type)
        self.assertEqual("Meow", mammal.sound)

    def test_make_sound(self):
        result = f"Leo makes Meow"
        self.mammal.make_sound()
        self.assertEqual(result, self.mammal.make_sound())

    def test_get_kingdom(self):
        self.assertEqual("animals", self.mammal.get_kingdom())

    def test_info(self):
        result = "Leo is of type cat"
        self.assertEqual(result, self.mammal.info())









