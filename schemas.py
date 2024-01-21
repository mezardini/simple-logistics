from pydantic import BaseModel


class Package(BaseModel):
    tracking_number: str
    name: str
    sender_name: str
    reciever_name: str
    rider_name: str
    delivery_location: str
    description: str
    price: float
    status: str


class Sender(BaseModel):
    name: str
    location: str


class Reciever(BaseModel):
    name: str
    location: str


class Rider(BaseModel):
    name: str
