import json
import os

def load_game_data(file_path):
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"No such file: '{file_path}'")
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data


def save_game_data(file_path, data):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)


def update_game_score(data, player_id, score):
    if player_id in data:
        data[player_id]['score'] += score
    else:
        data[player_id] = {'score': score}


def get_top_players(data, top_n=5):
    sorted_players = sorted(data.items(), key=lambda item: item[1]['score'], reverse=True)
    return dict(sorted_players[:top_n])

if __name__ == '__main__':
    game_data = load_game_data('game_data.json')
    update_game_score(game_data, 'player1', 300)
    save_game_data('game_data.json', game_data)
    top_players = get_top_players(game_data)
    print(top_players)