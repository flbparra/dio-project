from sqlalchemy import Integer, String
from camp_api.contrib.models import BaseModel
from sqlalchemy.orm import Mapped, relationship, mapped_column


class CartegoriaModel(BaseModel):
    __tablename__ = "cartegorias"

    pk_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    nome: Mapped[str] = mapped_column(String(10),unique=True,nullable=False)
    atletas: Mapped["AtletaModel"] = relationship("AtletaModel", back_populates="cartegoria")
