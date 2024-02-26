from src.HeadHunterAPI import Vacancy
from src.JSON_saver import JSONSaver
from data import *

json_saver = JSONSaver()
vacancy = Vacancy('vak', 'www', {'from': 0, 'to': 0, 'currency': 'RUR', 'gross': False}, 'описание')

def test_add_vacancy():
    json_saver.add_vacancy(vacancy, 'data/all.txt')