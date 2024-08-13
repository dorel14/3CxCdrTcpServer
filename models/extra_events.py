# -*- coding: UTF-8 -*-
from typing import Optional
from sqlmodel import Field, SQLModel
from datetime import  datetime

metadata = SQLModel.metadata

class extraEventsBase(SQLModel):
    event_title: str
    event_start: Optional[datetime] = Field(default=datetime.now())
    event_end: Optional[datetime] = Field(default=datetime.now())
    event_explanation: Optional[str] = Field(default=None)
    event_impact: Optional[str] = Field(default=None)
    date_added: Optional[datetime] = Field(default=datetime.now())
    date_modified: Optional[datetime] = Field(default=datetime.now())

class extraEvents(extraEventsBase, table=True):
    id: int = Field(default=None, primary_key=True, nullable=False)

class extraEventsCreate(extraEventsBase):
    date_added: Optional[datetime] = Field(default=datetime.now())
    pass

class extraEventsRead(extraEventsBase):
    id: int

class extraEventsUpdate(SQLModel):
    event_title: Optional[str]=None
    event_start: Optional[datetime] = Field(default=datetime.now())
    event_end: Optional[datetime] = Field(default=datetime.now(), nullable=True)
    event_explanation: Optional[str] = Field(default=None)
    event_impact: Optional[str] = Field(default=None)
    date_modified: Optional[datetime] = Field(default=datetime.now())