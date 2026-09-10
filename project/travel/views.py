from flask import Blueprint, render_template, request, redirect, url_for
from .models import Destination
from . import db
# imports to compare embeddings
from . import encoder
import json
import numpy as np


mainbp = Blueprint('main', __name__)

@mainbp.route('/')
def index():
    destinations = db.session.scalars(db.select(Destination)).all()    
    return render_template('index.html', destinations=destinations)

@mainbp.route('/search')
def search():
    if request.args['search'] and request.args['search'] != "":
        print(request.args['search'])
        if 'use_ai' in request.args:
            print ("AI search selected")
            query_embedding = encoder.encode(request.args['search'])
            destinations = db.session.scalars(db.select(Destination)).all()
            results = []
            for destination in destinations:
                # Convert JSON string back to array
                destination_embedding = np.array(json.loads(destination.description_embedding))
                score = cosine_similarity(query_embedding, destination_embedding)
                results.append([destination, score])
            results.sort (key=lambda x: x[1], reverse=True)
            print (results)
            destinations = [x[0] for x in results]
        else:
            query = "%" + request.args['search'] + "%"
            destinations = db.session.scalars(db.select(Destination).where(Destination.description.like(query)))
        return render_template('index.html', destinations=destinations)
    else:
        return redirect(url_for('main.index'))


def cosine_similarity(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

