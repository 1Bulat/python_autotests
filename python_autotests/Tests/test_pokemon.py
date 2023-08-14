import requests
import pytest

token = '5487c1638e623fdc7c185927f6d82fc7'
host = 'https://api.pokemonbattle.me:9104'

def test_status_code():
    response = requests.get (f'{host}/trainers', params={"trainer_id": '2014'} )
    assert response.status_code ==200

def test_part_of_answer():
    response = requests.get (f'{host}/trainers', params={"trainer_id": '2014'} )
    assert response.json ()['trainer_name'] == 'Bul3'

