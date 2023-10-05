from flask import abort, make_response

from config import db
from models import Part, Generator, part_schema

def read_one(part_id):
    part = Part.query.get(part_id)

    if part is not None:
        return part_schema.dump(part)
    else:
        abort(
            404, f"Part with ID {part_id} is not found"
        )

def update(part_id, part):
    existing_part = Part.query.get(part_id)

    if existing_part:
        update_part = part.schema.load(part, session=db.session)
        existing_part.price = update_part.price
        db.session.merge(existing_part)
        db.session.commit()
        return part_schema.dump(existing_part), 201
    else:
        abort(404, f"Part with ID {part_id} not found")

def delete(part_id):
    existing_part = Part.query.get(part_id)

    if existing_part:
        db.session.delete(existing_part)
        db.session.commit()
        return make_response(f"{part_id} successfully deleted", 204)
    else:
        abort(404, f"Part with ID {part_id} not found")

def create(part):
    generator_id = part.get("generator_id")
    price = part.get("price")
    name = part.get("name")
    generator = Generator.query.get(generator_id)

    if generator and price and name:
        new_part = Part(generator_id=generator_id, price=price, name=name)
        db.session.add(new_part)
        db.session.commit()
        return part_schema.dump(new_part), 201
    else:
        abort(
            404,
            f"Generator not found for ID: {generator_id}"
        )

def read_for_generator(generator_id):
    parts = Part.query.filter_by(generator_id=generator_id).all()

    if parts:
        return part_schema.dump(parts, many=True)
    else:
        abort(404, f"No parts found for Generator with ID {generator_id}")