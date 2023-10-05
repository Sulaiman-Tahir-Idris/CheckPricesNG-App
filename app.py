from flask import render_template, request, redirect, url_for, flash
import os
import config
from models import Manufacturer, Generator, Part

app = config.connex_app
app.add_api(config.basedir / "swagger.yml")

@app.route("/")
def home():
    manufacturers = Manufacturer.query.all()
    return render_template("home.html", manufacturers = manufacturers)

@app.route("/generators", methods=['GET', 'POST'])
def generators():
    if request.method == 'POST':
        # Handle POST request from the form on the home page
        selected_manufacturer = request.form['manufacturer_name']
        manufacturers = Manufacturer.query.all()
        selected_manufacturer_found = None

        for manufacturer in manufacturers:
            if selected_manufacturer == manufacturer.name:
                selected_manufacturer_found = manufacturer
                break

        if selected_manufacturer_found is not None:
            return render_template('generators.html', manufacturer=selected_manufacturer_found)
        else:
            flash(f"No manufacturer found with the name: {selected_manufacturer}", "warning")
            return redirect(url_for('home'))
    elif request.method == 'GET':
        # Handle GET request (potentially from the parts page)
        manufacturer_id = request.args.get('manufacturer_id')
        manufacturer = Manufacturer.query.get(manufacturer_id)
        if manufacturer:
            return render_template('generators.html', manufacturer=manufacturer)
        else:
            flash(f"No manufacturer found with the ID: {manufacturer_id}", "warning")
            return redirect(url_for('home'))


@app.route("/parts/<int:generator_id>")
def parts(generator_id):
    generator = Generator.query.get_or_404(generator_id)
    parts = Part.query.filter_by(generator_id=generator_id).all()
    return render_template('parts.html', generator=generator, parts=parts)

@app.route("/parts/generator/<int:generator_id>")
def parts_for_generator(generator_id):
    generator = Generator.query.get_or_404(generator_id)
    parts = Part.query.filter_by(generator_id=generator_id).all()
    return render_template('parts.html', generator=generator, parts=parts)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)