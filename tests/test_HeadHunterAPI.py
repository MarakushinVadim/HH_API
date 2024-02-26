import pytest

from src.HeadHunterAPI import HeadHunterAPI, Vacancy


search = 'Python'

hh_api = HeadHunterAPI()

hh_vacancies = hh_api.get_vacancies(search)
def test_get_vacancies():
    assert len(hh_vacancies) > 0

vacancies_list = Vacancy.cast_to_object_list(hh_vacancies)

def test_cast_to_object_list():
    for vacancy in vacancies_list:
        assert isinstance(vacancy, Vacancy)
    assert vacancies_list[0].salary['to'] >= vacancies_list[1].salary['to']# проверка на правильность сортировки

digit = 5
def test_get_top_vacancy():
    top_n_vac = Vacancy.get_top_vacancy(vacancies_list, digit)
    assert len(top_n_vac) == digit
    assert top_n_vac[0].salary['to'] >= top_n_vac[4].salary['to']

filter_words = ['IT']
filtred_vac = Vacancy.filter_vacancies(vacancies_list, filter_words)

def test_filter_vacancies():
    for vacancy in filtred_vac:
        assert filter_words[0] in vacancy.name


salary_range_min = 100000
salary_range_max = 150000
fiter_sal = Vacancy.get_vacancies_by_salary(vacancies_list, salary_range_min, salary_range_max)

def test_get_vacancies_by_salary():
    for vacancy in fiter_sal:
        assert salary_range_max >= vacancy.salary['to'] >= salary_range_min
