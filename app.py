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
losangeles = Base.classes.losangeles
locations = Base.classes.locations


@app.route("/")
def index():
    """Return the homepage."""
    return render_template("index.html")


@app.route("/names")
def names():
    """Return a list of sample names."""

    # Use Pandas to perform the sql query
    stmt = db.session.query(Samples).statement
    df = pd.read_sql_query(stmt, db.session.bind)

    # Return a list of the column names (sample names)
    return jsonify(list(df.columns)[2:])


@app.route("/metadata/<losengeles>")
def la_health_data(record):
    """Return the MetaData for a given sample."""
    sel = [
        losangeles.serial_number,
        losangeles.activity_date,
        losangeles.facility_name,
        losangeles.score,
        losangeles.grade,
        losangeles.service_code,
        losangeles.service_description,
        losangeles.employee_id,
        losangeles.facility_addresss,
        losangeles.facility_city,
        losangeles.facility_id,
        losangeles.facility_state,
        losangeles.facility_zip,
        losangeles.owner_id,
        losangeles.owner_name,
        losangeles.pe_description,
        losangeles.program_element_pe,
        losangeles.program_name,
        losangeles.program_status,
        losangeles.record_id,
    ]


    results = db.session.query(*sel).filter(losangeles.record == record).all()

    # Create a dictionary entry for each row of metadata information
    la_health_data = {}
    for result in results:
        la_health_data["serial_number"] = result[0]
        la_health_data["activity_date"] = result[1]
        la_health_data["facility_name"] = result[2]
        la_health_data["score"] = result[3]
        la_health_data["grade"] = result[4]
        la_health_data["service_code"] = result[5]
        la_health_data["service_description"] = result[6]
        la_health_data["employee_id"] = result[7]
        la_health_data["facility_address"] = result[8]
        la_health_data["facility_city"] = result[9]
        la_health_data["facility_id"] = result[10]
        la_health_data["facility_state"] = result[11]
        la_health_data["facility_zip"] = result[12]
        la_health_data["owner_id"] = result[13]
        la_health_data["owner_name"] = result[14]
        la_health_data["pe_description"] = result[15]
        la_health_data["program_element_pe"] = result[16]
        la_health_data["program_name"] = result[17]
        la_health_data["program_status"] = result[18]
        la_health_data["recard_id"] = result  [19]

    print(la_health_data)
    return jsonify(la_health_data)


@app.route("/locations/<location>")
def locations(location):
    """Return location data."""
    stmt = db.session.query(locations).statement
    df = pd.read_sql_query(stmt, db.session.bind)

    # Filter the data based on the sample number and
    # only keep rows with values above 1
    locations = ["facility_id", "lat", "lon", location]]
    # Format the data to send as json
    data = {
        "facility_id": locations.facility_id.values.tolist(),
        "lat": locations.lat.values.tolist(),
        "lon": locations.lon.tolist(),
    }
    return jsonify(data)


if __name__ == "__main__":
    app.run()
