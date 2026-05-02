import json
import os

# DEFENSE: Why use JSON? It is a standard, lightweight format to save data like dictionaries.
# It allows the settings and leaderboard to persist (not disappear) when we close the game.

def load_data(filename, default_data):
    # EXPLANATION: Checks if file exists. If yes, reads it. If no, returns default values.
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            return json.load(f)
    return default_data

def save_data(filename, data):
    # EXPLANATION: Writes the Python dictionary/list into a JSON file.
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)