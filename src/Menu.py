from src.JSON_saver import JSONSaver


class Menu:

    def __init__(self, vacancies_list, top_n_vac, filtred_vac, fiter_sal, x):
        self.vacancies_list =vacancies_list
        self.top_n_vac = top_n_vac
        self.filtred_vac = filtred_vac
        self.fiter_sal = fiter_sal
        self.json_saver = JSONSaver()
        self.x = x

    def main_menu(self):
        print(f''' 
Для навигации используйте цифровые значения

1 - получить список 100 вакансий
2 - получить топ N вакансий
3 - получить вакансии по ключевым словам
4 - получить вакансии по фильтру з/п
5 - просмотреть и отредактировать избранное
6 - завершить работу программы
''')
        try:
            choice = int(input())
            if isinstance(choice, int):
                if choice == 1:
                    self.get_all_vacancy()

                if choice == 2:
                    self.get_top_vacancy()

                if choice == 3:
                    self.get_filtred_vac()

                if choice == 4:
                    self.get_fiter_sal()

                if choice == 5:
                    self.watch_favorite()

                if choice == 6:
                    self.x = False

        except ValueError:
            print('Введено неверное значение, завершение программы')
            self.x = False




    def get_all_vacancy(self):
        if len(self.vacancies_list) < 1:
            print('по данным критериям ничего не найдено')

        for object in self.vacancies_list:
            print(object)
            print(f'''
1 - добавить в избранное
2 - пропустить
любое другое значение - возврат в главное меню
''')
            try:
                obj_choice = int(input())
            except ValueError:
                print('введено недопустимое значение, возврат в главное меню')
                break
            if isinstance(obj_choice, int):
                if int(obj_choice) == 1:
                    self.json_saver.add_vacancy(object, 'data/favorites.txt')
                elif int(obj_choice) == 2:
                    pass
                else:
                    break
        print('Вы просмотрели весь список, возврат в главное меню')


    def get_top_vacancy(self):
        if len(self.top_n_vac) < 1:
            print('по данным критериям ничего не найдено')
        for object in self.top_n_vac:
            print(object)
            print(f'''
1 - добавить в избранное
2 - пропустить
любое другое значение - возврат в главное меню
''')
            try:
                obj_choice = int(input())
            except ValueError:
                print('введено недопустимое значение, возврат в главное меню')
                break
            if isinstance(obj_choice, int):
                if int(obj_choice) == 1:
                    self.json_saver.add_vacancy(object, 'data/favorites.txt')
                elif int(obj_choice) == 2:
                    pass
                else:
                    break
        print('Вы просмотрели весь список, возврат в главное меню')


    def get_filtred_vac(self):
        if len(self.filtred_vac) < 1:
            print('по данным критериям ничего не найдено')
        for object in self.filtred_vac:
            print(object)
            print(f'''
1 - добавить в избранное
2 - пропустить
любое другое значение - возврат в главное меню
''')
            try:
                obj_choice = int(input())
            except ValueError:
                print('введено недопустимое значение, возврат в главное меню')
                break
            if isinstance(obj_choice, int):
                if int(obj_choice) == 1:
                    self.json_saver.add_vacancy(object, 'data/favorites.txt')
                elif int(obj_choice) == 2:
                    pass
                else:
                    break
        print('Вы просмотрели весь список, возврат в главное меню')


    def get_fiter_sal(self):
        if len(self.fiter_sal) < 1:
            print('по данным критериям ничего не найдено')
        for object in self.fiter_sal:
            print(object)
            print(f'''
1 - добавить в избранное
2 - пропустить
любое другое значение - возврат в главное меню
''')
            try:
                obj_choice = int(input())
            except ValueError:
                print('введено недопустимое значение, возврат в главное меню')
                break
            if isinstance(obj_choice, int):
                if int(obj_choice) == 1:
                    self.json_saver.add_vacancy(object, 'data/favorites.txt')
                elif int(obj_choice) == 2:
                    pass
                else:
                    break
        print('Вы просмотрели весь список, возврат в главное меню')


    def watch_favorite(self):
        print(f'''
1 - просмотреть весь список
2 - просмотр и редактирование списка по одной позиции
любое другое значение - возврат в главное меню
''')
        try:
            choice = int(input())
            if isinstance(choice, int):
                with open('data/favorites.txt', 'r', encoding='UTF-8') as file:
                    file = file.readlines()
                    if len(file) < 1:
                        print('список пуст')
                if choice == 1:
                        for object in file:
                            print(object)

                elif choice == 2:
                    for object in file:
                        print(object)
                        print(f'''
1 - далее
2 - удалить
''')

                        try:
                            local_choice = int(input())
                            if local_choice == 2:
                                self.json_saver.delete_vacancy(object, 'data/favorites.txt')
                            else:
                                pass
                        except ValueError:
                            print('введено недопустимое значение, возврат в главное меню')
                            break
                        print("Вы просмотрели весь список, возврат в главное меню")
                else:
                    print('введено недопустимое значение')



        except ValueError:
            print('введено недопустимое значение')
