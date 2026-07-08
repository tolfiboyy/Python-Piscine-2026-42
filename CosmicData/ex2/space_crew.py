from pydantic import BaseModel, Field, ValidationError, model_validator
from datetime import datetime
from enum import Enum


class Rank(Enum):
    COMMANDER = "commander"
    CAPTAIN = "captain"
    LIEUTENANT = "lieutenant"
    OFFICER = "officer"
    CADET = "cadet"


class CrewMember(BaseModel):
    member_id: str = Field(min_length=3, max_length=10)

    name: str = Field(min_length=2, max_length=50)

    rank: Enum

    age: int = Field(ge=18, le=80)

    specialization: str = Field(min_length=3, max_length=30)

    years_experience: int = Field(ge=0, le=50)

    is_active: bool = True


class SpaceMission(BaseModel):
    mission_id: str = Field(min_length=5, max_length=15)

    mission_name: str = Field(min_length=3, max_length=100)

    destination: str = Field(min_length=3, max_length=50)

    launch_date: datetime

    duration_days: int = Field(ge=1, le=3650)

    crew: list[CrewMember] = Field(min_length=1, max_length=12)

    mission_status: str = Field(default="planned")

    budget_millions: float = Field(ge=1.0, le=10000.0)

    @model_validator(mode="after")
    def mission_validator(self) -> "SpaceMission":

        if not self.mission_id.startswith("M"):
            raise ValueError("Mission ID must start with 'M'")

        is_there_leader = False

        for crew_member in self.crew:
            if crew_member.rank in (Rank.COMMANDER, Rank.CAPTAIN):
                is_there_leader = True
                break

        if is_there_leader is False:
            raise ValueError("Must have at least one Commander or Captain")

        if self.duration_days > 365:

            experience_count = 0

            for crew_member in self.crew:
                if crew_member.years_experience >= 5:
                    experience_count += 1

            if experience_count < len(self.crew) / 2:
                raise ValueError("Long missions (> 365 days) need 50% "
                                 "experienced crew (5+ years)")

        for crew_member in self.crew:
            if crew_member.is_active is False:
                raise ValueError("All crew members must be active")

        return self


def first_crew() -> list[CrewMember]:
    commander = CrewMember(
        member_id="C001",
        name="Sarah Connor",
        rank=Rank.COMMANDER,
        age=49,
        specialization="Mission Command",
        years_experience=17,
        is_active=True
    )

    lieutenant = CrewMember(
        member_id="L001",
        name="John Smith",
        rank=Rank.LIEUTENANT,
        age=35,
        specialization="Navigation",
        years_experience=8,
        is_active=True
    )

    officer = CrewMember(
        member_id="OFF01",
        name="Alice Johnson",
        rank=Rank.OFFICER,
        age=27,
        specialization="Engineering",
        years_experience=5,
        is_active=True
    )

    return [commander, lieutenant, officer]


def second_crew() -> list[CrewMember]:
    commander = CrewMember(
        member_id="C001",
        name="Sarah Connor",
        rank=Rank.CADET,
        age=49,
        specialization="Mission Command",
        years_experience=17,
        is_active=True
    )

    lieutenant = CrewMember(
        member_id="L001",
        name="John Smith",
        rank=Rank.LIEUTENANT,
        age=35,
        specialization="Navigation",
        years_experience=8,
        is_active=True
    )

    officer = CrewMember(
        member_id="OFF01",
        name="Alice Johnson",
        rank=Rank.OFFICER,
        age=27,
        specialization="Engineering",
        years_experience=5,
        is_active=True
    )

    return [commander, lieutenant, officer]


def main() -> None:
    print("Space Mission Crew Validation")
    print("=" * 45, end="\n\n")
    print("Valid mission created:")

    FirstCrew = first_crew()

    FirstMission = SpaceMission(
        mission_id="M2024_MARS",
        mission_name="Mars Colony Establishment",
        destination="Mars",
        launch_date=datetime.now(),
        duration_days=900,
        crew=FirstCrew,
        mission_status="launched",
        budget_millions=2500.0
    )

    print(f"Mission: {FirstMission.mission_name}")
    print(f"ID: {FirstMission.mission_id}")
    print(f"Destination: {FirstMission.destination}")
    print(f"Duration: {FirstMission.duration_days} days")
    print(f"Budget: ${FirstMission.budget_millions}M")
    print(f"Crew size: {len(FirstCrew)}")
    for crew_member in FirstCrew:
        print(f"- {crew_member.name} "
              f"({crew_member.rank.value}) "
              f"- {crew_member.specialization}")

    print()

    print("=" * 45, end="\n\n")

    try:
        SecondCrew = second_crew()

        FailedMission = SpaceMission(
            mission_id="M2024_MARS",
            mission_name="Mars Colony Establishment",
            destination="Mars",
            launch_date=datetime.now(),
            duration_days=900,
            crew=SecondCrew,
            mission_status="launched",
            budget_millions=2500.0
        )

        # to ignore the mypy i'm showing the budget,
        # all this money spent for nothing...
        print(f"{FailedMission.budget_millions}")

    except ValidationError as error:
        print("Expected validation error:")
        print(error)


if __name__ == "__main__":
    main()
