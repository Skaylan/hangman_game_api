import random

def get_random_game_data(data):
  key = random.choice(list(data.keys()))
  # key = 'filme'
  value = random.choice(data[key])
  return [key, value]