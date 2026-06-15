def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return sorted(
        artifacts, key=lambda artifact: artifact["power"], reverse=True
        )


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return list(filter(lambda mege: mege["power"] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda spell: f"* {spell} *", spells))


artifact_sorterr = ["Merlin", "power", "Fire"]
print(spell_transformer(artifact_sorterr))
