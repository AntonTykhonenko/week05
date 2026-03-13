from datetime import datetime
from typing import Optional

from sqlmodel import Field, Relationship, SQLModel

from Models.birds import Bird, BirdRead


class BirdSpottingBase(SQLModel):
	"""Shared bird spotting fields used by request and response models."""

	spotted_at: datetime
	location: str
	observer_name: str
	notes: Optional[str] = None


class BirdSpotting(BirdSpottingBase, table=True):
	"""Database table model for bird observations."""

	__tablename__ = "birdspotting"

	id: Optional[int] = Field(default=None, primary_key=True)
	bird_id: int = Field(foreign_key="birds.id")
	bird: Optional[Bird] = Relationship()


class BirdSpottingCreate(BirdSpottingBase):
	"""Request body for creating a bird observation."""

	bird_id: int


class BirdSpottingRead(BirdSpottingBase):
	"""Response model returned for bird observations including the linked bird."""

	id: int
	bird: BirdRead
