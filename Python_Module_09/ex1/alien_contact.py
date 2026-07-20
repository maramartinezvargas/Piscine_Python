from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field, model_validator, ValidationError
import enum


class ContactType(str, enum.Enum):
    """Enum for different types of AlienContact's contact type"""
    RADIO = "radio"
    VISUAL = "visual"
    PHYSICAL = "physical"
    TELEPATHIC = "telepathic"


class AlienContact(BaseModel):
    """Model representing an alien contact event"""
    contact_id: str = Field(min_length=5, max_length=15)
    timestamp: datetime
    location: str = Field(min_length=3, max_length=100)
    contact_type: ContactType
    signal_strength: float = Field(ge=0.0, le=10.0)
    duration_minutes: int = Field(ge=1, le=1440)  # max 24 hours
    witness_count: int = Field(ge=1, le=100)
    message_received: Optional[str] = Field(max_length=500)
    is_verified: bool = Field(default=False)


@model_validator(mode="after")
def validate_business_rules(self: "AlienContact") -> "AlienContact":

    if not self.contact_id.startswith("AC-"):
        """Ensure contact_id starts with 'AC-'"""
        raise ValueError("contact_id must start with 'AC-'")

    if self.contact_type == ContactType.PHYSICAL and not self.is_verified:
        """Ensure physical contacts are verified"""
        raise ValueError("Physical contacts must be verified")

    if self.contact_type == ContactType.TELEPATHIC and self.witness_count < 3:
        """Ensure telepathic contacts have at least 3 witnesses"""
        raise ValueError("Telepathic contacts must have at least 3 witnesses")

    if self.signal_strength > 7.0 and not self.message_received:
        """Ensure strong signals have a message received"""
        raise ValueError("Contacts with signal strength > 7.0"
                         " must include a message_received")

    return self


def display_contact(contact: AlienContact) -> None:
    print("Valid contact report created:")
    print("ID:", contact.contact_id)
    print("Type:", contact.contact_type)
    print(f"Location: {contact.location}")
    print(f"Signal: {contact.signal_strength}/10")
    print(f"Duration: {contact.duration_minutes} minutes")
    print(f"Witnesses: {contact.witness_count}")
    print(f"Message: '{contact.message_received}'")


def main() -> None:
    print("Alien Contact Log Validation")
    print("=" * 40)

    # Valid contact report
    try:
        valid_contact: AlienContact = AlienContact(
            contact_id="AC-2024_001",
            timestamp=datetime.now(),
            location="Space Station Alpha",
            contact_type=ContactType.RADIO,
            signal_strength=8.0,
            duration_minutes=10,
            witness_count=5,
            message_received="Hello, Earth!"
        )
        display_contact(valid_contact)
    except ValidationError as e:
        print("Expected validation error:")
        for error in e.errors():
            print(error)

    # Invalid contact report
    print()
    print("=" * 40)
    try:
        invalid_contact: AlienContact = AlienContact(
            contact_id="2024_001",  # Invalid: does not start with 'AC-'
            timestamp=datetime.now(),
            location="Space Station Beta",
            contact_type=ContactType.TELEPATHIC,
            signal_strength=9.0,
            duration_minutes=15,
            witness_count=2,  # Invalid: less than 3 for telepathic
            message_received="42"
        )
        display_contact(invalid_contact)
    except ValidationError as e:
        print("Expected validation error:")
        for error in e.errors():
            print(f"{error['msg']}")


if __name__ == "__main__":
    main()
