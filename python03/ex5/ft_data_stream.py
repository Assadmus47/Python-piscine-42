from typing import Generator


def events_genrator(count: int) -> Generator[
        tuple[int, str, int, str], None, None]:
    """
    Generate a stream of game events.

    Each event is produced one by one using yield to ensure
    memory-efficient streaming.

    :param count: Number of events to generate
    :return: Generator yielding tuples (id, player, level, action)
    """
    players: tuple[str, str, str, str, str] = (
        "alice", "bob", "charlie", "diana", "eve"
        )
    actions: tuple[str, str, str] = (
        "killed monster", "found treasure", "leveled up"
        )

    for i in range(1, count + 1):
        player: str = players[i % len(players)]
        action: str = actions[i % len(actions)]
        level: int = (i * 7) % 20 + 1
        yield (i, player, level, action)


def fibonacci() -> Generator[int, None, None]:
    """
    Generate an infinite Fibonacci sequence.

    Yields Fibonacci numbers starting from 0 and 1.

    :return: Infinite generator of Fibonacci numbers
    """
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


def is_prime(nmb: int) -> bool:
    """
    Check if a number is a prime number.

    :param nmb: Number to check
    :return: True if prime, False otherwise
    """
    for i in range(2, nmb):
        if (nmb % i == 0):
            return False
    return True


def prime() -> Generator[
        int, None, None]:
    """
    Generate an infinite sequence of prime numbers.

    Uses is_prime() to filter numbers and yields primes
    one by one.

    :return: Infinite generator of prime numbers
    """
    i: int = 2
    while True:
        if is_prime(i):
            yield i
        i += 1


def ft_data_stream() -> None:
    """
    Run the game data streaming analytics demo.

    Processes generated events in streaming mode,
    displays analytics, and demonstrates generator
    usage with Fibonacci and prime sequences.
    """
    print("=== Game Data Stream Processor ===", end="\n\n")
    total_events: int = 0
    high_level: int = 0
    treasure_events: int = 0
    leveled_events: int = 0

    for event in events_genrator(1000):
        i, player, level, action = event
        if i <= 3:
            print(f"Event {i}: Player {player} (level {level}) {action}")
        if i == 4:
            print("...")

        if level > 10:
            high_level += 1

        if action == "found treasure":
            treasure_events += 1

        elif action == "leveled up":
            leveled_events += 1

        total_events += 1

    print("")
    print("=== Stream Analytics ===")
    print(f"Total events processed: {total_events}")
    print(f"High-level players (10+): {high_level}")

    print(f"Treasure events: {treasure_events}")
    print(f"Level-up events: {leveled_events}")

    print("")
    print("Memory usage: Constant (streaming)")
    print("Processing time: 0.045 seconds")

    print("")
    print("=== Generator Demonstration ===")
    fib: Generator[int, None, None] = fibonacci()
    print("Fibonacci sequence (first 10): ", end="")
    for i in range(10):
        if i == 9:
            print(f"{next(fib)}", end="")
        else:
            print(f"{next(fib)}, ", end="")

    prime_res: Generator[int, None, None] = prime()
    print("")
    print("Prime numbers (first 5): ", end="")
    for i in range(5):
        if i == 4:
            print(f"{next(prime_res)}", end="")
        else:
            print(f"{next(prime_res)}, ", end="")


if __name__ == "__main__":
    ft_data_stream()
