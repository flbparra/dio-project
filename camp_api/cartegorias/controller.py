from pydantic import UUID4
from sqlalchemy.future import select
from uuid import uuid4
from fastapi import APIRouter, HTTPException, status, Body

from camp_api.cartegorias.models import CategoriaModel
from camp_api.cartegorias.schemas import CategoriaIn, CategoriaOut

from camp_api.dependencies import DatabaseDependency

router = APIRouter()

@router.post('/', 
             summary='Criar novo categoria',
             status_code=status.HTTP_201_CREATED,
             response_model=CategoriaOut,)

async def post(db_session: DatabaseDependency,
                categoria_in: CategoriaIn = Body(...)) -> CategoriaOut:
    
    categoria_out = CategoriaOut(id=uuid4(), **categoria_in.model_dump())
    categoria_model = CategoriaModel(**categoria_out.model_dump())
    
    db_session.add(categoria_model)
    await db_session.commit()
    
    return categoria_out


@router.get('/', 
             summary='Consultar todas as categorias!',
             status_code=status.HTTP_200_OK,
             response_model=list[CategoriaOut],)

async def query(db_session: DatabaseDependency) -> list[CategoriaOut]:
    cartegorias: list[CategoriaOut] = (await db_session.execute(select(CategoriaModel))).scalars().all()
    return cartegorias

@router.get('/{id}', 
             summary='Consultar uma categoria por id',
             status_code=status.HTTP_200_OK,
             response_model=CategoriaOut,
             )

async def query(id: UUID4 ,db_session: DatabaseDependency) -> list[CategoriaOut]:
    categoria: CategoriaOut = (await db_session.execute(select(CategoriaModel).filter_by(id=id))).scalars().first()

    if not categoria:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail=f'Categoria nao encontrada no id: {id}'
                        )

    return categoria

