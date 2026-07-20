from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field, ValidationError


class SpaceStation(BaseModel):
    station_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=1, max_length=50)
    crew_size: int = Field(ge=1, le=20)
    power_level: float = Field(ge=0.0, le=100.0)
    oxygen_level: float = Field(ge=0.0, le=100.0)
    last_maintenance: datetime
    is_operational: bool = Field(default=True)
    notes: Optional[str] = Field(max_length=200)


def display_station(station: SpaceStation) -> None:
    print("ID:", station.station_id)
    print("Name:", station.name)
    print(f"Crew: {station.crew_size} people")
    print(f"Power: {station.power_level}%")
    print(f"Oxygen: {station.oxygen_level}%")
    print("Status:", "Operational"
          if station.is_operational else "Non-operational")


def main() -> None:

    print("Space Station Data Validation")
    print("=" * 40)

    # Valid station
    try:
        valid_data = {
            "station_id": "ISS001",
            "name": "International Space Station",
            "crew_size": 6,
            "power_level": 85.5,
            "oxygen_level": 92.3,
            "last_maintenance": "2026-07-20T21:22:00",
            "is_operational": True,
            "notes": "All systems nominal."
        }
        station = SpaceStation.model_validate(valid_data)
        display_station(station)
    except ValidationError as e:
        print("Expected validation error:")
        print(e)

    # Invalid station
    print()
    print("=" * 40)
    try:
        invalid_data = {
            "station_id": "ISS001",
            "name": "International Space Station",
            "crew_size": 25,
            "power_level": 85.5,
            "oxygen_level": 92.3,
            "last_maintenance": "2026-07-20T21:22:00",
            "is_operational": True,
            "notes": "All systems nominal."
        }
        invalid_station_data = SpaceStation.model_validate(invalid_data)
        display_station(invalid_station_data)
    except ValidationError as e:
        print("Expected validation error:")
        for error in e.errors():
            print(f"{error['msg']}")


if __name__ == "__main__":
    main()
