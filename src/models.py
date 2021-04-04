import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er
from sqlalchemy import DateTime

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id= Column(Integer, primary_key=True)
    id = Column(Integer, primary_key=True)
    username = Column(String(250), nullable=False)
    password= Column(String(50), primary_key=True)

class People(Base):
    __tablename__ = 'people'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id= Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    height= Column(Integer, primary_key=True)
    mass= Column(Integer, primary_key=True)
    skin_color= Column(String(50), nullable=False)
    hair_color= Column(String(50), nullable=False)
    eye_color= Column(String(50), nullable=False)
    birth_year= Column(String(50), nullable=False)
    gender= Column(String(50), nullable=False)
    created= Column(DateTime, nullable=False)
    edited= Column(DateTime, nullable=False)
    homeworld= Column(String(250), nullable=False)
    url= Column(String(250), nullable=False)

class FavPeople(Base):
    __tablename__ = 'favpeople'
    id= Column(Integer, primary_key=True)
    id_people = Column(Integer, ForeignKey('people.id_people'))
    people = relationship(People)
    iduser = Column(Integer, ForeignKey('user.iduser'))
    user = relationship(User)

class Planets(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    diameter= Column(Integer, nullable=False)
    rotation_period= Column(Integer, nullable=False)
    orbital_period= Column(Integer, nullable=False)
    gravity= Column(String(50), nullable=False)
    population= Column(Integer, nullable=False)
    climate= Column(String(50), nullable=False)
    terrain= Column(String(50), nullable=False)
    surface_water= Column(Integer, nullable=False)
    created= Column(DateTime, nullable=False)
    edited= Column(DateTime, nullable=False)
    url= Column(String(250), nullable=False)

class FavPlanets(Base):
    __tablename__ = 'favplanets'
    id= Column(Integer, primary_key=True)
    idplaneta = Column(Integer, ForeignKey('planets.id_planets'))
    planets = relationship(Planets)
    iduser = Column(Integer, ForeignKey('user.iduser'))
    user = relationship(User)

    def to_dict(self):
        return {}

render_er(Base, 'diagram.png')




# import os
# import sys
# from sqlalchemy import Column, ForeignKey, Integer, String
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import relationship
# from sqlalchemy import create_engine
# from eralchemy import render_er

# Base = declarative_base()

# class Person(Base):
#     __tablename__ = 'person'
#     # Here we define columns for the table person
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     name = Column(String(250), nullable=False)

# class Address(Base):
#     __tablename__ = 'address'
#     # Here we define columns for the table address.
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     street_name = Column(String(250))
#     street_number = Column(String(250))
#     post_code = Column(String(250), nullable=False)
#     person_id = Column(Integer, ForeignKey('person.id'))
#     person = relationship(Person)

#     def to_dict(self):
#         return {}

# ## Draw from SQLAlchemy base
# render_er(Base, 'diagram.png')