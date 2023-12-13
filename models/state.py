#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"

    name = Column(
        String(128),
        nullable=False
    )

    from os import getenv
    typeStorage = getenv("HBNB_TYPE_STORAGE")

    if (typeStorage == "db"):
        cities = relationship('City', backref="state", cascade="all, delete")
    else:
        @property
        def cities(self):
            from models.engine.file_storage import FileStorage
            from models.city import City

            citiesArr = FileStorage.all(City)
            citiesFinalDict = {}

            for key, value in citiesArr.items():
                if value.state_id == self.id:
                    citiesFinalDict.update({key: value})
