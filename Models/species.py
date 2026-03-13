from decimal import Decimal
from typing import Optional
from sqlmodel import Field, SQLModel

class SpeciesBase(SQLModel):
    """Shared species fields used by request and response models."""

    name: str
    scientific_name: str
    family: str
    conservation_status: str
    wingspan_cm: Decimal

class Species(SpeciesBase, table=True):
    """Database table model for bird species."""

    id: Optional[int] = Field(default=None, primary_key=True)

class SpeciesCreate(SpeciesBase):
    """Request body for creating a species."""

    pass


class SpeciesRead(SpeciesBase):
    """Response model returned for species resources."""

    id: int