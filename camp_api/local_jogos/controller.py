from pydantic import UUID4
from sqlalchemy.future import select
from uuid import uuid4
from fastapi import APIRouter, HTTPException, status, Body

from camp_api.local_jogos.models import LocalJogoModel
from camp_api.local_jogos.schemas import LocalJogoIn, LocalJogoOut

from camp_api.dependencies import DatabaseDependency

router = APIRouter()
@router.post('/', 
             summary='Criar novo Local de Jogo',
             status_code=status.HTTP_201_CREATED,
             response_model=LocalJogoOut,)

async def post(db_session: DatabaseDependency,
                local_jogos_in: LocalJogoIn = Body(...)) -> LocalJogoOut:
    local_jogos_out = LocalJogoOut(id=uuid4(), **local_jogos_in.model_dump())
    local_jogos_model = LocalJogoModel(**local_jogos_out.model_dump())
    
    db_session.add(local_jogos_model)
    await db_session.commit()    
    return local_jogos_out


@router.get('/', 
             summary='Consultar todas os locais jogos!',
             status_code=status.HTTP_200_OK,
             response_model=list[LocalJogoOut],)

async def query(db_session: DatabaseDependency) -> list[LocalJogoOut]:
    local_jogoss: list[LocalJogoOut] = (await db_session.execute(select(LocalJogoModel))).scalars().all()
    return local_jogoss

@router.get('/{id}', 
             summary='Consultar local jogos por id',
             response_model=LocalJogoOut,
             )

async def query(id: UUID4 ,db_session: DatabaseDependency) -> list[LocalJogoOut]:
    local_jogos: LocalJogoOut = (await db_session.execute(select(LocalJogoModel).filter_by(id=id))).scalars().first()

    if not local_jogos:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail=f'local jogo nao encontrada no id: {id}'
                        )

    return local_jogos

