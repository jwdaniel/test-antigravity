from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.db.session import get_db
from app.models.item import Item
from app.schemas.item import ItemCreate, Item as ItemSchema

router = APIRouter()

@router.post("/", response_model=ItemSchema)
async def create_item(item: ItemCreate, db: AsyncSession = Depends(get_db)):
    db_item = Item(title=item.title, description=item.description)
    db.add(db_item)
    await db.commit()
    await db.refresh(db_item)
    return db_item

@router.get("/", response_model=List[ItemSchema])
async def read_items(skip: int = 0, limit: int = 100, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Item).offset(skip).limit(limit))
    items = result.scalars().all()
    return items
