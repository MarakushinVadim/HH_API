from abc import ABC, abstractmethod


class Save(ABC):

    @abstractmethod
    def add_vacancy(self, vacancy, path):
        with open(path, 'a', encoding='UTF-8') as file:
            file.write(vacancy)


    @abstractmethod
    def delete_vacancy(self, vacancy, path):
        with open(path, 'r', encoding='UTF-8') as deleted:
            deleted = deleted.readlines()
            del_obj = f'{vacancy.name}, {vacancy.url}, {vacancy.salary}, {vacancy.requirement} \n'
            for object in deleted:
                if del_obj in object:
                    deleted.remove(object)
        with open(path, 'w', encoding='UTF-8') as file:
            for string in deleted:
                file.write(string)



class JSONSaver(Save):


    def add_vacancy(self, vacancy, path):
        '''
        :param vacancy: обьект класса Vacancy
        :param path: путь к файлу в который идет сохранение
        :return: сохраняет данные в файл
        '''
        with open(path, 'a', encoding='UTF-8') as file:
            file.write(f'{vacancy.name}, {vacancy.url}, {vacancy.salary}, {vacancy.requirement} \n')


    def delete_vacancy(self, vacancy, path):
        '''
        :param vacancy: обьект класса Vacancy в виде строки в файле
        :param path: путь к файлу
        :return: удаляет строку из файла
        '''
        with open(path, 'r', encoding='UTF-8') as deleted:
            deleted = deleted.readlines()
            for object in deleted:
                if vacancy in object:
                    deleted.remove(object)
        with open(path, 'w', encoding='UTF-8') as file:
            for string in deleted:
                file.write(string)
