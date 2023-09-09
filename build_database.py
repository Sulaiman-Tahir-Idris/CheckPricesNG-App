from datetime import datetime
from config import app, db
from models import Manufacturer, Generator

MANUFACTURERS_GENERATORS = [
    {
        "name": "Honda",
        "generators": [
            ("Honda Gen 1", "2023-01-06 17:10:24"),
            ("Honda Gen 2", "2023-02-06 17:11:22"),
            ("Honda Gen 3", "2023-03-06 17:09:11"),
        ],
    },
     {
        "name": "Lutian",
        "generators": [
            ("Lutian Gen 1", "2022-01-06 17:10:24"),
            ("Lutian Gen 2", "2022-02-06 17:11:22"),
            ("Lutian Gen 3", "2022-03-06 17:09:11"),
        ],
    },
    {
        "name": "Sumec Firman",
        "generators": [
            ("Sumec Gen 1", "2022-01-06 15:10:24"),
            ("Sumec Gen 2", "2022-02-06 15:11:22"),
            ("Sumec Gen 3", "2022-03-06 15:09:11"),
        ],
    },
]

with app.app_context():
    db.drop_all()
    db.create_all()
    
    for data in MANUFACTURERS_GENERATORS:
        new_manufacturer = Manufacturer(name=data.get('name'))
        for name, timestamp in data.get("generators", []):
            new_manufacturer.generators.append(
                Generator(
                    generator_name = name,
                    timestamp = datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S"),
                )
            )
        db.session.add(new_manufacturer)
    db.session.commit()