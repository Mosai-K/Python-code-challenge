import unittest
from team_league_calculator import calculate_rank, sort_team_ranks, format_ranking_results

class TestLeagueRank(unittest.TestCase):
    
    def test_empty_input(self):
        input = ""
        expected = ""
        self.assertEqual(format_ranking_results(sort_team_ranks(calculate_rank(input))), expected)

    def test_basic_league_ranking(self):
        input = [
        "Lions 2, Chiefs 2",
        "Pirates 3, Lions 0",
        "Pirates 1, Chiefs 1",
        "Celtics 1, Lions 0"
        ]
        
        expected = {'Lions': 1, 'Chiefs': 2, 'Pirates': 4, 'Celtics': 3}
        self.assertEqual(calculate_rank(input), expected)
        
    def test_sorted_ranks(self):
        input = [
        "Lions 2, Chiefs 2",
        "Pirates 3, Lions 0",
        "Pirates 1, Chiefs 1",
        "Celtics 1, Lions 0"
        ]
        
        expected = [('Pirates', 4), ('Celtics', 3), ('Chiefs', 2), ('Lions', 1)]
        self.assertEqual(sort_team_ranks(calculate_rank(input)), expected)
    
    def test_multiple_teams_with_same_score(self):
        input = [
        "Lions 2, Chiefs 2",
        "Pirates 3, Lions 2",
        "Pirates 1, Chiefs 0",
        ]
        
        expected = [('Pirates', 6), ('Chiefs', 1), ('Lions', 1)]
        self.assertEqual(sort_team_ranks(calculate_rank(input)), expected)
    
    def test_multiple_teams_score_formatting(self):
        input = [
        "Lions 2, Chiefs 2",
        "Pirates 3, Lions 2",
        "Pirates 1, Chiefs 0",
        "Celtics 1, Pirates 2"
        ]
        expected = "1. Pirates: 9 pts\n2. Chiefs: 1 pt\n2. Lions: 1 pt\n4. Celtics: 0 pts"
        self.assertEqual(format_ranking_results(sort_team_ranks(calculate_rank(input))), expected)
        
if __name__ == "__main__":
    unittest.main()