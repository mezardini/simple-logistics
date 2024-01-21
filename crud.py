from sqlalchemy.orm import Session
import models

from database import Base, engine, SessionLocal
from sqlalchemy.orm import Session

Base.metadata.create_all(engine)


def get_session():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()


Rider = models.Rider
Sender = models.Sender
Reciever = models.Reciever
Package = models.Package
Status = models.Status


def create_rider(db: Session, name: str):
    rider = Rider(name=name)
    db.add(rider)
    db.commit()
    db.refresh(rider)
    return rider


def create_sender(db: Session, name: str, location: str):
    sender = Sender(name=name, location=location)
    db.add(sender)
    db.commit()
    db.refresh(sender)
    return sender


def create_reciever(db: Session, name: str, location: str):
    reciever = Reciever(name=name, location=location)
    db.add(reciever)
    db.commit()
    db.refresh(reciever)
    return reciever


def create_package(
    db: Session,
    tracking_number: str,
    name: str,
    sender_name: str,
    reciever_name: str,
    rider_name: str,
    delivery_location: str,
    description: str,
    price: float,
    status: Status,
):
    package = Package(
        tracking_number=tracking_number,
        name=name,
        sender_name=sender_name,
        reciever_name=reciever_name,
        rider_name=rider_name,
        delivery_location=delivery_location,
        description=description,
        price=price,
        status=status,
    )
    db.add(package)
    db.commit()
    db.refresh(package)
    return package


def get_package(db: Session, package_id: int):
    return db.query(Package).filter(Package.id == package_id).first()


def get_packages(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Package).offset(skip).limit(limit).all()


def update_package_status(db: Session, package_id: int, new_status: Status):
    package = db.query(Package).filter(Package.id == package_id).first()
    if package:
        package.status = new_status
        db.commit()
        db.refresh(package)
        return package
    return None


def delete_package(db: Session, package_id: int):
    package = db.query(Package).filter(Package.id == package_id).first()
    if package:
        db.delete(package)
        db.commit()
        return package
    return None
