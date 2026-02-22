

def ft_achievement_tracker():
    """
    Track and analyze player achievements using Python sets.

    The function defines achievement sets for multiple players and
    performs set operations to compute analytics such as:

    - all unique achievements across players
    - achievements common to all players
    - rare achievements owned by exactly one player
    - pairwise comparisons between players

    Results are displayed using the allowed set operations.
    """
    print("=== Achievement Tracker System ===", end="\n\n")

    alice_achiv: set[str] = {
        'first_kill', 'level_10', 'treasure_hunter', 'speed_demon'
        }
    bob_achiv: set[str] = {
        'first_kill', 'level_10', 'boss_slayer', 'collector'
        }
    charlie_achiv: set[str] = {
        'level_10', 'treasure_hunter',
        'boss_slayer', 'speed_demon', 'perfectionist'
        }

    print(f"Player alice achievements: {alice_achiv}")
    print(f"Player bob achievements: {bob_achiv}")
    print(f"Player charlie achievements: {charlie_achiv}")

    print("")
    print("=== Achievement Analytics ===")
    unique_achiv: set[str] = alice_achiv.union(bob_achiv).union(charlie_achiv)
    print(f"All unique achievements: {unique_achiv}")
    print(f"Total unique achievements: {len(unique_achiv)}")
    print("")

    common_achiv: set[str] = alice_achiv.intersection(
        bob_achiv).intersection(charlie_achiv)
    print(f"Common to all players: {common_achiv}")

    rare_achiv_alice: set[str] = alice_achiv.difference(
        bob_achiv.union(charlie_achiv))

    rare_achiv_bob: set[str] = bob_achiv.difference(
        alice_achiv.union(charlie_achiv))

    rare_achiv_charlie: set[str] = charlie_achiv.difference(
        bob_achiv.union(alice_achiv))

    rare_achiv: set[str] = rare_achiv_alice.union(
        rare_achiv_bob).union(rare_achiv_charlie)
    print(f"Rare achievements (1 player): {rare_achiv}")
    print("")

    common_ab: set[str] = alice_achiv.intersection(bob_achiv)
    print(f"Alice vs Bob common: {common_ab}")

    unique_alice: set[str] = alice_achiv.difference(bob_achiv)
    print(f"Alice unique: {unique_alice}")

    unique_bob: set[str] = bob_achiv.difference(alice_achiv)
    print(f"Bob unique: {unique_bob}")


if __name__ == "__main__":
    ft_achievement_tracker()
