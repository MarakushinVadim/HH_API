import json

import requests

from src.HeadHunterAPI import HeadHunterAPI, Vacancy
from src.JSON_saver import JSONSaver

if __name__ == '__main__':
    platforms = ['HeadHunter']
    search_query = input('Введите поисковый запрос: ')
    top_n = int(input("Введите количество вакансий для вывода в топ N: "))
    filter_words = input("Введите ключевые слова для фильтрации вакансий через пробел: ").split(' ')
    salary_range_min = int(input("Введите нижнюю границу зарплат: "))
    salary_range_max = int(input("Введите верхнюю границу зарплат: "))


    f = open('data/favorites.txt', 'w')
    f.close()


    f = open('data/all.txt', 'w')
    f.close()


    if salary_range_min > salary_range_max:
        salary_range_max = salary_range_min
        print(f'Вы ввели некорректный диапазон для фильтрации'
              f'параметр salary_range_max изменен и равен salary_range_min')



    hh_api = HeadHunterAPI()
    hh_vacancies = hh_api.get_vacancies(search_query)
    vacancies_list = Vacancy.cast_to_object_list(hh_vacancies)
    json_saver = JSONSaver()

    for vacancy in vacancies_list:
        json_saver.add_vacancy(vacancy, 'data/all.txt')

    top_n_vac = Vacancy.get_top_vacancy(vacancies_list, top_n)
    print(top_n_vac)

    filtred_vac = Vacancy.filter_vacancies(vacancies_list, filter_words)
    print(filtred_vac)

    fiter_sal = Vacancy.get_vacancies_by_salary(vacancies_list, salary_range_min, salary_range_max)
    print(fiter_sal)

    choice = int(input(f'''Списки составленны, данные записаны 
Для навигации используйте цифровые значения

1 - получить топ N вакансий
2 - получить вакансии по ключевым словам
3 - получить вакансии по фильтру з/п
'''))
    print()

    if choice == 1:
        for object in top_n_vac:
            print(object)
            obj_choice = int(input(f'''1 - добавить в избранное
2 - пропустить
3 - прервать просмотр
'''))
            if obj_choice == 1:
                 json_saver.add_vacancy(object, 'data/favorites.txt')



    # for object in filtred_vac:
    #     json_saver.add_vacancy(object)







    #
    # print(search_query, top_n, filter_words, salary_range_min, salary_range_max)
    #
    #




# for vacancy in vacancies_list:
#     json_saver.add_vacancy(vacancy)



# for object in fiter_sal:
#     json_saver.add_vacancy(object)

# for object in top_n:          сохранение топ-20
#     json_saver.add_vacancy(object)    сохранение топ-20
# print(top_n)    сохранение топ-20



# print(vacancies_list[0].name)
# print(vacancies_list[0].salary)
# print(vacancies_list[0].requirement)
# print(type(vacancies_list[0]))


# json_saver.add_vacancy(vacancies_list)
# json_saver.delete_vacancy(vacancies_list[0])







