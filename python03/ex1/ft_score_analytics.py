import sys


def ft_score_analytics():
    """
    Process and analyze player scores from command-line arguments.

    Converts inputs to integers, stores them in a list, and prints
    basic statistics while handling invalid input gracefully.
    """
    try:
        print("=== Player Score Analytics ===")
        argc: int = len(sys.argv)
        if argc < 2:
            raise ValueError(
                "No scores provided. Usage: python3 "
                "ft_score_analytics.py <score1> <score2> ..."
                )
        scores: list[int] = []
        for arg in sys.argv[1:]:
            score: int = int(arg)
            scores.append(score)
        print(f"Scores processed: {scores}")
        len_scores: int = len(scores)
        print(f"Total players: {len_scores}")
        sum_scores: int = sum(scores)
        print(f"Total score: {sum_scores}")
        average_scores: float = sum_scores / len_scores
        print(f"Average score: {average_scores}")
        max_score: int = max(scores)
        print(f"High score: {max_score}")
        min_score: int = min(scores)
        print(f"Low score: {min_score}")
        score_range: int = max_score - min_score
        print(f"Score range: {score_range}")
    except ValueError as e:
        print(e)


if __name__ == "__main__":
    ft_score_analytics()
