from app import app
from flask_cors import CORS
from dotenv import load_dotenv
import os

load_dotenv()
cors = CORS(app)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')