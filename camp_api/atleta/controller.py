from datetime import datetime
from uuid import uuid4
from fastapi import APIRouter, HTTPException, status, Body

from camp_api.atleta.schemas import AtletaIn, AtletaOut
from camp_api.atleta.models import AtletaModel
from camp_api.cartegorias.models import CategoriaModel
from camp_api.dependencies import DatabaseDependency

from sqlalchemy.future import select

router = APIRouter()

@router.post('/', 
             summary='Criar um novo atleta',
             status_code=status.HTTP_201_CREATED,
             response_model= AtletaOut
             )

async def post(db_session: DatabaseDependency,
                atleta_in: AtletaIn = Body(...)):

    cartegoria_name = atleta_in.cartegoria.nome
    

    cartegoria = (await db_session.execute(select(CategoriaModel).filter_by(nome=cartegoria_name))).scalars().first()
    
    if not cartegoria:
        raise HTTPException(

            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f'Cartegoria nao encontrada: {cartegoria_name} Not Found'
        )
    
    #breakpoint()
    atleta_out = AtletaOut(id=uuid4(), created_at=datetime.utcnow(), **atleta_in.model_dump())
    
    atleta_model = AtletaModel(**atleta_out.model_dump())
    
    db_session.add(atleta_model)
    await db_session.commit()
    
    return atleta_out