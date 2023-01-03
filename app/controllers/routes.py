from app import app
from flask import jsonify, request
from app.controllers.utils.functions import *
from app.controllers.game_data.data import data
from app.controllers.config.config import *


@app.route('/api/v1/get-game-data', methods=['GET'])
def get_game_data():
    game_data = get_random_game_data(data)
    payload = {'category': game_data[0], 'value': game_data[1]}
    return jsonify(payload)