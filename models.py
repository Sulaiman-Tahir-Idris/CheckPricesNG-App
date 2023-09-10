from datetime import datetime
from config import db, ma
from marshmallow_sqlalchemy import fields


class Part(db.Model):
    __tablename__ = "part"
    id = db.Column(db.Integer, primary_key = True)
    generator_id = db.Column(db.Integer, db.ForeignKey("generator.id"))
    price = db.Column(db.String, nullable = False)
    name = db.Column(db.String, nullable = False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


class Generator(db.Model):
    __tablename__ = "generator"
    id = db.Column(db.Integer, primary_key = True)
    manufacturer_id = db.Column(db.Integer, db.ForeignKey("manufacturer.id"))
    generator_name = db.Column(db.String, nullable=False)
    timestamp = db.Column(db.DateTime, default = datetime.utcnow, onupdate = datetime.utcnow)
    parts = db.relationship(
        Part,
        backref = "generator",
        cascade = "all, delete, delete-orphan",
        single_parent = True,
        order_by = "desc(Part.timestamp)"
    ) 



class GeneratorSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Generator
        load_instance = True
        sqla_session = db.session
        include_fk = True


class Manufacturer(db.Model):
    __tablename__ = "manufacturer"
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(32), unique = True)
    timestamp = db.Column(db.DateTime, default = datetime.utcnow, onupdate = datetime.utcnow)
    generators = db.relationship(
        Generator,
        backref="manufacturer", 
        cascade="all, delete, delete-orphan",
        single_parent = True,
        order_by = "desc(Generator.timestamp)"
    )


class ManufacturerSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Manufacturer
        load_instance = True
        sqla_session = db.session
        include_relationship = True
    generators = fields.Nested(GeneratorSchema, many = True)

generator_schema = GeneratorSchema()
manufacturer_schema = ManufacturerSchema()
manufacturers_schema = ManufacturerSchema(many = True)