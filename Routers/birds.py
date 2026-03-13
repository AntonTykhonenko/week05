from typing import Annotated, List

from fastapi import APIRouter, Depends, status
from sqlmodel import Session

from database import get_session
from Models.birds import BirdCreate, BirdRead
from Repositories.birds import BirdRepository

router = APIRouter(prefix="/birds", tags=["Birds"])


def get_bird_repository(
	session: Annotated[Session, Depends(get_session)],
) -> BirdRepository:
	"""Build the repository used by bird endpoints."""

	return BirdRepository(session)


@router.get("/", response_model=List[BirdRead], status_code=status.HTTP_200_OK)
async def get_birds(
	repo: Annotated[BirdRepository, Depends(get_bird_repository)],
):
	"""Return all birds stored in the database."""

	return repo.get_all()


@router.post("/", response_model=BirdRead, status_code=status.HTTP_201_CREATED)
async def add_bird(
	bird: BirdCreate,
	repo: Annotated[BirdRepository, Depends(get_bird_repository)],
):
	"""Create a new bird linked to an existing species."""

	return repo.insert(bird)

