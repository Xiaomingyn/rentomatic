from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import declarative_base

Base = declarative_base()


"""
Class represents the room object in database. 
This class is not what we are using in the business logic, but it defines the table in the SQL database
that we will use to map the 'Room' entity. The structure of this class is dictated by the needs of the 
storage layer rather than by the use cases. We could for example store 'longitude' and 'latitude' in a 
JSON field. 
Overall, it means that we have to keep the storage and the domain levels in sync and we need to manage
migrations on our own. One could use tools like *Alembic*, but the migration will not come directly from 
domain model changes.
"""
class Room(Base):
    __tablename__ = 'room'

    id = Column(Integer, primary_key=True)

    code = Column(String(40), nullable=False)
    size = Column(Integer)
    price = Column(Float)
    longitude = Column(Float)
    latitude = Column(Float)