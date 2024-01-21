from fastapi import FastAPI, Body, Depends, HTTPException
import schemas
import crud

from models import Package, Sender, Reciever, Rider, Status
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


# @app.get("/{str}")
# def getpackage(tracking_number: str, session: Session = Depends(get_session)):
#     package = session.query(Package).get(tracking_number)
#     return package.name


@app.get("/packages/{tracking_number}/name")
def get_package_name(tracking_number: str, db: Session = Depends(get_session)):
    # Query the database to find the package with the specified tracking_number
    package = db.query(Package).filter(
        Package.tracking_number == tracking_number).first()

    # Check if the package exists
    if package is None:
        raise HTTPException(status_code=404, detail="Package not found")

    # Return the name of the package
    return {"tracking_number": tracking_number, "package_name": package.name}


@app.post("/")
def create_package_endpoint(
    tracking_number: str,
    name: str,
    sender_name: str,
    reciever_name: str,
    rider_name: str,
    delivery_location: str,
    description: str,
    price: float,
    status: str,
    db: Session = Depends(get_session),
):
    sender = crud.create_sender(
        db, name=sender_name, location=delivery_location)
    reciever = crud.create_reciever(
        db, name=reciever_name, location=delivery_location)
    rider = crud.create_rider(db, name=rider_name)

    package = crud.create_package(
        db=db,
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

    return package
