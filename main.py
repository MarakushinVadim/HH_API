import json

import requests

from src.HeadHunterAPI import HeadHunterAPI, Vacancy
from src.JSON_saver import JSONSaver

hh_api = HeadHunterAPI()
hh_vacancies = hh_api.get_vacancies("Python")
vacancies_list = Vacancy.cast_to_object_list(hh_vacancies)
print(vacancies_list[0].name)
print(vacancies_list[0].url)
print(vacancies_list[0].salary)
print(vacancies_list[0].requirement)
print(type(vacancies_list[0]))

json_saver = JSONSaver()
# json_saver.add_vacancy(vacancies_list[13])
json_saver.delete_vacancy(vacancies_list[0])







