from flask import Blueprint, render_template, request, redirect, url_for, flash, abort
from .models import Destination, Comment
from .forms import DestinationForm, CommentForm
from . import db
import os
from werkzeug.utils import secure_filename
# additional import:
from flask_login import login_required, current_user

# imports to calculate recommender embeddings
from . import encoder
import json

destbp = Blueprint('destination', __name__, url_prefix='/destinations')

@destbp.route('/<id>')
def show(id):
    destination = db.session.scalar(db.select(Destination).where(Destination.id==id))
    # create the comment form
    form = CommentForm()
    # If the database doesn't return a destination, show a 404 page
    if not destination:
       abort(404)
    return render_template('destinations/show.html', destination=destination, form=form)

@destbp.route('/create', methods=['GET', 'POST'])
@login_required
def create():
  print('Method type: ', request.method)
  form = DestinationForm()
  if form.validate_on_submit():
    # Retrieve embeddings for description and convert to text
    embedding = encoder.encode(form.description.data)
    embedding_text = json.dumps(embedding.tolist())

    # call the function that checks and returns image
    db_file_path = check_upload_file(form)
    destination = Destination(name=form.name.data, description=form.description.data,
    description_embedding=embedding_text, image=db_file_path,currency=form.currency.data)
    # add the object to the db session
    db.session.add(destination)
    # commit to the database
    db.session.commit()
    flash('Successfully created new travel destination', 'success')
    # Always end with redirect when form is valid
    return redirect(url_for('destination.create'))
  return render_template('destinations/create.html', form=form)

def check_upload_file(form):
  # get file data from form  
  fp = form.image.data
  filename = fp.filename
  # get the current path of the module file… store image file relative to this path  
  BASE_PATH = os.path.dirname(__file__)
  # upload file location – directory of this file/static/image
  upload_path = os.path.join(BASE_PATH, 'static/image', secure_filename(filename))
  # store relative path in DB as image location in HTML is relative
  db_upload_path = '/static/image/' + secure_filename(filename)
  # save the file and return the db upload path
  fp.save(upload_path)
  return db_upload_path

@destbp.route('/<id>/comment', methods=['GET', 'POST'])  
@login_required
def comment(id):  
    form = CommentForm()  
    # get the destination object associated to the page and the comment
    destination = db.session.scalar(db.select(Destination).where(Destination.id==id))
    if form.validate_on_submit():  
      # read the comment from the form
      comment = Comment(text=form.text.data, destination=destination, user=current_user) 
      # here the back-referencing works - comment.destination is set
      # and the link is created
      db.session.add(comment) 
      db.session.commit() 
      # flashing a message which needs to be handled by the html
      flash('Your comment has been added', 'success')  
      # print('Your comment has been added', 'success') 
    # using redirect sends a GET request to destination.show
    return redirect(url_for('destination.show', id=id))

