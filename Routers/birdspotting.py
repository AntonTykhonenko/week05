from typing import Annotated, List

from fastapi import APIRouter, Depends, status
from sqlmodel import Session

from database import get_session
from Models.birdspotting import BirdSpottingCreate, BirdSpottingRead
from Repositories.birdspotting import BirdSpottingRepository

router = APIRouter(prefix="/birdspotting", tags=["Bird Spotting"])


def get_birdspotting_repository(
	session: Annotated[Session, Depends(get_session)],
) -> BirdSpottingRepository:
	"""Build the repository used by bird spotting endpoints."""

	return BirdSpottingRepository(session)


@router.get("/", response_model=List[BirdSpottingRead], status_code=status.HTTP_200_OK)
async def get_birdspotting(
	repo: Annotated[BirdSpottingRepository, Depends(get_birdspotting_repository)],
):
	"""Return all recorded bird observations with their linked bird."""

	return repo.get_all()


@router.get("/{spotting_id}", response_model=BirdSpottingRead, status_code=status.HTTP_200_OK)
async def get_birdspotting_by_id(
	spotting_id: int,
	repo: Annotated[BirdSpottingRepository, Depends(get_birdspotting_repository)],
):
	"""Return one bird observation by its identifier."""

	return repo.get_one(spotting_id)


@router.post("/", response_model=BirdSpottingRead, status_code=status.HTTP_201_CREATED)
async def add_birdspotting(
	birdspotting: BirdSpottingCreate,
	repo: Annotated[BirdSpottingRepository, Depends(get_birdspotting_repository)],
):
	"""Create a new observation linked to an existing bird."""

	return repo.insert(birdspotting)
