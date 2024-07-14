from typing import Annotated
from pydantic import Field, UUID4

from camp_api.contrib.schemas import BaseSchema


class LocalJogoIn(BaseSchema):
    nome: Annotated[
        str,
        Field(description="Nome do local do jogo", example="Guara Futsal", max_length=20),
    ]
    endereco: Annotated[
        str,
        Field(description="Endereço da Quadra", example="Quadra 30 TR Bixo", max_length=60),
    ]
    proprietario: Annotated[str, Field(description="Nome do dono", example="Parra", max_length=30)]



class LocalJogoAtleta(BaseSchema):
    nome: Annotated[
        str,
        Field(description="Nome do local do jogo", example="Guara Futsal", max_length=20),
    ]

class LocalJogoOut(LocalJogoIn):
    id: Annotated[UUID4, Field(description="Identificador do local de Jogo")]