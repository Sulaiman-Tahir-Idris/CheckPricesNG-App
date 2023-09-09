from flask import abort, make_response

from config import db
from models import Generator, generator_schema, Manufacturer

def read_one(generator_id):
    generator = Generator.query.get(generator_id)

    if generator is not None:
        return generator_schema.dump(generator)
    else:
        abort(
            404, f"Generator with ID {generator_id} not found"
        )

def update(generator_id, generator):
    existing_generator = Generator.query.get(generator_id)

    if existing_generator:
        update_gen = generator_schema.load(generator, session = db.session)
        existing_generator.name = update_gen.name
        db.session.merge(existing_generator)
        db.session.commit()
        return generator_schema.dump(existing_generator), 201
    else:
        abort(404, f"Generator with ID {generator_id} not found")

def delete(generator_id):
    existing_generator = Generator.query.get(generator_id)

    if existing_generator:
        db.session.delete(existing_generator)
        db.session.commit()
        return make_response(f"{generator_id} successfully deleted", 204)
    else:
        abort(404, f"Generator with ID{generator_id} not found")

def create(generator):
    manufacturer_id = generator.get("manufacturer_id")
    manufacturer = Manufacturer.query.get(manufacturer_id)

    if manufacturer:
        new_generator = generator_schema.load(generator, session = db.session)
        manufacturer.generators.append(new_generator)
        db.session.commit()
        return generator_schema.dump(new_generator), 201
    else:
        abort( 404, f"Manufacturer not found for ID: {manufacturer_id}")