from app import app
from flask_cors import CORS
from dotenv import load_dotenv
import os

load_dotenv()
cors = CORS(app, resources={'/api/*': {'origins': ['http://localhost:3000', 'http://127.0.0.1:3000', 'http://hangman-game-api.vercel.app']}})
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')