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
        '''

        :param search: вводим название для поиска
        :return: данные для создания обьектов класса Vakancy
        '''
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
        '''
        vacancies_obj: данные для создания обьектов класса Vakancy
        :return: отсортированный по зарплатам список вакансий в кол-ве 100 штук
        '''
        vacancies_list = []
        for vacancy in vacancies_obj['items']:
            # форматируем данные salary для последующей сортировки по з/п
            if vacancy['salary'] is None:
                vacancy['salary'] = {'from': 0, 'to': 0, 'currency': 'RUR', 'gross': False}
            if vacancy['salary']['to'] is None:
                if vacancy['salary']['from'] is None:
                    vacancy['salary'] = {'from': 0, 'to': 0, 'currency': 'RUR', 'gross': False}
                else:
                    vacancy['salary']['to'] = vacancy['salary']['from']
            if vacancy['salary']['from'] is None:
                vacancy['salary']['from'] = vacancy['salary']['to']
            vacancies_list.append(Vacancy(vacancy['name'],
                                          vacancy['alternate_url'],
                                          vacancy['salary'],
                                          vacancy['snippet']['requirement']))
        # добавляем сортировку по з/п
        vacancies_list.sort(key=lambda x: x.salary['to'], reverse=True)

        return vacancies_list


    def get_top_vacancy(vacancies_list, digit):
        '''

        :param digit: количество обьектов в топ
        :return: список топ N вакансий
        '''
        top_vacancy_list = []
        for vacancy in range(digit):
            top_vacancy_list.append(vacancies_list[vacancy])
        return top_vacancy_list


    def filter_vacancies(vacancies_list, filter_words):
        '''

        :param filter_words: слова для фильтрации
        :return: отфильтрованный по ключевым словам список вакансий
        '''
        filtred_list = []
        for word in filter_words:
            for vacancy in vacancies_list:
                if word in vacancy.name:
                    filtred_list.append(vacancy)
        return filtred_list


    def get_vacancies_by_salary(vacancies_list, min_salary, max_salary):
        '''

        :param min_salary: минимум з/п
        :param max_salary: максимум з/п
        :return: список отфильтровнных вакансий
        '''
        salary_list = []
        for vacancy in vacancies_list:
            if min_salary > max_salary:
                max_salary = min_salary
            if min_salary <= int(vacancy.salary['to']) <= max_salary:
                salary_list.append(vacancy)
        return salary_list


    def __str__(self):
        return f'{self.name}, {self.url}, {self.salary}, {self.requirement}'