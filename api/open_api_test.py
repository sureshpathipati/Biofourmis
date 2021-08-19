import requests
import random
from api.end_points import Endpoints

def test_card_deck_count(request):
		deck_number = random.randint(1, 25)
		end_point = Endpoints.NEW_DECK % deck_number
		response = requests.get(end_point)
		assert response.status_code == 200
		assert response.json()["remaining"] == deck_number*52
		assert response.json()["success"] == True


def test_card_deck_updation(request):
		deck_number = random.randint(1, 25)
		pluck_card = random.randint(1, 5)
		end_point = Endpoints.NEW_DECK % deck_number
		response = requests.get(end_point)
		deck_id = response.json()["deck_id"]
		updation_end_point = Endpoints.UPDATION_DECK.format(deck_id, pluck_card)
		response = requests.get(updation_end_point)
		assert response.status_code == 200
		assert response.json()["remaining"] == (deck_number*52 - pluck_card)


def test_reshuffle_cards(request):
		deck_number = random.randint(1, 25)
		pluck_card = random.randint(1, 5)
		end_point = Endpoints.NEW_DECK % deck_number		
		response = requests.get(end_point)
		deck_id = response.json()["deck_id"]
		updation_end_point = Endpoints.UPDATION_DECK.format(deck_id, pluck_card)
		response = requests.get(updation_end_point)
		reshuffle_end_point = Endpoints.SHUFFLE_DECK.format(deck_id)
		reshuffle_response = requests.get(reshuffle_end_point)
		assert reshuffle_response.status_code == 200
		assert reshuffle_response.json()['remaining'] == deck_number*52
		assert response.json()["success"] == True





