from datetime import datetime


from sqlalchemy.orm import Mapped, relationship, mapped_column
from sqlalchemy import Integer, String, DateTime, ForeignKey

from camp_api.contrib.models import BaseModel



 
class AtletaModel(BaseModel):
    __tablename__ = "atletas"

    pk_id: Mapped[int] = mapped_column(Integer, primary_key=True)

    nome: Mapped[str] = mapped_column(String(50), nullable=False)
    matricula: Mapped[str] = mapped_column(String(50),unique=True, nullable=False)
    idade: Mapped[int] = mapped_column(Integer, nullable=False)
    nome_time: Mapped[str] = mapped_column(String(50), nullable=False)
    curso: Mapped[int] = mapped_column(String(3), nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    
    cartegoria: Mapped["CategoriaModel"] = relationship(back_populates="atletas")
    cartegoria_id: Mapped[int] = mapped_column(ForeignKey("cartegorias.pk_id"))
    local_jogo: Mapped["LocalJogoModel"] = relationship(back_populates="atletas")
    local_jogo_id: Mapped[int] = mapped_column(ForeignKey("local_jogo.pk_id"))
