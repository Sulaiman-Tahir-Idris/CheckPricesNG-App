from flask import abort, make_response
from config import db
from models import Manufacturer, manufacturer_schema, manufacturers_schema

def read_all():
    manufacturers = Manufacturer.query.all()
    return manufacturers_schema.dump(manufacturers)

def create(manufacturer):
    name = manufacturer.get("name")
    existing_manufacturer = Manufacturer.query.filter(Manufacturer.name == name).one_or_none()

    if existing_manufacturer is None:
        new_manufacturer = manufacturer_schema.load(manufacturer, session=db.session)
        db.session.add(new_manufacturer)
        db.session.commit()
        return manufacturer_schema.dump(new_manufacturer), 201
    else:
        abort(
            406,
            f"Manufacturer with name {name} already exists",
        )

def read_one(name):
    manufacturer = Manufacturer.query.filter(Manufacturer.name == name).one_or_none()
    if manufacturer is not None:
        return manufacturer_schema.dump(manufacturer)
    else:
        abort(
            404, f"Manufacturer with name{name} not found"
        )

def update(name, manufacturer):
    existing_manufacturer = Manufacturer.query.filter(Manufacturer.name == name).one_or_none()
    
    if existing_manufacturer:
        update_manufacturer = manufacturer_schema.load(manufacturer, session=db.session)
        existing_manufacturer.name = update_manufacturer.name
        db.session.merge(existing_manufacturer)
        db.session.commit()
        return manufacturer_schema.dump(existing_manufacturer), 201
    else:
        abort(
            404, 
            f"Manufacturer with name {name} not found"
        )

def delete(name):
    existing_manufacturer = Manufacturer.query.filter(Manufacturer.name == name).one_or_none()
    
    if existing_manufacturer:
        db.session.delete(existing_manufacturer)
        db.session.commit()
        return make_response(f"{name} successfully deleted", 200)
    else:
        abort(
            404,
            f"Manufacturer with name {name} not found"
        )