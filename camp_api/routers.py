from fastapi import APIRouter

from camp_api.atleta.controller import router as atleta 
from camp_api.cartegorias.controller import router as categorias
from camp_api.local_jogos.controller import router as local_jogo


api_rounter = APIRouter()

api_rounter.include_router(atleta, prefix='/atletas', tags=['atletas'])
api_rounter.include_router(categorias, prefix='/categoria', tags=['categorias'])
api_rounter.include_router(local_jogo, prefix='/local_jogo', tags=['local_jogo'])

