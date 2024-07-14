from typing import Annotated
from pydantic import UUID4, Field

from camp_api.contrib.schemas import BaseSchema


class CartegoriaIn(BaseSchema):
    nome: Annotated[
        str,
        Field(description="Nome da Categoria", example="Futsal", max_length=10),
    ]


class CartegoriaOut(CartegoriaIn):
    id: Annotated[UUID4, Field(description="Identificador da Categoria")]
