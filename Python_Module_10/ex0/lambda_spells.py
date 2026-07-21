


def artifact_sorter(artifacts: list[dict]) -> list[dict]
    """Orde by power"""
    return sorted(artifacts, key=lambda artifact: artifact["power"], reverse=True)

def power_filter(mages: list[dict], min_power: int) -> list[dict]
    ...


def spell_transformer(spells: list[str]) -> list[str]
    ...


def mage_stats(mages: list[dict]) -> dict
    ...


def main() -> None:
    ...


if __name__ == "__main__":
    main()
