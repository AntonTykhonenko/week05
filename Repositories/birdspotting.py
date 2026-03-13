from fastapi import HTTPException
from sqlalchemy.orm import selectinload
from sqlmodel import Session, select

from Models.birds import Bird
from Models.birdspotting import BirdSpotting, BirdSpottingCreate


class BirdSpottingRepository:
	def __init__(self, session: Session):
		self.session = session

	def get_all(self):
		statement = select(BirdSpotting).options(selectinload(BirdSpotting.bird))
		items = self.session.exec(statement).all()
		return items

	def get_one(self, spotting_id: int):
		statement = (
			select(BirdSpotting)
			.where(BirdSpotting.id == spotting_id)
			.options(selectinload(BirdSpotting.bird))
		)
		item = self.session.exec(statement).one_or_none()
		if item is None:
			raise HTTPException(status_code=404, detail="Bird spotting not found")
		return item

	def insert(self, payload: BirdSpottingCreate):
		bird = self.session.get(Bird, payload.bird_id)
		if bird is None:
			raise HTTPException(status_code=400, detail="Bird does not exist")

		item = BirdSpotting.model_validate(payload)
		self.session.add(item)
		self.session.commit()
		self.session.refresh(item)
		return self.get_one(item.id)
