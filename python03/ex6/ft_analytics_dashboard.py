
def ft_analytics_dashboard():
    print("=== Game Analytics Dashboard ===")
    print("")
    players_list = [
        ['alice', 2300],
        ['david', 1800],
        ['diana', 2150],
        ['charlie', 2050],
    ]
    print("=== List Comprehension Examples ===")

    high_scores: list[str] = [name for name, score in players_list if score > 2000]
    scores_doubled: list[int] = [score * 2 for name, score in players_list]
   
    active_source = {"alice", "bob", "charlie"}
    active_players: list[str] = [name for name, score in players_list if name in active_source]
   
    print(f"High scorers (>2000): {high_scores}")
    print(f"Scores doubled: {scores_doubled}")
    print(f"Active players: {active_players}")

    print("")
    print("=== Dict Comprehension Examples ===")
    players_dict = {
        "alice": 2300,
        "bob": 1800,
        "charlie": 2150
    }
    score_categories = {
        "high": 0,
        "medium": 0,
        "low": 0
    }
    players_scores = {key: players_dict[key] for key in players_dict}
    score_categories = {
        "high": sum(1 for k in players_dict if players_dict[k] > 2000),
        "medium": sum(1 for k in players_dict if 1500 <= players_dict[k] <= 2000),
        "low": sum(1 for k in players_dict if players_dict[k] < 1500),
    }

        
    print(f"Player scores: {players_scores}")
    print(f"Score categories: {score_categories}")
ft_analytics_dashboard()