import json
from abc import ABC, abstractmethod

import requests


class API(ABC):

    @abstractmethod
    def get_vacancies(self, search):
        search_params = {
            'area': 113,  # Поиск в России
            'per_page': 100,  # Кол-во вакансий на 1 странице
            "text": search  # название вакансии
        }
        vac_resp = requests.get('https://api.hh.ru/vacancies', search_params)  # получаем список вакансий по параметрам
        return vac_resp


class HeadHunterAPI(API):


    def get_vacancies(self, search):
        search_params = {
            'area': 113,  # Поиск в России
            'per_page': 100,  # Кол-во вакансий на 1 странице
            "text": search  # название вакансии для поиска
        }
        vac_resp = requests.get('https://api.hh.ru/vacancies', search_params)  # получаем список вакансий по параметрам
        return json.loads(vac_resp.content.decode())


class Vacancy:


    def __init__(self, name=None, url=None, salary=None, requirement=None):
        self.name = name
        self.url = url
        self.salary = salary
        self.requirement = requirement


    def cast_to_object_list(vacancies_obj):
        vacancies_list = []
        for vacancy in vacancies_obj['items']:
            vacancies_list.append(Vacancy(vacancy['name'], vacancy['alternate_url'], vacancy['salary'],vacancy['snippet']['requirement']))
        return vacancies_list


    # def __repr__(self):
    #     return f'{self.name}, {self.url}, {self.salary}, {self.requirement}'