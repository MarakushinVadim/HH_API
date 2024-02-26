from src.HeadHunterAPI import HeadHunterAPI, Vacancy
from src.JSON_saver import JSONSaver
from src.Menu import Menu

if __name__ == '__main__':
    platforms = ['HeadHunter']
    search_query = input('Введите поисковый запрос: ')

    filter_words = input("Введите ключевые слова для фильтрации вакансий через пробел: ").split(' ')

    # Запускаем циклы на проверку являются ли введенные данные цтфровыми значениями
    while True:
        try:
            top_n = int(input("Введите количество вакансий для вывода в топ N: "))
            break
        except ValueError:
            print('Введите цифровое значение')

    while True:
        try:
            salary_range_min = int(input("Введите нижнюю границу зарплат: "))
            break
        except ValueError:
            print('Введите цифровое значение')

    while True:
        try:
            salary_range_max = int(input("Введите верхнюю границу зарплат: "))
            break
        except ValueError:
            print('Введите цифровое значение')

    # Создаем файлы для работы
    f = open('data/favorites.txt', 'w')
    f.close()


    f = open('data/all.txt', 'w')
    f.close()

    # Создаем необходимые экземпляры классов
    hh_api = HeadHunterAPI()
    hh_vacancies = hh_api.get_vacancies(search_query)
    vacancies_list = Vacancy.cast_to_object_list(hh_vacancies)
    json_saver = JSONSaver()

    # сохраняем все найденные вакансии в файл
    for vacancy in vacancies_list:
        json_saver.add_vacancy(vacancy, 'data/all.txt')

    # инициализируем списки согласно потребности
    top_n_vac = Vacancy.get_top_vacancy(vacancies_list, top_n)

    filtred_vac = Vacancy.filter_vacancies(vacancies_list, filter_words)

    fiter_sal = Vacancy.get_vacancies_by_salary(vacancies_list, salary_range_min, salary_range_max)

    x = True

    # создаем экземпляр класса меню
    menu = Menu(vacancies_list, top_n_vac, filtred_vac, fiter_sal, x)

    print("Списки составленны, данные записаны")

    # запускаем класс меню в работу
    while menu.x is True:
        menu.main_menu()
