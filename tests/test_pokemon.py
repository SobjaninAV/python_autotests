import requests

def test_status_code():
    response = requests.get('https://pokemonbattle.me:5000/trainers')
    assert response.status_code == 200
def test_trainer_name():
    response = requests.get('https://pokemonbattle.me:5000/trainers?trainer_id=1803')
    assert response.json()['trainer_name'] == 'Antonio'
