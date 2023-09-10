from datetime import datetime
from config import app, db
from models import Manufacturer, Generator, Part

MANUFACTURERS_GENERATORS = [
    {
        "name": "Honda",
        "generators": [
            ("Honda Gen 1", "2023-01-06 17:10:24", [
            ("Fuel Tap", "N250", "2023-01-06 17:10:24" ),
            ("Engine Top", "N8500", "2023-01-06 17:10:24" ),
            ("Valve Plate", "N500", "2023-01-06 17:10:24" ),
        ]),
            ("Honda Gen 2", "2023-02-06 17:11:22", [
            ("Fuel Tap", "N250", "2023-01-06 17:10:24" ),
            ("Engine Top", "N8500", "2023-01-06 17:10:24" ),
            ("Valve Plate", "N500", "2023-01-06 17:10:24" ),
        ]),
            ("Honda Gen 3", "2023-03-06 17:09:11", [
            ("Fuel Tap", "N250", "2023-01-06 17:10:24" ),
            ("Engine Top", "N8500", "2023-01-06 17:10:24" ),
            ("Valve Plate", "N500", "2023-01-06 17:10:24" ),
        ]),
        ],
    },
     {
        "name": "Lutian",
        "generators": [
            ("Lutian Gen 1", "2022-01-06 17:10:24", [
            ("Fuel Tap", "N250", "2023-01-06 17:10:24" ),
            ("Engine Top", "N8500", "2023-01-06 17:10:24" ),
            ("Valve Plate", "N500", "2023-01-06 17:10:24" ),
        ]),
            ("Lutian Gen 2", "2022-02-06 17:11:22", [
            ("Fuel Tap", "N250", "2023-01-06 17:10:24" ),
            ("Engine Top", "N8500", "2023-01-06 17:10:24" ),
            ("Valve Plate", "N500", "2023-01-06 17:10:24" ),
        ]),
            ("Lutian Gen 3", "2022-03-06 17:09:11", [
            ("Fuel Tap", "N250", "2023-01-06 17:10:24" ),
            ("Engine Top", "N8500", "2023-01-06 17:10:24" ),
            ("Valve Plate", "N500", "2023-01-06 17:10:24" ),
        ]),
        ],
    },
    {
        "name": "Sumec Firman",
        "generators": [
            ("Sumec Gen 1", "2022-01-06 15:10:24", [
            ("Fuel Tap", "N250", "2023-01-06 17:10:24" ),
            ("Engine Top", "N8500", "2023-01-06 17:10:24" ),
            ("Valve Plate", "N500", "2023-01-06 17:10:24" ),
        ]),
            ("Sumec Gen 2", "2022-02-06 15:11:22", [
            ("Fuel Tap", "N250", "2023-01-06 17:10:24" ),
            ("Engine Top", "N8500", "2023-01-06 17:10:24" ),
            ("Valve Plate", "N500", "2023-01-06 17:10:24" ),
        ]),
            ("Sumec Gen 3", "2022-03-06 15:09:11", [
            ("Fuel Tap", "N250", "2023-01-06 17:10:24" ),
            ("Engine Top", "N8500", "2023-01-06 17:10:24" ),
            ("Valve Plate", "N500", "2023-01-06 17:10:24" ),
        ]),
        ],
    },
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
            for part_name, part_price, part_timestamp in parts:
                new_part = Part(
                    name = part_name,
                    price = part_price, 
                    timestamp = datetime.strptime(part_timestamp, "%Y-%m-%d %H:%M:%S"),
                )
                new_generator.parts.append(new_part)

            new_manufacturer.generators.append(new_generator)
        db.session.add(new_manufacturer)
    db.session.commit()