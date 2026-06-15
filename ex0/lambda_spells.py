def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return sorted(
        artifacts, key=lambda artifact: artifact["power"], reverse=True
        )


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return list(filter(lambda mege: mege["power"] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda spell: f"* {spell} *", spells))


def mage_stats(mages: list[dict]) -> dict:
    powers = list(map(lambda mege: mege["power"], mages))
    return {
        "max_power": max(powers),
        "min_power": min(powers),
        "avg_power": round(sum(powers) / len(powers), 2),
    }


artifacts = [
    {"name": "Crystal Wand", "power": 50, "type": "Weapon"},
    {"name": "Dragon Orb", "power": 90, "type": "Artifact"},
    {"name": "Magic Ring", "power": 70, "type": "Accessory"},
]

meges = [
    {"name": "Crystal Wand", "power": 50, "type": "Weapon"},
    {"name": "Dragon Orb", "power": 90, "type": "Artifact"},
    {"name": "Magic Ring", "power": 70, "type": "Accessory"},
]

spells = ["Merlin", "power", "Fire"]
print("sorted artifacts:")
print(artifact_sorter(artifacts))
print("\n power mages (power >=70)")
print(power_filter(meges, 70))
print("\n spell_transformer")
print(spell_transformer(spells))
print("\n meges statistics:")
print(mage_stats(meges))
