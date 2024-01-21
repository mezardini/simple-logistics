# models.py
from sqlalchemy import Column, Integer, String, Float, ForeignKey, Enum
from sqlalchemy.orm import declarative_base, relationship
from enum import Enum as PythonEnum

Base = declarative_base()


class Rider(Base):
    __tablename__ = 'rider'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(256))


class Sender(Base):
    __tablename__ = 'sender'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(256))
    location = Column(String(256))


class Reciever(Base):
    __tablename__ = 'reciever'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(256))
    location = Column(String(256))

    packagex = relationship("Package", backref="reciever")


class Status(str, PythonEnum):
    Delivered = "delivered"
    Transit = "transit"


class Package(Base):
    __tablename__ = 'package'
    id = Column(Integer, primary_key=True, index=True)
    tracking_number = Column(String(256))
    name = Column(String(256))
    sender_name = Column(String(256), ForeignKey("sender.name"))
    reciever_name = Column(String(256), ForeignKey("reciever.name"))
    rider_name = Column(String(256), ForeignKey("rider.name"))
    delivery_location = Column(String(256))
    description = Column(String)
    price = Column(Float)
    status = Column(Enum(Status), nullable=False)

    senderx = relationship("Sender", backref="package")
    recieverx = relationship("Reciever", backref="package")
    riderx = relationship("Rider", backref="package")
