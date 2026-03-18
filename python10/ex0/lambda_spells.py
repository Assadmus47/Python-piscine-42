def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return sorted(
        artifacts, key=lambda element: element['power'], reverse=True
        )


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return list(filter(lambda mage: mage['power'] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda chaine: "* " + chaine + " *", spells))


def mage_stats(mages: list[dict]) -> dict:
    max_dict = max(mages, key=lambda mage: mage['power'])
    min_dict = min(mages, key=lambda mage: mage['power'])
    return {
        'max_power': max_dict['power'],
        'min_power': min_dict['power'],
        'avg_power':
            round(sum(mage['power'] for mage in mages) / len(mages), 2)
    }


def main() -> None:
    print()
    print("Testing artifact_sorter...")
    result = artifact_sorter([
        {"name": "Crystal Orb", "power": 85},
        {"name": "Fire Staff", "power": 92}
    ])
    print(
        f"Fire Staff ({result[0]['power']} power) "
        f"comes before Crystal Orb ({result[1]['power']} power)"
    )

    print()
    print("Testing spell transformer...")
    print(" ".join(spell_transformer(["fireball", "heal", "shield"])))


if __name__ == "__main__":
    main()
