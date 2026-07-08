from pydantic import BaseModel, Field, ValidationError
from datetime import datetime


class SpaceStation(BaseModel):
    station_id: str = Field(min_length=3, max_length=10)

    name: str = Field(min_length=1, max_length=50)

    crew_size: int = Field(ge=1, le=20)

    power_level: float = Field(ge=0.0, le=100.0)

    oxygen_level: float = Field(ge=0.0, le=100.0)

    last_maintenance: datetime

    is_operational: bool = True

    notes: str | None = Field(default=None, max_length=200)


def main() -> None:

    print("Space Station Data Validation")
    print("=" * 45, end="\n\n")

    station = SpaceStation(
        station_id="ISS001",
        name="International Space Station",
        crew_size=6,
        power_level=85.5,
        oxygen_level=92.3,
        last_maintenance=datetime(2026, 7, 7, 12, 5, 20),
        notes="Everything is ok on board"
    )

    print("Valid station created:")
    print(f"ID: {station.station_id}")
    print(f"Name: {station.name}")
    print(f"Crew: {station.crew_size}")
    print(f"Power: {station.power_level}%")
    print(f"Oxygen: {station.oxygen_level}%")
    print(f"Last service: {station.last_maintenance}")
    print(f"Status: {"Operational" if station.is_operational else "Offline"}")
    print(f"Notes: {station.notes}")

    print()
    print("=" * 45, end="\n\n")
    print("Unvalid station creation:\n")

    try:
        SpaceStation(
            station_id="ISS001",
            name="International Space Station",
            crew_size=25,
            power_level=85.5,
            oxygen_level=92.3,
            last_maintenance=datetime(2026, 7, 7, 12, 5, 20),
            notes="Everything is ok on board"
        )

    except ValidationError as error:
        print("Expected validation error:")
        print(error)


if __name__ == "__main__":
    main()
