# FastAPI Logistics Project

This project is a FastAPI-based application for managing logistics operations. It includes a set of SQLAlchemy models for defining entities such as riders, senders, receivers, and packages. The application also features endpoints to interact with the logistics data, such as creating and retrieving packages.

## Project Structure

- **models.py:** Contains the SQLAlchemy models for defining the database schema, including Rider, Sender, Receiver, and Package entities.

- **main.py:** The main FastAPI application file. It includes endpoints for retrieving the name of a package based on its tracking number and creating a new package.

- **crud.py:** This file handles the crud operations for this app.

- **database.py:** Handles the database configuration, including creating the tables defined in models.py and providing a database session for the application.

## ENDPOINTS

1. POST /create-rider/ - create a rider

2. GET /all - get all packages

3. POST /create_package/ - create a package

4. POST /assign_rider/{tracking_number}/location/ - assign a rider to a package
