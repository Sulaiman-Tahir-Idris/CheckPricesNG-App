from datetime import datetime
from config import app, db
from models import Manufacturer, Generator, Part
from flask import url_for

MANUFACTURERS_GENERATORS = [
    {
        "name": "Honda",
        "generators": [
            ("Honda 2.5kva Generator EZ3000CX", "2023-01-06 17:10:24", [
            ("Fuel Tap", "N250", "2023-01-06 17:10:24" ),
            ("Engine Seating", "N8500", "2023-01-06 17:10:24" ),
            ("Valve Plate", "N500", "2023-01-06 17:10:24" ),
        ]),
            ("Honda 5.5kva Generator EZ6500X", "2023-02-06 17:11:22", [
            ("Fuel Tap", "N250", "2023-01-06 17:10:24" ),
            ("Engine Seating", "N8500", "2023-01-06 17:10:24" ),
            ("Valve Plate", "N500", "2023-01-06 17:10:24" ),
        ]),
            ("Honda Generator EG6500CXS 5.5KVA Key-Start", "2023-03-06 17:09:11", [
            ("Fuel Tap", "N250", "2023-01-06 17:10:24" ),
            ("Engine Seating", "N8500", "2023-01-06 17:10:24" ),
            ("Valve Plate", "N500", "2023-01-06 17:10:24" ),
        ]),
        ],
    },
     {
        "name": "Thermocool",
        "generators": [
            ("Haier Thermocool 1.25Kva Generator", "2022-01-06 17:10:24", [
            ("Fuel Tap", "N250", "2023-01-06 17:10:24" ),
            ("Engine Seating", "N8500", "2023-01-06 17:10:24" ),
            ("Valve Plate", "N500", "2023-01-06 17:10:24" ),
        ]),
            ("Haier Thermocool 3.75Kva Generator", "2022-02-06 17:11:22", [
            ("Fuel Tap", "N250", "2023-01-06 17:10:24" ),
            ("Engine Seating", "N8500", "2023-01-06 17:10:24" ),
            ("Valve Plate", "N500", "2023-01-06 17:10:24" ),
        ]),
            ("Haier Thermocool 7.5Kva Generator", "2022-03-06 17:09:11", [
            ("Fuel Tap", "N250", "2023-01-06 17:10:24" ),
            ("Engine Seating", "N8500", "2023-01-06 17:10:24" ),
            ("Valve Plate", "N500", "2023-01-06 17:10:24" ),
        ]),
        ],
    },
    {
        "name": "Sumec Firman",
        "generators": [
            ("Sumec Firman 1.0Kva Generator", "2022-01-06 15:10:24", [
            ("Fuel Tap", "N250", "2023-01-06 17:10:24" ),
            ("Engine Seating", "N8500", "2023-01-06 17:10:24" ),
            ("Valve Plate", "N500", "2023-01-06 17:10:24" ),
        ]),
            ("Sumec Firman 2.5Kva Generator", "2022-02-06 15:11:22", [
            ("Fuel Tap", "N250", "2023-01-06 17:10:24" ),
            ("Engine Seating", "N8500", "2023-01-06 17:10:24" ),
            ("Valve Plate", "N500", "2023-01-06 17:10:24" ),
        ]),
            ("Sumec Firman 5.0Kva Generator", "2022-03-06 15:09:11", [
            ("Fuel Tap", "N250", "2023-01-06 17:10:24" ),
            ("Engine Seating", "N8500", "2023-01-06 17:10:24" ),
            ("Valve Plate", "N500", "2023-01-06 17:10:24" ),
        ]),
        ],
    },
    {
        "name": "Senwei",
        "generators": [
            ("Senwei 1.8Kva Generator", "2022-01-06 15:10:24", [
            ("Fuel Tap", "N250", "2023-01-06 17:10:24" ),
            ("Engine Seating", "N8500", "2023-01-06 17:10:24" ),
            ("Valve Plate", "N500", "2023-01-06 17:10:24" ),
        ]),
            ("Senwei 3.5Kva Generator", "2022-02-06 15:11:22", [
            ("Fuel Tap", "N250", "2023-01-06 17:10:24" ),
            ("Engine Seating", "N8500", "2023-01-06 17:10:24" ),
            ("Valve Plate", "N500", "2023-01-06 17:10:24" ),
        ]),
            ("Senwei 4.5Kva Generator", "2022-03-06 15:09:11", [
            ("Fuel Tap", "N250", "2023-01-06 17:10:24" ),
            ("Engine Seating", "N8500", "2023-01-06 17:10:24" ),
            ("Valve Plate", "N500", "2023-01-06 17:10:24" ),
        ]),
        ],
    },
]

#Define image URLs for each part
BASE_URL = "http://localhost:8000/static/"

