from typing import Optional
from sqlmodel import Field, Relationship, SQLModel
from Models.species import Species

class BirdBase(SQLModel):
    """Shared bird fields used by request and response models."""

    nickname: str
    ring_code: str
    age: int

class Bird(BirdBase, table=True):
    """Database table model for tracked birds."""

    __tablename__ = "birds"

    id: Optional[int] = Field(default=None, primary_key=True)
    species_id: int = Field(foreign_key="species.id")
    species: Optional[Species] = Relationship()

class BirdCreate(BirdBase):
    """Request body for creating a bird."""

    species_id: int


class BirdRead(BirdBase):
    """Response model returned for bird resources."""

    id: int
    species_id: int