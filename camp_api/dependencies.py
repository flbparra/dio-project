from fastapi import Depends
from typing import Annotated
from sqlalchemy.ext.asyncio import AsyncSession

from camp_api.configs.database import get_session

DatabaseDependency = Annotated[AsyncSession, Depends(get_session)]