#Define Image URLs for each Generator
GENERATOR_IMAGES = [
    {"name": "Haier Thermocool 1.25Kva Generator", "url": BASE_URL + 'images/generators/Haier Thermocool 1.25Kva Generator.jpg'},
    {"name": "Haier Thermocool 3.75Kva Generator", "url": BASE_URL + 'images/generators/Haier Thermocool 3.75Kva Generator.jpg'},
    {"name": "Haier Thermocool 7.5Kva Generator", "url": BASE_URL + 'images/generators/Haier Thermocool 7.5Kva Generator.jpg'},
    {"name": "Honda 2.5kva Generator EZ3000CX", "url": BASE_URL + 'images/generators/Honda_2.5kva_Generator_EZ3000CX.jpg'},
    {"name": "Honda 5.5kva Generator EZ6500X", "url": BASE_URL + 'images/generators/Honda_5.5kva_Generator_EZ6500X.webp'},
    {"name": "Honda Generator EG6500CXS 5.5KVA Key-Start", "url": BASE_URL + 'images/generators/Honda_Generator_EG6500CXS_5.5KVA_Key-Start.webp'},
    {"name": "Senwei 1.8Kva Generator", "url": BASE_URL + 'images/generators/Senwei 1.8Kva Generator.jpg'},
    {"name": "Senwei 3.5Kva Generator", "url": BASE_URL + 'images/generators/Senwei 3.5Kva Generator.jpg'},
    {"name": "Senwei 4.5Kva Generator", "url": BASE_URL + 'images/generators/Senwei 4.5Kva Generator.jpg'},
    {"name": "Sumec Firman 1.0Kva Generator", "url": BASE_URL + 'images/generators/Sumec Firman 1.0Kva Generator.webp'},
    {"name": "Sumec Firman 2.5Kva Generator", "url": BASE_URL + 'images/generators/Sumec Firman 2.5Kva Generator.png'},
    {"name": "Sumec Firman 5.0Kva Generator", "url": BASE_URL + 'images/generators/Sumec Firman 5.0Kva Generator.png'},
]


PART_IMAGES = [
    {"name": "Fuel Tap", "url": BASE_URL + 'images/sumec/sumec_one/parts/fuel_tap.jpg'},
    {"name": "Valve Plate", "url": BASE_URL + 'images/sumec/sumec_one/parts/valve_plate.jpg'},
    {"name": "Plug", "url": BASE_URL + 'images/sumec/sumec_one/parts/spark_plug.jpg'},
    {"name": "Carburetor", "url": BASE_URL + 'images/sumec/sumec_one/parts/carburetor.jpg'},
    {"name": "Avr", "url": BASE_URL + 'images/sumec/sumec_one/parts/avr.jpg'},
    {"name": "Brushes", "url": BASE_URL + 'images/sumec/sumec_one/parts/brushes.jpg'},
    {"name": "Piston and Rings", "url": BASE_URL + 'images/sumec/sumec_one/parts/piston_rings.jpg'},
    {"name": "Fuel Hose", "url": BASE_URL + 'images/sumec/sumec_one/parts/fuel_hose.jpg'},
    {"name": "Starter Kit", "url": BASE_URL + 'images/sumec/sumec_one/parts/starter.jpg'},
    {"name": "Camshaft", "url": BASE_URL + 'images/sumec/sumec_one/parts/camshaft.webp'},
    {"name": "Capacitor", "url": BASE_URL + 'images/sumec/sumec_one/parts/capacitor.jpg'},
    {"name": "Rope", "url": BASE_URL + 'images/sumec/sumec_one/parts/rope.jpg'},
    {"name": "Oil Fill", "url": BASE_URL + 'images/sumec/sumec_one/parts/oil_fill.jpg'},
    {"name": "Ignition Coil", "url": BASE_URL + 'images/sumec/sumec_one/parts/Ignition_coil.jpg'},
    {"name": "Block Coil", "url": BASE_URL + 'images/sumec/sumec_one/parts/block_coil.jpg'},
    {"name": "Diode", "url": BASE_URL + 'images/sumec/sumec_one/parts/Diode.jpg'},
    {"name": "Engine Seating", "url": BASE_URL + 'images/sumec/sumec_one/parts/engine_seating.jpg'},
    {"name": "Exhaust", "url": BASE_URL + 'images/sumec/sumec_one/parts/exhaust.jpg'},
    {"name": "Governor Control", "url": BASE_URL + 'images/sumec/sumec_one/parts/governor_control.jpg'},
    {"name": "Valve", "url": BASE_URL + 'images/sumec/sumec_one/parts/valve.jpg'},
    {"name": "Crankshaft", "url": BASE_URL + 'images/sumec/sumec_one/parts/cranskshaft.jpg'},
    {"name": "Sockets", "url": BASE_URL + 'images/sumec/sumec_one/parts/sockets.jpg'},
]


with app.app_context():
    db.drop_all()
    db.create_all()
    
    for data in MANUFACTURERS_GENERATORS:
        new_manufacturer = Manufacturer(name=data.get('name'))
        for gen_name, timestamp, parts in data.get("generators", []):
            new_generator = Generator(
                    generator_name = gen_name,
                    timestamp = datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S"),
                )
            
            #Find the corresponding image URL for the generator
            generator_image = next((g["url"] for g in GENERATOR_IMAGES if g["name"] == gen_name), None)

            if generator_image:
                new_generator.image_url = generator_image


            for part_name, part_price, part_timestamp in parts:
                new_part = Part(
                    name = part_name,
                    price = part_price, 
                    timestamp = datetime.strptime(part_timestamp, "%Y-%m-%d %H:%M:%S"),
                )

                # Find the corresponding image URL for the part
                part_image = next((p["url"] for p in PART_IMAGES if p["name"] == part_name), None)

                if part_image:
                    new_part.image_url = part_image

                new_generator.parts.append(new_part)

            new_manufacturer.generators.append(new_generator)
        db.session.add(new_manufacturer)
    db.session.commit()
