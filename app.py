from flask import Flask, session, render_template
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from database_setup import db
import httplib2
import json

app = Flask(__name__)

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

def get_nanodegrees():
    catalog_url = "https://catalog-api.udacity.com/v1/degrees"
    h = httplib2.Http()
    catalog_dict = json.loads(h.request(catalog_url, 'GET')[1])
    catalog = {}

    for degree in catalog_dict['degrees']:
        if degree['available'] and degree['open_for_enrollment']:
            catalog[degree['title']] = [degree['card_image'], degree['key']]

    return catalog


@app.route("/enrollment")
def index():
    catalog = get_nanodegrees()
    print(catalog.keys())
    return 'Hi :)'


if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.run(host='0.0.0.0')