'''
################################################################################
# Seed database
# place temporarily in to destinations.py and visit /destinations/populate
# need to manually add the images
################################################################################


@destbp.route('/populate')
def populate():
    print ("Populating Database with data")

    path = "/static/image/"

    ### Add a destination
    name = "Japan"
    currency = "Japanese Yen (JPY)"
    description = "Japan combines ancient traditions with cutting-edge technology. Visitors can explore historic temples in Kyoto, experience the vibrant nightlife of Tokyo, relax in natural hot springs, and enjoy world-famous cuisine including sushi and ramen. Popular activities include cherry blossom viewing, hiking mountain trails, visiting cultural festivals, and shopping in modern entertainment districts."
    image = path + "Japan.jpeg"
    embedding = encoder.encode(description)
    embedding_text = json.dumps(embedding.tolist())
    d = Destination(name=name, description=description, description_embedding=embedding_text, image=image, currency=currency)
    db.session.add(d)
    db.session.commit()

    ### Add a destination
    name = "Australia"
    currency = "Australian Dollar (AUD)"
    description = "Australia offers diverse travel experiences ranging from tropical beaches and coral reefs to rugged deserts and cosmopolitan cities. Travellers can snorkel the Great Barrier Reef, explore national parks, encounter unique wildlife such as kangaroos and koalas, and enjoy outdoor adventures including hiking, surfing, and camping in spectacular natural landscapes."
    image = path + "Australia.jpeg"
    embedding = encoder.encode(description)
    embedding_text = json.dumps(embedding.tolist())
    d = Destination(name=name, description=description, description_embedding=embedding_text, image=image, currency=currency)
    db.session.add(d)
    db.session.commit()

    ### Add a destination
    name = "Italy"
    currency = "Euro (EUR)"
    description = "Italy is renowned for its rich history, art, architecture, and cuisine. Visitors can discover ancient Roman landmarks, explore Renaissance museums, dine on authentic pasta and pizza, and enjoy picturesque coastal villages. Activities include wine tasting, sightseeing in historic cities, visiting archaeological sites, and experiencing local cultural traditions."
    image = path + "Italy.jpeg"
    embedding = encoder.encode(description)
    embedding_text = json.dumps(embedding.tolist())
    d = Destination(name=name, description=description, description_embedding=embedding_text, image=image, currency=currency)
    db.session.add(d)
    db.session.commit()

       ### Add a destination
    name = "New Zealand"
    currency = "New Zealand Dollar (NZD)"
    description = "New Zealand attracts travellers seeking breathtaking scenery and outdoor adventure. Visitors can enjoy mountain hiking, glacier tours, scenic drives, and water sports in pristine natural environments. Popular activities include exploring national parks, visiting volcanic regions, experiencing Māori culture, and participating in adventure sports such as bungee jumping and kayaking."
    image = path + "New_Zealand.jpeg"
    embedding = encoder.encode(description)
    embedding_text = json.dumps(embedding.tolist())
    d = Destination(name=name, description=description, description_embedding=embedding_text, image=image, currency=currency)
    db.session.add(d)
    db.session.commit()

    ### Add a destination
    name = "Thailand"
    currency = "Thai Baht (THB)"
    description = "Thailand is famous for tropical islands, vibrant street markets, ornate temples, and flavourful cuisine. Travellers can relax on sandy beaches, explore bustling night markets, visit cultural landmarks, and enjoy activities such as island hopping, scuba diving, boat tours, and cooking classes featuring traditional Thai dishes."
    image = path + "Thailand.jpeg"
    embedding = encoder.encode(description)
    embedding_text = json.dumps(embedding.tolist())
    d = Destination(name=name, description=description, description_embedding=embedding_text, image=image, currency=currency)
    db.session.add(d)
    db.session.commit()

    ### Add a destination
    name = "Switzerland"
    currency = "Swiss Franc (CHF)"
    description = "Switzerland offers stunning alpine scenery, charming villages, and excellent outdoor recreation opportunities. Visitors can ride scenic railways through mountain regions, ski world-class slopes, hike picturesque trails, and enjoy crystal-clear lakes. The country is also known for luxury travel experiences, fine chocolate, and historic European towns."
    image = path + "Switzerland.jpeg"
    embedding = encoder.encode(description)
    embedding_text = json.dumps(embedding.tolist())
    d = Destination(name=name, description=description, description_embedding=embedding_text, image=image, currency=currency)
    db.session.add(d)
    db.session.commit()

    ### Add a destination
    name = "Egypt"
    currency = "Egyptian Pound (EGP)"
    description = "Egypt attracts travellers interested in ancient history and archaeological wonders. Visitors can explore the pyramids, cruise along the Nile River, visit temples and museums, and learn about one of the world's oldest civilisations. Popular activities include desert tours, cultural sightseeing, photography, and exploring historic monuments."
    image = path + "Egypt.jpeg"
    embedding = encoder.encode(description)
    embedding_text = json.dumps(embedding.tolist())
    d = Destination(name=name, description=description, description_embedding=embedding_text, image=image, currency=currency)
    db.session.add(d)
    db.session.commit()

    ### Add a destination
    name = "Canada"
    currency = "Canadian Dollar (CAD)"
    description = "Canada offers vast wilderness, vibrant cities, and exceptional outdoor experiences. Travellers can visit spectacular national parks, observe wildlife, hike mountain trails, ski in winter resorts, and explore multicultural urban destinations. Popular activities include canoeing, camping, wildlife watching, and scenic road trips through forests and lakes."
    image = path + "Canada.jpeg"
    embedding = encoder.encode(description)
    embedding_text = json.dumps(embedding.tolist())
    d = Destination(name=name, description=description, description_embedding=embedding_text, image=image, currency=currency)
    db.session.add(d)
    db.session.commit()

    ### Add a destination
    name = "France"
    currency = "Euro (EUR)"
    description = "France combines iconic cultural attractions, sophisticated cuisine, and diverse regional experiences. Visitors can admire historic architecture, explore world-famous museums, enjoy wine regions, and relax in charming countryside villages. Activities include culinary tours, shopping, sightseeing, cycling, and exploring coastal and mountain destinations."
    image = path + "France.jpeg"
    embedding = encoder.encode(description)
    embedding_text = json.dumps(embedding.tolist())
    d = Destination(name=name, description=description, description_embedding=embedding_text, image=image, currency=currency)
    db.session.add(d)
    db.session.commit()

       ### Add a destination
    name = "Costa Rica"
    currency = "Costa Rican Colón (CRC)"
    description = "Costa Rica is a leading destination for ecotourism and nature-based travel. Visitors can explore rainforests, observe wildlife, relax on tropical beaches, and experience sustainable tourism attractions. Popular activities include zip-lining, volcano tours, bird watching, surfing, hiking, and guided wildlife excursions in protected national parks."
    image = path + "Costa_Rica.jpeg"
    embedding = encoder.encode(description)
    embedding_text = json.dumps(embedding.tolist())
    d = Destination(name=name, description=description, description_embedding=embedding_text, image=image, currency=currency)
    db.session.add(d)
    db.session.commit()

    print ("Database population complete")
    return "<h1>Database populated with data</h1><p>"


'''