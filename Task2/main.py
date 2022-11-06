import random
import unittest
from Task1.main import get_score, generate_game


class TestGame(unittest.TestCase):
    def setUp(self):
        self.game_stamps = generate_game()

        self.last_offset = self.game_stamps[-1]['offset']

    def test_negative_offset(self):
        self.assertEqual(get_score(self.game_stamps, -1), (-1, -1))

    def test_offset_out_of_bounds(self):
        self.assertEqual(get_score(self.game_stamps, self.last_offset + 1), (-1, -1))

    def test_check_random_offset(self):
        random_stamp = random.choice(self.game_stamps)
        random_offset = random_stamp['offset']
        self.assertEqual(get_score(self.game_stamps, random_offset),
                         (random_stamp['score']['home'], random_stamp['score']['away']))

    def test_check_last_offset(self):
        last_offset = self.game_stamps[-1]['offset']
        last_home = self.game_stamps[-1]['score']['home']
        last_away = self.game_stamps[-1]['score']['away']
        self.assertEqual(get_score(self.game_stamps, last_offset), (last_home, last_away))

    def test_check_first_offset(self):
        first_offset = self.game_stamps[0]['offset']
        first_home = self.game_stamps[0]['score']['home']
        first_away = self.game_stamps[0]['score']['away']
        self.assertEqual(get_score(self.game_stamps, first_offset), (first_home, first_away))


if __name__ == '__main__':
    unittest.main()
