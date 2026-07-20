from datetime import datetime
from enum import Enum
from typing import List

from pydantic import BaseModel, Field, model_validator, ValidationError


class Rank(str, Enum):
    """Enum for different ranks of SpaceCrew members"""
    CADET = "cadet"
    OFFICER = "officer"
    LIEUTENANT = "lieutenant"
    CAPTAIN = "captain"
    COMMANDER = "commander"


class CrewMember(BaseModel):
    """Model representing a crew member of a space station"""
    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    rank: Rank
    age: int = Field(ge=18, le=80)
    specialization: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(ge=0, le=50)
    is_active: bool = Field(default=True)


class SpaceMission(BaseModel):
    """Model representing a space mission with a crew"""
    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(ge=1, le=3650)  # max 10 years
    crew: List[CrewMember] = Field(min_length=1, max_length=12)
    mission_status: str = Field(default="planned")
    budget_millions: float = Field(ge=1.0, le=10000.0)

    @model_validator(mode="after")
    def mission_validation_rules(self: "SpaceMission") -> "SpaceMission":
        """Custom validation rules for SpaceMission"""

        if not self.mission_id.startswith("M"):
            """Ensure mission_id starts with 'M'"""
            raise ValueError("Mission ID must start with 'M'")

        if not any(member.rank in {Rank.CAPTAIN, Rank.COMMANDER}
                   for member in self.crew):
            """Ensure at least one Captain or Commander in the crew"""
            raise ValueError("Mission must have at least "
                             "one Commander or Captain")

        if self.duration_days > 365:
            """Ensure that long missions have experienced crew members"""
            experienced_count = sum(1 for member in self.crew
                                    if member.years_experience >= 5)
            if experienced_count < len(self.crew) / 2:
                raise ValueError("Long missions (>365 days) require"
                                 " at least 50% of the crew to have "
                                 "5+ years of experience")
        if not all(member.is_active for member in self.crew):
            """Ensure all crew members are active for the mission"""
            raise ValueError("All crew members must be active for the mission")
        return self


def display_mission(mission: SpaceMission) -> None:
    print(f"Mission: {mission.mission_name}")
    print(f"ID: {mission.mission_id}")
    print(f"Destination: {mission.destination}")
    print(f"Duration: {mission.duration_days} days")
    print(f"Budget: ${mission.budget_millions}M")
    print(f"Crew size: {len(mission.crew)}")
    print("Crew Members:")
    for member in mission.crew:
        print(f" - {member.name} ({member.rank.value})"
              f" - {member.specialization}")


def main() -> None:
    print("Space Mission Crew Validation")
    print("=" * 40)

    try:
        print("Valid mission created:")
        valid_mission = SpaceMission(
            mission_id="M2024_MARS",
            mission_name="Mars Colony Establishment",
            destination="Mars",
            launch_date=datetime(2024, 11, 15),
            duration_days=900,
            crew=[
                CrewMember(
                    member_id="C001",
                    name="Sarah Connor",
                    rank=Rank.COMMANDER,
                    age=35,
                    specialization="Mission Command",
                    years_experience=10,
                    is_active=True
                ),
                CrewMember(
                    member_id="C002",
                    name="John Smith",
                    rank=Rank.LIEUTENANT,
                    age=28,
                    specialization="Navigation",
                    years_experience=5,
                    is_active=True
                ),
                CrewMember(
                    member_id="C003",
                    name="Alice Johnson",
                    rank=Rank.OFFICER,
                    age=30,
                    specialization="Engineering",
                    years_experience=6,
                    is_active=True
                )
            ],
            mission_status="planned",
            budget_millions=2500.0
        )
        display_mission(valid_mission)
    except ValidationError as e:
        print("Expected validation error:")
        for error in e.errors():
            print(f"{error['msg']}")

    # Invalid mission (Mission don't have a Captain or Commander)
    print()
    print("=" * 40)
    try:
        invalid_mission = SpaceMission(
            mission_id="M-2024_MOON",
            mission_name="Moon Base Alpha",
            destination="Moon",
            launch_date=datetime(2024, 5, 20),
            duration_days=400,
            crew=[
                CrewMember(
                    member_id="C004",
                    name="Bob Brown",
                    rank=Rank.OFFICER,
                    age=32,
                    specialization="Science Officer",
                    years_experience=4,
                    is_active=True
                ),
                CrewMember(
                    member_id="C005",
                    name="Eve Davis",
                    rank=Rank.LIEUTENANT,
                    age=29,
                    specialization="Pilot",
                    years_experience=3,
                    is_active=True
                )
            ],
            mission_status="planned",
            budget_millions=1500.0
        )
        display_mission(invalid_mission)
    except ValidationError as e:
        print("Expected validation error:")
        for error in e.errors():
            clean_msg = error['msg'].replace("Value error, ", "")
            print(clean_msg)


if __name__ == "__main__":
    main()
