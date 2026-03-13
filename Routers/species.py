from typing import Annotated, List

from fastapi import APIRouter, Depends, status
from sqlmodel import Session

from database import get_session
from Models.species import SpeciesCreate, SpeciesRead
from Repositories.species import SpeciesRepository

router = APIRouter(prefix="/species", tags=["Species"])

def get_species_repository(
    session: Annotated[Session, Depends(get_session)],
) -> SpeciesRepository:
    """Build the repository used by species endpoints."""

    return SpeciesRepository(session)


@router.get("/", response_model=List[SpeciesRead], status_code=status.HTTP_200_OK)
async def get_species(repo: Annotated[SpeciesRepository, Depends(get_species_repository)]):
    """Return all species stored in the database."""

    return repo.get_all()


@router.post("/", response_model=SpeciesRead, status_code=status.HTTP_201_CREATED)
async def add_species(species: SpeciesCreate, repo: Annotated[SpeciesRepository, Depends(get_species_repository)]):
    """Create a new species entry."""

    return repo.insert(species)