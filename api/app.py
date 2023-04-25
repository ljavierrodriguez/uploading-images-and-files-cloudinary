import os
from flask import Flask, request, jsonify
from flask_migrate import Migrate
from flask_cors import CORS
from models import db
from dotenv import load_dotenv
import cloudinary

from routes.main import api

load_dotenv()

app = Flask(__name__)
app.config['DEBUG'] = True 
app.config['ENV'] = 'development' 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI')

db.init_app(app)
Migrate(app, db)
CORS(app)

cloudinary.config(
    cloud_name = os.getenv('CLOUDINARY_CLOUD_NAME'),
    api_key = os.getenv('CLOUDINARY_CLOUD_API_KEY'),
    api_secret = os.getenv('CLOUDINARY_CLOUD_API_SECRET'),
    secure = True
)

app.register_blueprint(api)

if __name__ == '__main__':
    app.run()
