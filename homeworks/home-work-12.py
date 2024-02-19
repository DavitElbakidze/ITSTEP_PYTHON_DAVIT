chess_players = [
  {'id': 19, 'name': 'Jobava', 'country': 'Georgia', 'rating': 2588, 'age': 41},
  {'id': 28, 'name': 'Caruana', 'country': 'USA', 'rating': 2781, 'age': 32},
  {'id': 35, 'name': 'Giri', 'country': 'Netherlands', 'rating': 2771, 'age': 30},
  {'id': 84, 'name': 'Carlsen', 'country': 'Norway', 'rating': 2864, 'age': 34},
  {'id': 118, 'name': 'Ding', 'country': 'China', 'rating': 2799, 'age': 32},
  {'id': 139, 'name': 'Karjakin', 'country': 'Russia', 'rating': 2747, 'age': 35},
  {'id': 258, 'name': 'Duda', 'country': 'Poland', 'rating': 2731, 'age': 31},
  {'id': 301, 'name': 'Vachier-Lagrave', 'country': 'France', 'rating': 2737, 'age': 34},
  {'id': 403, 'name': 'Nakamura', 'country': 'USA', 'rating': 2768, 'age': 36},
]
# დაწერეთ პითონის ფუნქცია რომელიც კონტექსტის მენეჯერის გამოყენებით პარამეტრად მიიღებს ფაილის მისამართს, სახელს და შემქნის მას.
# დაწერეთ პითონის ფუნქცია რომელიც წაიკითხავს პარამეტრად მიღებული ფაილის კონტენტს
# დაწერეთ პითონის ფუნქცია, რომელიც გაანახლებს ფაილში არსებულ კონტენტს
# დაწერეთ პითონის ფუნქცია რომელიც პარამეტრად მიიღებს ლექსიკონს (dict) და ჩაწერს/გაანახლებს ფაილის კონტენტს
# [
#   {'id': 568, 'name': 'Kasparov', 'country': 'Russia', 'rating': 2705, 'age': 56},
#   {'id': 189, 'name': 'Karpov', 'country': 'Russia', 'rating': 2698, 'age': 59},
# ]
# ბოლოში უნდა ჩაემატოს მხოლოდ ორი ლექსიკონი და არა სია

import json
import os

def create_file(file_path, initial_content=None):
    try:
        with open(file_path, 'w') as file:
            json.dump(initial_content or {}, file)
        print(f"File '{file_path}' created successfully.")
    except Exception as e:
        print(f"Error creating file: {e}")

def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = json.load(file)
        return content
    except FileNotFoundError:
        return None
    except Exception as e:
        print(f"Error reading file: {e}")
        return None

def update_file_with_dicts(file_path, new_data_dicts):
    try:
        existing_content = read_file(file_path) or {}

        for player_data in new_data_dicts:
            existing_content[player_data['id']] = player_data

        with open(file_path, 'w') as file:
            json.dump(existing_content, file)

        print(f"File '{file_path}' updated successfully.")
    except Exception as e:
        print(f"Error updating file: {e}")

file_path = 'chess_players.json'

new_players_dicts = [
    {'id': 568, 'name': 'Kasparov', 'country': 'Russia', 'rating': 2705, 'age': 56},
    {'id': 189, 'name': 'Karpov', 'country': 'Russia', 'rating': 2698, 'age': 59}
]

try:
    os.remove(file_path)
except FileNotFoundError:
    pass

initial_content = {}
create_file(file_path, initial_content)

update_file_with_dicts(file_path, new_players_dicts)

content = read_file(file_path)
if content:
    player1 = content.get('568', {})
    player2 = content.get('189', {})
    print("Player 1:", player1)
    print("Player 2:", player2)




