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
            from models import storage
            from models.city import City

            citiesArr = storage.all(City)
            citiesFinalArr = []

            for value in citiesArr.values():
                if value.state_id == self.id:
                    citiesFinalArr.append(value)
            return citiesFinalArr
