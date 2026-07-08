from pydantic import BaseModel, Field, ValidationError, model_validator
from datetime import datetime
from enum import Enum


class ContactType(Enum):
    RADIO = "radio"
    VISUAL = "visual"
    PHYSICAL = "physical"
    TELEPATHIC = "telepathic"


class AlienContact(BaseModel):
    contact_id: str = Field(min_length=5, max_length=15)

    timestamp: datetime

    location: str = Field(min_length=3, max_length=100)

    contact_type: Enum

    signal_strength: float = Field(ge=0.0, le=10.0)

    durations_minutes: int = Field(ge=1, le=1440)

    witness_count: int = Field(ge=1, le=100)

    message_received: str | None = Field(default=None, max_length=500)

    is_verified: bool = False

    @model_validator(mode="after")
    def valide_contact(self) -> "AlienContact":

        if not self.contact_id.startswith("AC"):
            raise ValueError("Contact ID must start with 'AC' (Alien Contact)")

        if self.contact_type == ContactType.PHYSICAL \
                and self.is_verified is False:
            raise ValueError("Physical contact reports must be verified")

        if self.contact_type == ContactType.TELEPATHIC \
                and self.witness_count < 3:
            raise ValueError("Telepathic contact requires "
                             "at least 3 witnesses")

        if self.signal_strength > 7.0 and self.message_received is None:
            raise ValueError("Strong signals (> 7.0) "
                             "should include received messages")

        return self


def main() -> None:
    print("Alien Contact Log Validation")
    print("=" * 45, end="\n\n")
    print("Valid Contact Report")

    ValidContact = AlienContact(
        contact_id="AC_2024_001",
        timestamp=datetime(2026, 7, 7, 12, 5, 20),
        location="Area 51, Nevada",
        contact_type=ContactType.RADIO,
        signal_strength=8.5,
        durations_minutes=45,
        witness_count=5,
        message_received="’Greetings from Zeta Reticuli’"
    )

    print(f"ID: {ValidContact.contact_id}")
    print(f"Type: {ValidContact.contact_type.value}")
    print(f"Location: {ValidContact.location}")
    print(f"Signal: {ValidContact.signal_strength}/10")
    print(f"Duration: {ValidContact.durations_minutes}")
    print(f"Witnesses: {ValidContact.witness_count}")
    print(f"Message: {ValidContact.message_received}")

    print()
    print("=" * 45, end="\n\n")

    try:
        AlienContact(
            contact_id="AC_2024_001",
            timestamp=datetime(2026, 7, 7, 12, 5, 20),
            location="Area 51, Nevada",
            contact_type=ContactType.TELEPATHIC,
            signal_strength=8.5,
            durations_minutes=45,
            witness_count=1,
            message_received="’Greetings from Zeta Reticuli’"
        )

    except ValidationError as error:
        print("Expected validation error:")
        print(error)


if __name__ == "__main__":
    main()
