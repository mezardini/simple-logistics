from fastapi import FastAPI, Body, Depends
import schemas
import crud
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


app = FastAPI()


# @app.on_event("startup")
# async def startup():
#     await create_db_and_tables()


@app.post("/create_package/")
def create_package_endpoint(
    name: str,
    sender_name: str,
    sender_phone: str,
    reciever_name: str,
    reciever_phone: str,
    rider_name: str,
    pickup_location: str,
    delivery_location: str,
    description: str,
    price: float,
    status: str,
    db: Session = Depends(get_session),
):
    sender = crud.create_sender(
        db, name=sender_name, location=delivery_location, phone_number=sender_phone)
    reciever = crud.create_reciever(
        db, name=reciever_name, location=delivery_location, phone_number=reciever_phone)
    # rider = crud.create_rider(db, name=rider_name)

    package = crud.create_package(
        db=db,
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

    return package


@app.post("/create-rider/")
def create_rider_endpoint(
    rider_name: str,
    location: str,
    rider_status: str, rating: int,
    db: Session = Depends(get_session),
):
    rider = crud.create_rider(
        db, name=rider_name, location=location, rider_status=rider_status, rating=rating)
    return rider


@app.get("/assign_rider/{tracking_number}/location/")
def assign_rider_to_package(
    tracking_number: str,
    # packagex: models.Package,
    db: Session = Depends(get_session),
):
    package = db.query(models.Package).filter(
        models.Package.tracking_number == tracking_number).first()

    packagex = package.pickup_location
    choice_rider = db.query(models.Rider).filter(
        models.Rider.location == packagex, models.Rider.rider_status == 'free', models.Rider.rating == 2).first()
    rider = crud.update_package_rider(db=db, package_id=tracking_number, rider=choice_rider.name)

    return choice_rider


@app.get("/all")
def get_all_packages(
    db: Session = Depends(get_session),
    ):
    packages = db.query(models.Package).all()
    return packages

