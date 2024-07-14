from typing import Annotated
from pydantic import BaseModel, Field

from camp_api.cartegorias.schemas import CategoriaIn
from camp_api.contrib.schemas import BaseSchema, OutMixin
from camp_api.local_jogos.schemas import LocalJogoAtleta


class Atleta(BaseSchema):

    nome: Annotated[
        str,
        Field(
            description="Nome do aluno/atleta", example="Fabio Parra", max_length=50
        ),
    ]
    matricula: Annotated[
        str,
        Field(
            description="Matricula do Aluno/atleta", example="211020976", max_length=9
        ),
    ]
    idade: Annotated[int, Field(description="Idade do Aluno/atleta", example=21)]
    nome_time: Annotated[
        str,
        Field(
            description="Time do Aluno/atleta", example="Flamengudo", max_length=100
        ),
    ]
    curso: Annotated[
        str, Field(description="Curso do Aluno/atleta", example="CIC", max_length=3)
    ]

    cartegoria: Annotated[CategoriaIn, Field(description="Categoria do esporte") ]
    local_jogo: Annotated[LocalJogoAtleta, Field(description="Local do jogo") ]


class AtletaIn(Atleta):
    pass

class AtletaOut(Atleta, OutMixin):
    pass