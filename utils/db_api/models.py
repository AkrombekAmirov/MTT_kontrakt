from sqlmodel import SQLModel, Field
from datetime import datetime


class User(SQLModel, table=True):
    id: int = Field(primary_key=True, index=True)
    name: str
    passport: str
    telegram_id: str
    telegram_number: str
    contract_number: str
    telegram_name: str
    username: str
    file_id: str
    faculty: str
    created_date: str = Field(default=datetime.now().strftime("%Y-%m-%d"))
    created_time: str = Field(default=datetime.now().strftime("%H:%M:%S"))


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
