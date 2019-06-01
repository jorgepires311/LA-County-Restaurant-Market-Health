import os

import pandas as pd
import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine

from flask import Flask, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


#################################################
# Database Setup
#################################################

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data/los_angeles.db"
db = SQLAlchemy(app)

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(db.engine, reflect=True)

# Save references to each table
Losangeles = Base.classes.losangeles
Locations = Base.classes.locations
Scoring = Base.classes.scoring


@app.route("/")
def index():
    """Return the homepage."""
    return render_template("index.html")


@app.route("/losangeles")
def la_health_data():
    """Return the MetaData for a given data."""
    sel = [
        Losangeles.serial_number,
        Losangeles.activity_date,
        Losangeles.facility_name,
        Losangeles.score,
        Losangeles.grade,
        Losangeles.service_code,
        Losangeles.service_description,
        Losangeles.employee_id,
        Losangeles.facility_address,
        Losangeles.facility_city,
        Losangeles.facility_id,
        Losangeles.facility_state,
        Losangeles.facility_zip,
        Losangeles.owner_id,
        Losangeles.owner_name,
        Losangeles.pe_description,
        Losangeles.program_element_pe,
        Losangeles.program_name,
        Losangeles.program_status,
        Losangeles.record_id,
        Losangeles.id,
        Losangeles.row_id,
    ]


    xs = db.session.query(*sel).all()

    # Create a dictionary entry for each row of metadata information
    la_health_data_list = []
    for x in xs:
        la_health_data = {}
        la_health_data["serial_number"] = x[0]
        la_health_data["activity_date"] = x[1]
        la_health_data["facility_name"] = x[2]
        la_health_data["score"] = x[3]
        la_health_data["grade"] = x[4]
        la_health_data["service_code"] = x[5]
        la_health_data["service_description"] = x[6]
        la_health_data["employee_id"] = x[7]
        la_health_data["facility_address"] = x[8]
        la_health_data["facility_city"] = x[9]
        la_health_data["facility_id"] = x[10]
        la_health_data["facility_state"] = x[11]
        la_health_data["facility_zip"] = x[12]
        la_health_data["owner_id"] = x[13]
        la_health_data["owner_name"] = x[14]
        la_health_data["pe_description"] = x[15]
        la_health_data["program_element_pe"] = x[16]
        la_health_data["program_name"] = x[17]
        la_health_data["program_status"] = x[18]
        la_health_data["record_id"] = x[19]
        la_health_data["id"] = x[20]
        la_health_data["row_id"] = x[21]
        la_health_data_list.append(la_health_data)

    # print(la_health_data)
    return jsonify(la_health_data_list)

@app.route("/locations")
def location_data():
    """Return the MetaData for a given data."""
    sel = [
        Locations.id,
        Locations.row_id,
        Locations.facility_address,
        Locations.facility_city,
        Locations.facility_id,
        Locations.facility_state,
        Locations.facility_zip,
        Locations.lat,
        Locations.lng,
    ]

    ys = db.session.query(*sel).all()

    # Create a dictionary entry for each row of metadata information
    location_data_list = []
    for y in ys:
        location_data = {}
        location_data["id"] = y[0]
        location_data["row_id"] = y[1]
        location_data["facility_address"] = y[2]
        location_data["facility_city"] = y[3]
        location_data["facility_id"] = y[4]
        location_data["facility_state"] = y[5]
        location_data["facility_zip"] = y[6]
        location_data["lat"] = y[7]
        location_data["lng"] = y[8]
        location_data_list.append(location_data)

    # print(location_data)
    return jsonify(location_data_list)

@app.route("/scoring")
def scoring_data():
    """Return the MetaData for a given data."""
    sel = [
        Scoring.id,
        Scoring.row_id,
        Scoring.facility_id,
        Scoring.score,
        Scoring.grade,
    ]

    zs = db.session.query(*sel).all()

    # Create a dictionary entry for each row of metadata information
    scoring_data_list = []
    for z in zs:
        scoring_data = {}
        scoring_data["id"] = z[0]
        scoring_data["row_id"] = z[1]
        scoring_data["facility_id"] = z[2]
        scoring_data["score"] = z[3]
        scoring_data["grade"] = z[4]
        scoring_data_list.append(scoring_data)

    # print(scoring_data)
    return jsonify(scoring_data_list)



if __name__ == "__main__":
    app.run()
