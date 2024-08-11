#!/usr/bin/python3
""" Initializes a Flask Web Application """
from models import storage
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from os import environ
from flask import Flask, render_template
import uuid

app = Flask(__name__)
# app.jinja_env.trim_blocks = True
# app.jinja_env.lstrip_blocks = True


@app.teardown_appcontext
def teardown_db(error):
    """ Closes the SQLAlchemy Session """
    storage.close()


@app.route('/0-hbnb/', strict_slashes=False)
def display_hbnb():
    """ Render the HBNB homepage """
    states = list(storage.all(State).values())
    states.sort(key=lambda state: state.name)
    state_city_list = []

    for state in states:
        cities = sorted(state.cities, key=lambda city: city.name)
        state_city_list.append([state, cities])

    amenities = list(storage.all(Amenity).values())
    amenities.sort(key=lambda amenity: amenity.name)

    places = list(storage.all(Place).values())
    places.sort(key=lambda place: place.name)
    cache_id = uuid.uuid4()

    return render_template('0-hbnb.html',
                           states=state_city_list,
                           amenities=amenities,
                           places=places,
                           cache_id=cache_id)


if __name__ == "__main__":
    """ Runs the application """
    app.run(host='0.0.0.0', port=5000)
