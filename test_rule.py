import unittest

import rule


class MyTestCase(unittest.TestCase):
#all posible situation
    def test_valid_game_once(self):
        self.assertEqual(rule.game_once(player='rock', computer='scissors'), 'player')
        self.assertEqual(rule.game_once(player='paper',computer='scissors'),'computer')
        self.assertEqual(rule.game_once(player='scissors',computer='scissors'),'tie')

        self.assertEqual(rule.game_once(player='rock', computer='rock'), 'tie')
        self.assertEqual(rule.game_once(player='paper',computer='rock'),'player')
        self.assertEqual(rule.game_once(player='scissors',computer='rock'),'computer')

        self.assertEqual(rule.game_once(player='rock', computer='paper'), 'computer')
        self.assertEqual(rule.game_once(player='paper',computer='paper'),'tie')
        self.assertEqual(rule.game_once(player='scissors',computer='paper'),'player')
#wrong result test
        self.assertNotEqual(rule.game_once(player='rock', computer='paper'), 'player' or 'tie')
#end rule test
    def test_valid_is_end(self):
        self.assertEqual(rule.is_end(5, 4), (True, "player"))
        self.assertEqual(rule.is_end(4, 5), (True, "computer"))
        self.assertEqual(rule.is_end(4, 4), (False, None))

if __name__ == "__main__":
    unittest.main()