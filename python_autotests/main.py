import requests

token = '5487c1638e623fdc7c185927f6d82fc7'
host = 'https://api.pokemonbattle.me:9104'

#Создать покемона
response_create_pokemons = requests.post (f'{host}/pokemons', json= {   
    "name": "Бульбазавр",
    "photo": "https://dolnikov.ru/pokemons/albums/001.png"
}, 
headers= {'Content-Type': 'application/json', "trainer_token": token},
)

#Смена имени покемона
response_update_pokemons =requests.put (f'{host}/pokemons', json= {
    "pokemon_id": "6129",
    "name": "Badiii",
    "photo": "https://dolnikov.ru/pokemons/albums/008.png"
}, 
headers= {'Content-Type': 'application/json',
          "trainer_token": token},
)

#Поймать покемона в покебол
response_pokemon_in_pokeball =requests.post (f'{host}/trainers/add_pokeball', json= {
    "pokemon_id": "6129",
    }, 
headers= {'Content-Type': 'application/json',
          "trainer_token": token},
)

print (response_update_pokemons.text)
print (response_pokemon_in_pokeball.text)
