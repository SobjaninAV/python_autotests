import requests

token = 'b27b9326fc9246366bc6ca9db13346ea'
response = requests.post('https://pokemonbattle.me:5000/pokemons',
                         json={"name": "jigglypuff",
                               "photo": "https://www.pngfind.com/pngs/m/7-72826_smashwiki-super-smash-bros-ultimate-jigglypuff-hd-png.png"},
                         headers={'trainer_token': token, 'Content-Type': 'application/json'})
print(response.json())
pokemon_id = response.json()['id']

response_change = requests.put('https://pokemonbattle.me:5000/pokemons',
                               json={"pokemon_id": pokemon_id, "name": "Vasiliy", "photo": "https://static.wikia.nocookie.net/civ/images/6/61/%D0%92%D0%B0%D1%81%D0%B8%D0%BB%D0%B8%D0%B9_II_%28Civ6%29.png/revision/latest?cb=20200929133608&path-prefix=ru"},
                               headers={'trainer_token': token, 'Content-Type': 'application/json'})
print(response_change.json())

response_pokeball = requests.post("https://pokemonbattle.me:5000/trainers/add_pokeball",
                                  json={"pokemon_id": pokemon_id},
                                  headers={'trainer_token': token, 'Content-Type': 'application/json'})
print(response_pokeball.json())
