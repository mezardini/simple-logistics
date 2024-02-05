from sqlalchemy.orm import Session
import models
import random
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


def create_rider(db: Session, name: str, location: str, rider_status: str, rating: int):
    rider = Rider(name=name, location=location,
                  rider_status=rider_status, rating=rating)
    db.add(rider)
    db.commit()
    db.refresh(rider)
    return rider


def create_sender(db: Session, name: str, location: str, phone_number: str):
    sender = Sender(name=name, location=location, phone=phone_number)
    db.add(sender)
    db.commit()
    db.refresh(sender)
    return sender


def create_reciever(db: Session, name: str, location: str, phone_number: str):
    reciever = Reciever(name=name, location=location, phone=phone_number)
    db.add(reciever)
    db.commit()
    db.refresh(reciever)
    return reciever


def create_package(
    db: Session,
    name: str,
    sender_name: str,
    reciever_name: str,
    rider_name: str,
    pickup_location: str,
    delivery_location: str,
    description: str,
    price: float,
    status: Status,
):
    package = Package(
        tracking_number=random.randint(2340, 9877),
        name=name,
        sender_name=sender_name,
        reciever_name=reciever_name,
        rider_name=rider_name,
        pickup_location=pickup_location,
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


def update_package_rider(db: Session, package_id: str, rider: str):
    package = db.query(Package).filter(
        Package.tracking_number == package_id).first()
    if package:
        package.rider_name = rider
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
