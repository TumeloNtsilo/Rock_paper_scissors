import unittest
from rock_paper_scissors import Winner  

class TestWinner(unittest.TestCase):

    def setUp(self):
        self.winner = Winner()
    
    """This tests is for when a player 
    wins over a computer."""

    def test_player_wins(self):
        winning_cases = [
            ("rock", "scissors"),
            ("paper", "rock"),
            ("scissors", "paper"),
        ]
        for player, computer in winning_cases:
            self.winner.score_count((player, computer))
        self.assertEqual(self.winner.player_score, 3)
        self.assertEqual(self.winner.comp_score, 0)

    """This tests when a player losses 
    over a computer"""
    def test_computer_wins(self):
        losing_cases = [
            ("scissors", "rock"),
            ("rock", "paper"),
            ("paper", "scissors"),
        ]
        for player, computer in losing_cases:
            self.winner.score_count((player, computer))
        self.assertEqual(self.winner.comp_score, 3)
        self.assertEqual(self.winner.player_score, 0)

    """This tests a tie in the game."""
    def test_ties(self):
        tie_cases = [
            ("rock", "rock"),
            ("paper", "paper"),
            ("scissors", "scissors"),
        ]
        for player, computer in tie_cases:
            self.winner.score_count((player, computer))
        self.assertEqual(self.winner.comp_score, 0)
        self.assertEqual(self.winner.player_score, 0)


if __name__ == "__main__":
    unittest.main()
