

def ft_analytics_dashboard() -> None:
    """
    Display a game analytics dashboard demonstrating list, dict,
    and set comprehensions along with combined statistics.
    """

    print("=== Game Analytics Dashboard ===")
    print("")

    # ---------- List Comprehension Examples ----------
    players_list: list[list[object]] = [
        ["alice", 2300],
        ["david", 1800],
        ["diana", 2150],
        ["charlie", 2050],
    ]

    print("=== List Comprehension Examples ===")

    high_scores: list[str] = [
        name for name, score in players_list if score > 2000
    ]

    scores_doubled: list[int] = [
        score * 2 for name, score in players_list
    ]

    active_source: set[str] = {"alice", "bob", "charlie"}
    active_players: list[str] = [
        name for name, score in players_list if name in active_source
    ]

    print(f"High scorers (>2000): {high_scores}")
    print(f"Scores doubled: {scores_doubled}")
    print(f"Active players: {active_players}")

    # ---------- Dict Comprehension Examples ----------
    print("")
    print("=== Dict Comprehension Examples ===")

    players_dict: dict[str, int] = {
        "alice": 2300,
        "bob": 1800,
        "charlie": 2150,
    }

    players_achievements: dict[str, list[str]] = {
        "alice": [
            "first_kill", "level_10", "boss_slayer", "explorer", "collector"
            ],
        "bob": ["first_kill", "explorer", "trader"],
        "charlie": [
            "boss_slayer", "level_10", "first_kill",
            "speedrunner", "collector", "explorer", "veteran"],
    }

    players_scores: dict[str, int] = {
        key: players_dict[key] for key in players_dict
    }

    score_categories: dict[str, int] = {
        "high": sum(1 for k in players_dict if players_dict[k] > 2000),
        "medium": sum(
            1 for k in players_dict if 1500 <= players_dict[k] <= 2000
            ),
        "low": sum(1 for k in players_dict if players_dict[k] < 1500),
    }

    achievement_counts: dict[str, int] = {
        player: len(players_achievements[player])
        for player in players_achievements
    }

    print(f"Player scores: {players_scores}")
    print(f"Score categories: {score_categories}")
    print(f"Achievement counts: {achievement_counts}")

    # ---------- Set Comprehension Examples ----------
    print("")
    print("=== Set Comprehension Examples ===")

    players_with_duplicates: list[str] = [
        "alice", "bob", "alice", "charlie", "diana"
    ]

    unique_players: set[str] = {
        player for player in players_with_duplicates
    }

    unique_achievements: set[str] = {
        ach
        for player in players_achievements
        for ach in players_achievements[player]
    }

    player_regions: dict[str, str] = {
        "alice": "north",
        "bob": "east",
        "charlie": "central",
        "diana": "north",
    }

    active_regions: set[str] = {
        player_regions[player] for player in player_regions
    }

    print(f"Unique players: {unique_players}")
    print(f"Unique achievements: {unique_achievements}")
    print(f"Active regions: {active_regions}")
    print("")

    # ---------- Combined Analysis ----------
    print("=== Combined Analysis ===")

    total_players: int = len(unique_players)
    total_unique_achievements: int = len(unique_achievements)

    average_score: float = (
        sum(players_dict[k] for k in players_dict) / len(players_dict)
    )

    top_player: str = max(players_dict, key=lambda k: players_dict[k])
    top_score: int = players_dict[top_player]
    top_achievements: int = achievement_counts[top_player]

    print(f"Total players: {total_players}")
    print(f"Total unique achievements: {total_unique_achievements}")
    print(f"Average score: {average_score:.1f}")
    print(
        f"Top performer: {top_player} "
        f"({top_score} points, {top_achievements} achievements)"
    )


if __name__ == "__main__":
    ft_analytics_dashboard()
