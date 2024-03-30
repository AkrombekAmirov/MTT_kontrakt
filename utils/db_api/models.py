from sqlmodel import SQLModel, Field
from datetime import datetime


class User(SQLModel, table=True):
    id: int = Field(primary_key=True, index=True)
    name: str
    passport: str
    telegram_id: str
    phone_number: str
    telegram_number: str
    contract_number: str
    telegram_name: str
    username: str
    file_id: str
    faculty: str
    group: str
    created_date: datetime = Field(default=datetime.now().strftime("%Y-%m-%d"), index=True)
    created_time: datetime = Field(default=datetime.now().strftime("%H:%M:%S"), index=True)


class FileChunk(SQLModel, table=True):
    id: int = Field(primary_key=True, index=True)
    file_id: str
    chunk: bytes


class FileRepository(SQLModel, table=True):
    id: int = Field(primary_key=True, index=True)
    user_id: str
    contract_number: str
    content_type: str
    file_id: str
    date: str = Field(default=datetime.now().strftime("%Y-%m-%d"))
    time: str = Field(default=datetime.now().strftime("%H:%M:%S"))
