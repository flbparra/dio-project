from sqlalchemy import Integer, String
from camp_api.contrib.models import BaseModel
from sqlalchemy.orm import Mapped, relationship, mapped_column



class LocalJogoModel(BaseModel):
    __tablename__ = "local_jogo"

    pk_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    nome: Mapped[str] = mapped_column(String(50), unique=True,nullable=False)
    endereco: Mapped[str] = mapped_column(String(60), nullable=False)
    proprietario: Mapped[str] = mapped_column(String(30), nullable=False)
   
    atletas: Mapped["AtletaModel"] = relationship(back_populates="local_jogo")

