ARTIFACTS = [{'name': 'Wind Cloak', 'power': 97, 'type': 'relic'},
             {'name': 'Light Prism', 'power': 65, 'type': 'accessory'},
             {'name': 'Shadow Blade', 'power': 71, 'type': 'relic'},
             {'name': 'Storm Crown', 'power': 135, 'type': 'accessory'}]

MAGES = [{'name': 'Ash', 'power': 97, 'element': 'ice'},
         {'name': 'River', 'power': 84, 'element': 'earth'},
         {'name': 'Morgan', 'power': 78, 'element': 'wind'},
         {'name': 'Zara', 'power': 67, 'element': 'light'},
         {'name': 'Casey', 'power': 56, 'element': 'ice'}]

SPELLS = ['heal', 'freeze', 'flash', 'fireball']


def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return sorted(artifacts,
                  key=lambda artifact: artifact["power"], reverse=True)


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return list(filter(lambda mage: mage["power"] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda spell: f"* {spell} *", spells))


def mage_stats(mages: list[dict]) -> dict:

    max_mage = max(mages, key=lambda mage: mage["power"])

    min_mage = min(mages, key=lambda mage: mage["power"])

    total = sum(mage["power"] for mage in mages)

    average = round(total / len(mages), 2)

    return {"max_power": max_mage["power"],
            "min_power": min_mage["power"],
            "average": average}


def main() -> None:

    # artifact testing
    print("Testing artifact sorter...")

    artifacts = artifact_sorter(ARTIFACTS)

    print(f"{artifacts[0]["name"]} ({artifacts[0]["power"]} power) comes "
          f"before {artifacts[1]["name"]} ({artifacts[1]["power"]} power)")

    # power filter testing
    print("\nTesting power filter...")

    best_mages = power_filter(MAGES, 80)

    print("These are the mage that meets the minimum power requirements:")

    i = 0

    for mage in best_mages:
        print(f"Mage [{i}]: {mage["name"]} ({mage["power"]} power)")
        i += 1

    # spell transformer testing
    print("\nTesting spell transformer...")

    spells = spell_transformer(SPELLS)
    for spell in spells:
        print(f"{spell}", end=" ")

    print()

    # mage statistics
    print("\nTesting mage stats...")

    mages = mage_stats(MAGES)

    print(f"Minimum power found in mage is {mages["min_power"]}")
    print(f"Maximum power found in mage is {mages["max_power"]}")
    print(f"Average power is {mages["average"]}")


if __name__ == "__main__":
    main()
